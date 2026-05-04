import mysql.connector
from tkinter import messagebox

def connect_db():
    try:
        # Changed port to 3306 for MySQL Workbench
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Bilalband1.", # Enter the password you set in Workbench
            database="smart_udhaar",
            port=3306 
        )
        return conn
    except Exception as e:
        messagebox.showerror("Database Error", f"Cannot connect to database: {e}")
        return None