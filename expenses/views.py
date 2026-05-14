from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Group, Expense, ExpenseSplit
from .forms import UserRegisterForm, GroupForm, ExpenseForm
from django.db.models import Sum
from decimal import Decimal

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'expenses/register.html', {'form': form})

@login_required
def dashboard(request):
    groups = request.user.expense_groups.all()
    
    # Calculate total owed by user (to others)
    total_owed = ExpenseSplit.objects.filter(
        user=request.user, 
        is_settled=False
    ).exclude(expense__paid_by=request.user).aggregate(Sum('amount'))['amount__sum'] or Decimal('0.00')
    
    # Calculate total owed to user (from others)
    total_owed_to_user = ExpenseSplit.objects.filter(
        expense__paid_by=request.user, 
        is_settled=False
    ).exclude(user=request.user).aggregate(Sum('amount'))['amount__sum'] or Decimal('0.00')

    # Recent expenses
    recent_expenses = Expense.objects.filter(group__in=groups).order_by('-date')[:5]

    context = {
        'groups': groups,
        'total_owed': total_owed,
        'total_owed_to_user': total_owed_to_user,
        'recent_expenses': recent_expenses
    }
    return render(request, 'expenses/dashboard.html', context)

@login_required
def create_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save()
            if request.user not in group.members.all():
                group.members.add(request.user)
            messages.success(request, f'Group "{group.name}" created successfully!')
            return redirect('dashboard')
    else:
        form = GroupForm(initial={'members': [request.user]})
    return render(request, 'expenses/create_group.html', {'form': form})

@login_required
def group_detail(request, group_id):
    group = get_object_or_404(Group, id=group_id, members=request.user)
    
    # Calculate balances
    # We want a matrix of who owes whom. Or simply a list of debts.
    # To keep it simple: we aggregate all unsettled splits for this group.
    
    splits = ExpenseSplit.objects.filter(expense__group=group, is_settled=False)
    
    # balance_map[(debtor_id, creditor_id)] = amount
    balance_map = {}
    
    for split in splits:
        debtor = split.user
        creditor = split.expense.paid_by
        if debtor == creditor:
            continue
            
        pair = (debtor, creditor)
        reverse_pair = (creditor, debtor)
        
        amount = split.amount
        
        # If the reverse debt exists, we offset it
        if reverse_pair in balance_map:
            if balance_map[reverse_pair] > amount:
                balance_map[reverse_pair] -= amount
            elif balance_map[reverse_pair] < amount:
                amount -= balance_map[reverse_pair]
                del balance_map[reverse_pair]
                balance_map[pair] = amount
            else:
                del balance_map[reverse_pair]
        else:
            balance_map[pair] = balance_map.get(pair, Decimal('0.00')) + amount

    balances = []
    for (debtor, creditor), amount in balance_map.items():
        balances.append({
            'debtor': debtor,
            'creditor': creditor,
            'amount': amount
        })

    context = {
        'group': group,
        'balances': balances,
    }
    return render(request, 'expenses/group_detail.html', context)

@login_required
def add_expense(request, group_id):
    group = get_object_or_404(Group, id=group_id, members=request.user)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, group=group)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.group = group
            expense.save()
            
            participants = form.cleaned_data['participants']
            if participants.exists():
                split_amount = expense.amount / Decimal(participants.count())
                for participant in participants:
                    ExpenseSplit.objects.create(
                        expense=expense,
                        user=participant,
                        amount=split_amount
                    )
            messages.success(request, 'Expense added successfully!')
            return redirect('group_detail', group_id=group.id)
    else:
        form = ExpenseForm(group=group, initial={'paid_by': request.user, 'participants': group.members.all()})
    return render(request, 'expenses/add_expense.html', {'form': form, 'group': group})

@login_required
def expense_history(request, group_id):
    group = get_object_or_404(Group, id=group_id, members=request.user)
    expenses = group.expenses.all().order_by('-date')
    return render(request, 'expenses/expense_history.html', {'group': group, 'expenses': expenses})

@login_required
def settle_up(request, group_id, debtor_id, creditor_id):
    group = get_object_or_404(Group, id=group_id, members=request.user)
    # Only allow the debtor or creditor to settle
    if request.user.id not in [debtor_id, creditor_id]:
        messages.error(request, "You can only settle your own balances.")
        return redirect('group_detail', group_id=group.id)
        
    # Mark splits where debtor owes creditor as settled
    splits = ExpenseSplit.objects.filter(
        expense__group=group,
        user_id=debtor_id,
        expense__paid_by_id=creditor_id,
        is_settled=False
    )
    splits.update(is_settled=True)
    
    messages.success(request, 'Balance settled successfully!')
    return redirect('group_detail', group_id=group.id)
