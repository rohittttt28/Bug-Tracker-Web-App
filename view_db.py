import sqlite3

def view_database():
    conn = sqlite3.connect('bug_tracker.db')
    cursor = conn.cursor()
    
    # Get table info
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("Tables in database:")
    for table in tables:
        print(f"  - {table[0]}")
    print()
    
    # View issues table
    cursor.execute("SELECT * FROM issues")
    issues = cursor.fetchall()
    
    if issues:
        print("Current issues in database:")
        print("-" * 80)
        for issue in issues:
            print(f"ID: {issue[0]}")
            print(f"Title: {issue[1]}")
            print(f"Description: {issue[2]}")
            print(f"Status: {issue[3]}")
            print(f"Priority: {issue[4]}")
            print(f"Assignee: {issue[5]}")
            print(f"Date: {issue[6]}")
            print("-" * 80)
    else:
        print("No issues found in database.")
    
    conn.close()

if __name__ == "__main__":
    view_database() 