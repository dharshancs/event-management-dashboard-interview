import sqlite3
from .database import create_database
from werkzeug.security import generate_password_hash

def initialise():
    create_database()
    conn = sqlite3.connect("Event_management.db")
    cur = conn.cursor()

    admin_id = 1
    admin_name = "Dharshan"
    admin_email = "dharshanspn@gmail.com"
    admin_password = generate_password_hash("admin")
    role = "organiser"

    cur.execute(''' INSERT OR REPLACE INTO USERS(id,name,email,password,role) VALUES(?,?,?,?,?);''',(admin_id,admin_name,admin_email,admin_password,role))

    conn.commit()
    conn.close()    
