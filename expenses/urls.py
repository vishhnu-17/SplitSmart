from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='expenses/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    
    path('dashboard/', views.dashboard, name='dashboard'),
    path('group/create/', views.create_group, name='create_group'),
    path('group/<int:group_id>/', views.group_detail, name='group_detail'),
    path('group/<int:group_id>/expense/add/', views.add_expense, name='add_expense'),
    path('group/<int:group_id>/expense/history/', views.expense_history, name='expense_history'),
    path('group/<int:group_id>/settle/<int:debtor_id>/<int:creditor_id>/', views.settle_up, name='settle_up'),
]
