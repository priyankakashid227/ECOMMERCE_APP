import sqlite3
from werkzeug.security import generate_password_hash
import os

DB_PATH = os.path.join("instance", "ecommerce.db")
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

users = [
    ("priyanka", "12345", "priyanka@email.com", "Customer"),
    ("radha", "12345", "radha@email.com", "Seller"),
    ("admin", "admin123", "admin@email.com", "Admin")
]

for username, pwd, email, role in users:
    hashed = generate_password_hash(pwd)
    try:
        cursor.execute(
            "INSERT INTO Users (Username, Password, Email, Role) VALUES (?, ?, ?, ?)",
            (username, hashed, email, role)
        )
    except sqlite3.IntegrityError:
        continue

conn.commit()
conn.close()
print("Test users added!")
