# Task Manager Web Application

![Task Manager Screenshot](image.png)

## Features
- **CRUD Operations**:
  - Create, Read, Update, and Delete tasks
  - 🗑️ Delete Task: Click the trash icon
- **Filtering**: Use status buttons (All/Pending/In Progress/Completed)
- **Database**: SQLite integration
- **Responsive Design**: Works on all screen sizes

## Project Structure
├── app.py # Main Flask application
├── static/ # Static assets
│ ├── custom.css # Custom styles
│ └── custom.js # Interactive scripts
├── templates/ # HTML templates
│ ├── base.html # Base template
│ ├── index.html # Task listing
│ └── task_form.html # Add/Edit form
├── database.db # Auto-generated database
└── README.md # Documentation


## View Database
1. Download [DB Browser for SQLite](https://sqlitebrowser.org/)
2. Open `database.db` file
3. Navigate to **Browse Data** tab
4. View the `tasks` table

## Troubleshooting
- **Missing dependencies**:
  ```bash
  pip install flask
Port conflict:

bash
Copy
python app.py --port=5001
Database issues:

bash
Copy
rm database.db && python app.py
To Run:

Clone repository:

bash
Copy
git clone https://github.com/YOUR-USERNAME/REPO-NAME.git
Install dependencies:

bash
Copy
pip install -r requirements.txt
Start application:

bash
Copy
python app.py
Visit http://localhost:5000

Copy

**Key Improvements**:
1. Proper code block formatting with triple backticks (```)
2. Consistent indentation for file structure
3. Emoji icons for better visual guidance
4. Clear section headers with hierarchy
5. Proper bash command formatting
6. Organized bullet points with sub-items

To use this template:
1. Replace `YOUR-USERNAME/REPO-NAME` with your GitHub details
2. Ensure `image.png` exists in your repository
3. Add a `requirements.txt` file if missing:
   ```bash
   pip freeze > requirements.txt
