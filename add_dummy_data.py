import sqlite3
from datetime import datetime, timedelta
import random

def add_dummy_data():
    conn = sqlite3.connect('bug_tracker.db')
    c = conn.cursor()
    
    # Dummy data
    dummy_issues = [
        {
            'title': 'Login page not responsive on mobile',
            'description': 'The login form elements are overlapping on screens smaller than 768px. Need to fix CSS media queries.',
            'status': 'Open',
            'priority': 'High',
            'assignee': 'Sarah Chen',
            'date': (datetime.now() - timedelta(days=5)).strftime('%Y-%m-%d')
        },
        {
            'title': 'Database connection timeout error',
            'description': 'Users experiencing timeout errors when trying to save large files. Connection pool may need optimization.',
            'status': 'In Progress',
            'priority': 'High',
            'assignee': 'Mike Johnson',
            'date': (datetime.now() - timedelta(days=3)).strftime('%Y-%m-%d')
        },
        {
            'title': 'Search functionality broken',
            'description': 'Search results are not displaying correctly. Query optimization needed.',
            'status': 'Closed',
            'priority': 'Medium',
            'assignee': 'Alex Rodriguez',
            'date': (datetime.now() - timedelta(days=10)).strftime('%Y-%m-%d')
        },
        {
            'title': 'Email notifications not sending',
            'description': 'Users are not receiving email notifications for important updates. SMTP configuration issue.',
            'status': 'Open',
            'priority': 'High',
            'assignee': 'Lisa Wang',
            'date': (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
        },
        {
            'title': 'Dashboard loading slowly',
            'description': 'Dashboard takes more than 5 seconds to load. Need to optimize database queries and add caching.',
            'status': 'In Progress',
            'priority': 'Medium',
            'assignee': 'David Kim',
            'date': (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')
        },
        {
            'title': 'User profile image upload failing',
            'description': 'Users cannot upload profile pictures. File size validation is too restrictive.',
            'status': 'Open',
            'priority': 'Low',
            'assignee': 'Emma Wilson',
            'date': (datetime.now() - timedelta(days=2)).strftime('%Y-%m-%d')
        },
        {
            'title': 'API rate limiting not working',
            'description': 'Rate limiting middleware is not properly blocking excessive requests. Security concern.',
            'status': 'In Progress',
            'priority': 'High',
            'assignee': 'Tom Anderson',
            'date': (datetime.now() - timedelta(days=4)).strftime('%Y-%m-%d')
        },
        {
            'title': 'Password reset link expired too quickly',
            'description': 'Password reset links expire after 1 hour, should be 24 hours for better user experience.',
            'status': 'Closed',
            'priority': 'Low',
            'assignee': 'Rachel Green',
            'date': (datetime.now() - timedelta(days=15)).strftime('%Y-%m-%d')
        },
        {
            'title': 'Dark mode toggle not working',
            'description': 'Dark mode preference is not being saved and applied correctly across sessions.',
            'status': 'Open',
            'priority': 'Medium',
            'assignee': 'Chris Lee',
            'date': (datetime.now() - timedelta(days=6)).strftime('%Y-%m-%d')
        },
        {
            'title': 'Export to PDF feature broken',
            'description': 'PDF export is generating corrupted files. Need to fix PDF generation library.',
            'status': 'In Progress',
            'priority': 'Medium',
            'assignee': 'Maria Garcia',
            'date': (datetime.now() - timedelta(days=8)).strftime('%Y-%m-%d')
        },
        {
            'title': 'Mobile app crashes on startup',
            'description': 'App crashes immediately after launch on Android devices running version 11 and below.',
            'status': 'Open',
            'priority': 'High',
            'assignee': 'James Brown',
            'date': (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
        },
        {
            'title': 'Calendar integration not syncing',
            'description': 'Google Calendar integration is not syncing events properly. API authentication issue.',
            'status': 'Closed',
            'priority': 'Medium',
            'assignee': 'Sophie Turner',
            'date': (datetime.now() - timedelta(days=12)).strftime('%Y-%m-%d')
        },
        {
            'title': 'File upload progress bar stuck',
            'description': 'Progress bar shows 100% but upload never completes. JavaScript event handling issue.',
            'status': 'Open',
            'priority': 'Low',
            'assignee': 'Kevin Zhang',
            'date': (datetime.now() - timedelta(days=3)).strftime('%Y-%m-%d')
        },
        {
            'title': 'User permissions not updating',
            'description': 'Role-based permissions are not being applied immediately after admin changes.',
            'status': 'In Progress',
            'priority': 'High',
            'assignee': 'Amanda White',
            'date': (datetime.now() - timedelta(days=9)).strftime('%Y-%m-%d')
        },
        {
            'title': 'Report generation taking too long',
            'description': 'Monthly reports are taking 10+ minutes to generate. Database query optimization needed.',
            'status': 'Open',
            'priority': 'Medium',
            'assignee': 'Robert Taylor',
            'date': (datetime.now() - timedelta(days=5)).strftime('%Y-%m-%d')
        }
    ]
    
    # Insert dummy data
    for issue in dummy_issues:
        c.execute("""
            INSERT INTO issues (title, description, status, priority, assignee, date) 
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            issue['title'],
            issue['description'],
            issue['status'],
            issue['priority'],
            issue['assignee'],
            issue['date']
        ))
    
    conn.commit()
    conn.close()
    print("Added 15 dummy records to the database!")

if __name__ == "__main__":
    add_dummy_data() 