# Task Manager Web Application

A Flask-based web application for managing tasks with CRUD operations and status tracking.

![Task Manager Screenshot](image.png)

## Features
- Create, Read, Update, and Delete tasks
- Filter tasks by status (Pending/In Progress/Completed)
- Modern UI with responsive design
- SQLite database integration

## Prerequisites
- Python 3.6+
- pip package manager

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
cd YOUR-REPO-NAME
Install dependencies

bash
Copy
pip install -r requirements.txt
Initialize the database

bash
Copy
python app.py
Running the Application
bash
Copy
python app.py
Access the application at:
http://localhost:5000

Usage
Create Task: Click "+ New Task" (top-right)

Edit Task: Click the pencil (✏️) icon

Delete Task: Click the trash (🗑️) icon

Filter Tasks: Use status buttons (All/Pending/In Progress/Completed)

Project Structure
Copy
├── app.py
├── static/
│   ├── custom.css
│   └── custom.js
├── templates/
│   ├── base.html
│   ├── index.html
│   └── task_form.html
├── database.db (auto-generated)
└── README.md
View Database
Install DB Browser for SQLite

Open database.db file

View the tasks table

Troubleshooting
Missing dependencies: Run pip install flask

Port conflict: Change port in app.py (modify app.run(port=5001))

Database issues: Delete database.db and restart the app

Copy

**To use this:**
1. Create a new file named `README.md`
2. Copy-paste this content
3. Replace these placeholders:
   - `YOUR-USERNAME/YOUR-REPO-NAME` with your GitHub details
   - `image.png` with your actual screenshot filename
4. Add a `requirements.txt` file using:
```bash
pip freeze > requirements.txt
