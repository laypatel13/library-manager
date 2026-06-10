# 📚 Library Manager - CLI

A simple command-line Library Manager built using Python.
This project helps you track your books, manage reading progress, and maintain your personal library with a colorful and neatly formatted interface.

---

## ✨ Features

- Add books with title, author, and publication year
- View all books in a formatted table
- View only unread books
- Mark books as read
- Save data in a JSON file (`books.json`)
- Reset entire library when needed
- Colorful CLI output for better readability

---

## 📦 Install via pip

```bash
pip install laypatel13-library-manager
```

Then run it from anywhere in your terminal:

```bash
library-manager
```

---

## 🛠️ Install from source

```bash
git clone https://github.com/laypatel13/library-manager.git
cd library-manager
pip install -r requirements.txt
pip install -e .
```

Then run:

```bash
library-manager
```

---

## 📂 Project Structure

```text
library-manager/
├── library_manager/
│   ├── __init__.py
│   └── main.py
├── pyproject.toml
├── requirements.txt
└── README.md
```

---

## 🧰 Built With

- Used [Colorama](https://pypi.org/project/colorama/) for colored terminal output.
- Used [Tabulate](https://pypi.org/project/tabulate/) for formatted table display.