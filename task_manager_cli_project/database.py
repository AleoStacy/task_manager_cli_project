import sqlite3

def connect():
    return sqlite3.connect("task_manager.db")

def initialize_db():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            due_date TEXT,
            priority INTEGER,
            status TEXT DEFAULT 'Incomplete'
        )
    ''')
    conn.commit()
    conn.close()
