import sqlite3
import os

DB_PATH = os.path.join("instance", "ecommerce.db")
conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

# Check if admin exists
cur.execute("SELECT * FROM Users WHERE Username=?", ("admin",))
if cur.fetchone() is None:
    cur.execute("""
    INSERT INTO Users (Username, Password, Email, Role)
    VALUES (?, ?, ?, ?)
    """, ("admin", "admin123", "admin@example.com", "Admin"))
    conn.commit()
    print("Admin user added successfully!")
else:
    print("Admin user already exists!")

conn.close()
