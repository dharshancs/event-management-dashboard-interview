import sqlite3
from .database import create_database

def initialise():
    create_database()
    conn = sqlite3.connect("Event_management.db")
    cur = conn.cursor()

    admin_id = 1
    admin_name = "Dharshan"
    admin_email = "dharshanspn@gmail.com"
    admin_password = "admin"
    is_admin = True

    cur.execute(''' INSERT OR REPLACE INTO USERS(id,name,email,password,is_admin) VALUES(?,?,?,?,?);''',(admin_id,admin_name,admin_email,admin_password,is_admin))

    conn.commit()
    conn.close()    
