from database import connect

def add_task(title, description, due_date, priority):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO tasks (title, description, due_date, priority)
        VALUES (?, ?, ?, ?)
    ''', (title, description, due_date, priority))
    conn.commit()
    conn.close()
