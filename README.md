# 💸 WalletWatch

A personal finance tracker built with Django to help users efficiently manage and visualize their daily transactions, monitor monthly spending, and maintain a healthy financial balance.

---

## 🚀 Tech Stack

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Django](https://img.shields.io/badge/Django-4.2-green)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey)
![Chart.js](https://img.shields.io/badge/Charts-Chart.js-orange)

---

## 📚 Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Screenshots](#screenshots)
4. [Setup Instructions](#setup-instructions)
5. [Folder Structure](#folder-structure)
6. [Future Enhancements](#future-enhancements)
7. [License](#license)

---

## 🔍 Introduction

**WalletWatch** is a web-based financial tracker application where users can:
- Log income and expense transactions
- View summaries and visual charts
- Filter transactions by date and category
- Export data in CSV format
- Switch between Light and Dark mode for better UX

---

## ✨ Features

- 🔐 User Authentication (Register/Login/Logout)
- 📆 Date Range Filtering
- 📊 Doughnut Chart for Income vs Expense
- 💾 Monthly Summary Table and Export
- 🌙 Dark Mode Toggle
- 🧠 Smart validations on registration (password strength & matching)
- 🧹 Clean and responsive UI using Bootstrap 5

---

## 🖼️ Screenshots

| Register Page | Dark Mode Dashboard |
|--------------|---------------------|
| ![register](static/screens/register page.png) | ![dark-mode](static/screens/Dark Mode.png) |

> ⚠️ Add screenshots to the `static/screens/` folder for them to render.

---

## ⚙️ Setup Instructions

1. **Clone the repo**
    ```bash
    git clone https://github.com/poojab2813/WalletWatch.git
    cd WalletWatch
    ```

2. **Create a virtual environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # or venv\Scripts\activate on Windows
    ```

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run migrations**
    ```bash
    python manage.py migrate
    ```

5. **Run the server**
    ```bash
    python manage.py runserver
    ```

6. **Access**
    - Navigate to `http://127.0.0.1:8000/`

---

## 🗂️ Folder Structure (simplified)

```
WalletWatch/
├── tracker/                # Main Django app
│   ├── models.py           # Transaction model
│   ├── views.py            # Core views (add/edit/delete/export)
│   ├── forms.py            # Django forms for transaction input
│   └── templates/tracker/  # HTML templates
├── static/                 # Static files (CSS, JS, images)
├── db.sqlite3              # SQLite DB
├── manage.py
└── requirements.txt
```

---

## 🔮 Future Enhancements

- ✅ OAuth login (Google/GitHub)
- ✅ Email-based verification
- ✅ Expense category suggestions
- ✅ Progressive Web App (PWA) integration

---

## 📄 License

This project is licensed under the MIT License. Feel free to fork and enhance.

---

> 💡 Built with ❤️ by [Pooja Bavisetti](https://github.com/poojab2813)
