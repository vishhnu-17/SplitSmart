#  SplitSmart — Minimalist Expense Splitter

**SplitSmart** is a clean, full-stack Django web application designed to help friends and roommates split expenses without the stress. It's a simplified Splitwise clone focused on functionality, clean UI, and ease of use.


##  Features

- **User Authentication**: Secure Register, Login, and Logout functionality.
- **Dashboard**: A high-level overview of your total debts and credits across all groups.
- **Group Management**: Create groups and add members to organize your shared costs.
- **Equal Expense Splitting**: Add expenses and automatically split them equally among selected participants.
- **Smart Balance Calculation**: View exactly who owes whom (e.g., "Rahul owes Vishnu ₹200") with net balance logic.
- **Settlement System**: Mark balances as settled with a single click.
- **Modern Responsive UI**: Built with Bootstrap 5, featuring a clean layout that works on desktop and mobile.
- **Dark Mode**: Built-in light and dark mode toggle with preference persistence (localStorage).



## Tech Stack

- **Backend**: Django (Python)
- **Database**: SQLite (Beginner-friendly & lightweight)
- **Frontend**: HTML5, CSS3, JavaScript (ES6)
- **Styling**: Bootstrap 5 (Minimal & modern)
- **Icons**: Bootstrap Icons


##  Outputs
<img width="1919" height="1079" alt="Screenshot 2026-05-14 203451" src="https://github.com/user-attachments/assets/10ec5358-b76d-4087-88dc-c3aec2e59080" />
<img width="1911" height="1078" alt="Screenshot 2026-05-14 203227" src="https://github.com/user-attachments/assets/557861ee-ef6a-4bea-89a6-f3ac6bbbf6f1" />
<img width="1917" height="1079" alt="Screenshot 2026-05-14 203532" src="https://github.com/user-attachments/assets/3390f883-21f4-4383-a6f7-6920d0a1c906" />
<img width="1914" height="1079" alt="Screenshot 2026-05-14 212856" src="https://github.com/user-attachments/assets/35084ef0-303f-4940-b1d8-9d1701d61004" />
<img width="1916" height="1074" alt="Screenshot 2026-05-14 212915" src="https://github.com/user-attachments/assets/a5fa2dc2-29ad-4798-bf30-6ba907e81be2" />
<img width="1920" height="1080" alt="Screenshot 2026-05-14 213034" src="https://github.com/user-attachments/assets/0e81d818-ecf8-401c-a136-c83df82b15b4" />
<img width="1920" height="1080" alt="Screenshot 2026-05-14 213103" src="https://github.com/user-attachments/assets/1442dc05-db94-4ccc-8cd6-ab8a9aaa1007" />
<img width="1920" height="1080" alt="Screenshot 2026-05-14 213137" src="https://github.com/user-attachments/assets/4810fb5d-20f5-4d31-adc8-d3ea35bb67ad" />
<img width="1920" height="1080" alt="Screenshot 2026-05-14 213201" src="https://github.com/user-attachments/assets/0b9d5a7a-a7b7-4003-82c6-a2e07402eb28" />
<img width="1920" height="1080" alt="Screenshot 2026-05-14 213240" src="https://github.com/user-attachments/assets/fad6a68f-4717-4cd4-9a49-fd9befa9f59a" />
<img width="1920" height="1080" alt="Screenshot 2026-05-14 213323" src="https://github.com/user-attachments/assets/1d646b9d-8c0b-4f8d-a7ad-2d87486070d7" />





##  Installation & Setup

### Prerequisites

- Python 3.8+ installed on your machine.

### Steps to Run Locally

1. **Clone the repository:**

```bash
git clone https://github.com/YOUR_USERNAME/splitsmart.git
cd splitsmart
```

2. **Install Django:**

```bash
pip install django
```

3. **Run Migrations:**

```bash
python manage.py makemigrations expenses
python manage.py migrate
```

4. **Start the development server:**

```bash
python manage.py runserver
```

5. **Access the app:**

Open [http://127.0.0.1:8000/register/](http://127.0.0.1:8000/register/) in your browser and create your first account.


## Project Structure

```
splitsmart/
├── expenses/             # Main app (Models, Views, Forms, URLs)
│   ├── models.py         # Group, Expense, ExpenseSplit models
│   ├── views.py          # All view logic and balance calculation
│   ├── forms.py          # Register, Group, Expense forms
│   └── urls.py           # App-level URL routing
├── splitsmart/           # Core project configuration
│   ├── settings.py
│   └── urls.py
├── templates/            # HTML Templates (Base, Dashboard, Auth, etc.)
│   ├── base.html
│   └── expenses/
│       ├── dashboard.html
│       ├── login.html
│       ├── register.html
│       ├── group_detail.html
│       ├── create_group.html
│       ├── add_expense.html
│       └── expense_history.html
├── manage.py
└── db.sqlite3
```


##  Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to check the [issues page](https://github.com/vishhnu-17/splitsmart/issues).

---

##  License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).
