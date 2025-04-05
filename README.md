# Task Manager Web Application

![Task Manager Screenshot](./image.png) <!-- Replace with your actual screenshot file -->

A feature-rich task management web application built with Python Flask and SQLite.

## Features ✨
- ✅ Full CRUD (Create, Read, Update, Delete) operations
- 🏷️ Task status filtering (All/Pending/In Progress/Completed)
- 📅 Due date management
- 📊 Real-time statistics dashboard
- 🎨 Modern UI with hover animations
- 📱 Fully responsive design

## Prerequisites 📋
- Python 3.6+
- pip package manager
- Web browser

## Installation 🛠️

### 1. Clone the repository
```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
cd YOUR-REPO-NAME
2. Install dependencies
bash
Copy
pip install -r requirements.txt
If you don't have requirements.txt:

bash
Copy
pip install flask
3. Initialize database (automatic)
The database (database.db) will be created automatically on first run.

Running the Application 🚀
bash
Copy
python app.py
Access the application at:
http://localhost:5000

Project Structure 📂
Copy
.
├── app.py                 # Main application logic
├── static/                # Static assets
│   ├── custom.css         # Custom styles
│   └── custom.js          # Interactive features
├── templates/             # HTML templates
│   ├── base.html          # Base template
│   ├── index.html         # Main interface
│   └── task_form.html     # Task creation/editing form
├── database.db            # SQLite database (auto-generated)
└── README.md              # This documentation
Usage Guide 📖
Creating a Task
Click "+ New Task" (top-right)

Fill in task details

Click "Create Task"

Create Task Demo <!-- Add screenshot -->

Editing a Task
Click the ✏️ (Edit) icon on any task

Modify task details

Click "Update Task"

Deleting a Task
Click the 🗑️ (Trash) icon on any task

Confirm deletion

Filtering Tasks
Use the status buttons to filter tasks:

All Tasks

Pending

In Progress

Completed

Database Management 🔍
Install DB Browser for SQLite

Open database.db from project root

View the tasks table:

Database View <!-- Add database screenshot -->

Troubleshooting 🚨
Issue	Solution
Missing dependencies	pip install -r requirements.txt
Port 5000 in use	python app.py --port=5001
Database issues	Delete database.db and restart app
Form not submitting	Ensure all required fields are filled
Contributing 🤝
Fork the repository

Create feature branch:
git checkout -b feature/awesome-feature

Commit changes:
git commit -m 'Add awesome feature'

Push to branch:
git push origin feature/awesome-feature

Open a Pull Request

License 📄
Distributed under the MIT License. See LICENSE for more information.
