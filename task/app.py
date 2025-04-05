from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os
from datetime import datetime

app = Flask(__name__)
DATABASE = 'database.db'

def init_db():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            status TEXT NOT NULL DEFAULT 'Pending',
            due_date DATE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    search_query = request.args.get('search', '')
    status_filter = request.args.get('status', 'all')
    
    conn = get_db_connection()
    query = "SELECT * FROM tasks WHERE 1=1"
    params = []
    
    if search_query:
        query += " AND (title LIKE ? OR description LIKE ?)"
        params.extend([f'%{search_query}%', f'%{search_query}%'])
    
    if status_filter != 'all':
        query += " AND status = ?"
        params.append(status_filter)
    
    query += " ORDER BY due_date ASC, created_at DESC"
    
    tasks = conn.execute(query, params).fetchall()
    stats = conn.execute('SELECT status, COUNT(*) as count FROM tasks GROUP BY status').fetchall()
    conn.close()
    
    return render_template('index.html', 
                         tasks=tasks, 
                         stats=stats, 
                         status_filter=status_filter, 
                         search_query=search_query)

# Updated routes with explicit endpoints
@app.route('/task/new', methods=['GET', 'POST'], endpoint='new_task')
@app.route('/task/<int:task_id>', methods=['GET', 'POST'], endpoint='edit_task')
def task_form(task_id=None):
    conn = get_db_connection()
    
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        status = request.form['status']
        due_date = request.form['due_date'] or None
        
        if task_id:
            conn.execute('''
                UPDATE tasks SET
                title=?, description=?, status=?, due_date=?
                WHERE id=?
            ''', (title, description, status, due_date, task_id))
        else:
            conn.execute('''
                INSERT INTO tasks (title, description, status, due_date)
                VALUES (?, ?, ?, ?)
            ''', (title, description, status, due_date))
        
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    
    task = conn.execute('SELECT * FROM tasks WHERE id = ?', (task_id,)).fetchone() if task_id else None
    conn.close()
    return render_template('task_form.html', task=task)

@app.route('/delete/<int:task_id>')
def delete(task_id):
    conn = get_db_connection()
    conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    if not os.path.exists(DATABASE):
        init_db()
    app.run(debug=True)