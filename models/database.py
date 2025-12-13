import sqlite3

def create_database():
    conn = sqlite3.connect("Event_management.db")
    conn.execute("PRAGMA foreign_keys =ON")

    cur=conn.cursor()

    cur.execute('''
                CREATE TABLE IF NOT EXISTS USERS(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                role TEXT NOT NULL DEFAULT 'user'
                );
                ''')
    cur.execute('''
                CREATE TABLE IF NOT EXISTS EVENTS(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                date DATETIME,
                created_by INTEGER,
                FOREIGN KEY(created_by) REFERENCES USERS(id)
                );
                ''')
    cur.execute('''
                CREATE TABLE IF NOT EXISTS REGISTRATIONS(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                event_id INTEGER NOT NULL,
                FOREIGN KEY(user_id) REFERENCES USERS(id),
                FOREIGN KEY(event_id) REFERENCES EVENTS(id)
                );
                ''')
    conn.commit()
    conn.close()
    