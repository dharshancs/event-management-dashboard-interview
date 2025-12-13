import sqlite3

def connect_database():
    conn = sqlite3.connect("Event_management.db")
    conn.row_factory = sqlite3.Row #converts tuples into rows 
    
    return conn
