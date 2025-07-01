from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)
DB = 'bug_tracker.db'

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    
    # Create issues table without AUTOINCREMENT
    c.execute('''CREATE TABLE IF NOT EXISTS issues (
                    id INTEGER PRIMARY KEY,
                    title TEXT NOT NULL,
                    description TEXT,
                    status TEXT DEFAULT 'Open',
                    priority TEXT DEFAULT 'Medium',
                    assignee TEXT,
                    date TEXT
                )''')
    
    # Create counter table for managing IDs
    c.execute('''CREATE TABLE IF NOT EXISTS id_counter (
                    next_id INTEGER DEFAULT 1
                )''')
    
    # Initialize counter if empty
    c.execute("INSERT OR IGNORE INTO id_counter (next_id) VALUES (1)")
    
    conn.commit()
    conn.close()

def get_next_id():
    """Get the next available ID and increment the counter"""
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    
    try:
        # Get current next_id
        c.execute("SELECT next_id FROM id_counter")
        current_id = c.fetchone()[0]
        
        # Increment the counter
        c.execute("UPDATE id_counter SET next_id = next_id + 1")
        
        conn.commit()
        return current_id
    finally:
        conn.close()

def reorder_ids():
    """Reorders IDs to be sequential after deletion"""
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    
    try:
        # Get all records ordered by current ID
        c.execute("SELECT * FROM issues ORDER BY id")
        all_records = c.fetchall()
        
        # Clear the issues table
        c.execute("DELETE FROM issues")
        
        # Reset the counter
        c.execute("UPDATE id_counter SET next_id = 1")
        
        # Re-insert all records with new sequential IDs
        for i, record in enumerate(all_records, 1):
            c.execute("INSERT INTO issues (id, title, description, status, priority, assignee, date) VALUES (?, ?, ?, ?, ?, ?, ?)",
                      (i, record[1], record[2], record[3], record[4], record[5], record[6]))
        
        # Update counter to next available ID
        c.execute("UPDATE id_counter SET next_id = ?", (len(all_records) + 1,))
        
        conn.commit()
    finally:
        conn.close()

@app.route('/')
def index():
    priority_filter = request.args.get('priority', '')
    
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    
    if priority_filter:
        c.execute("SELECT * FROM issues WHERE priority = ? ORDER BY id DESC", (priority_filter,))
    else:
        c.execute("SELECT * FROM issues ORDER BY id DESC")
    
    issues = c.fetchall()
    conn.close()
    
    return render_template('index.html', issues=issues, selected_priority=priority_filter)

@app.route('/add', methods=['GET', 'POST'])
def add_issue():
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['description']
        priority = request.form['priority']
        assignee = request.form['assignee']
        date = datetime.now().strftime('%Y-%m-%d')
        
        # Get next available ID
        new_id = get_next_id()
        
        conn = sqlite3.connect(DB)
        c = conn.cursor()
        c.execute("INSERT INTO issues (id, title, description, priority, assignee, date) VALUES (?, ?, ?, ?, ?, ?)",
                  (new_id, title, desc, priority, assignee, date))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add_issue.html')

@app.route('/update/<int:id>/<status>')
def update_status(id, status):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("UPDATE issues SET status=? WHERE id=?", (status, id))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_issue(id):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("DELETE FROM issues WHERE id=?", (id,))
    conn.commit()
    conn.close()
    
    # Reorder IDs after deletion
    reorder_ids()
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
