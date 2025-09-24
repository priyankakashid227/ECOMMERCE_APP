# import os
# import sqlite3

# # Database path
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# DB_PATH = os.path.join(BASE_DIR, "instance", "ecommerce.db")

# # Connect to DB
# conn = sqlite3.connect(DB_PATH)
# cursor = conn.cursor()

# # Create Products table if not exists
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS Products (
#     ProductID INTEGER PRIMARY KEY AUTOINCREMENT,
#     Name TEXT NOT NULL,
#     Price REAL NOT NULL,
#     Stock INTEGER NOT NULL,
#     SellerID INTEGER NOT NULL,
#     FOREIGN KEY (SellerID) REFERENCES Users(UserID)
# )
# """)

# # Test Products (Name, Price, Stock, SellerID)
# products = [
#     ("Laptop", 55000, 10, 2),     # SellerID = 2 (seller1)
#     ("Smartphone", 20000, 15, 2),
#     ("Headphones", 1500, 25, 2),
#     ("Keyboard", 1200, 20, 2),
#     ("Monitor", 8000, 8, 2)
# ]

# # Insert products
# for p in products:
#     try:
#         cursor.execute("INSERT INTO Products (Name, Price, Stock, SellerID) VALUES (?, ?, ?, ?)", p)
#     except sqlite3.IntegrityError:
#         print(f"Product {p[0]} already exists, skipping...")

# conn.commit()
# conn.close()

# print("✅ Test products added successfully!")
import sqlite3
import os

DB_PATH = os.path.join("instance", "ecommerce.db")
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

products = [
    ("Laptop", 55000, 10, 2),
    ("Smartphone", 20000, 15, 2),
    ("Headphones", 1500, 25, 2),
    ("Keyboard", 1200, 20, 2),
    ("Monitor", 8000, 8, 2)
]

for name, price, stock, seller_id in products:
    try:
        cursor.execute(
            "INSERT INTO Products (Name, Price, Stock, SellerID) VALUES (?, ?, ?, ?)",
            (name, price, stock, seller_id)
        )
    except sqlite3.IntegrityError:
        continue

conn.commit()
conn.close()
print("Sample products added!")
