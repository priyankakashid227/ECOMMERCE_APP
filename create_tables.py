import sqlite3
import os

DB_PATH = os.path.join("instance", "ecommerce.db")

# Ensure instance folder exists
if not os.path.exists("instance"):
    os.makedirs("instance")

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

# -------- Users Table --------
cur.execute("""
CREATE TABLE IF NOT EXISTS Users (
    UserID INTEGER PRIMARY KEY AUTOINCREMENT,
    Username TEXT UNIQUE,
    Password TEXT,
    Email TEXT,
    Role TEXT CHECK(Role IN ('Customer','Seller','Admin'))
)
""")

# -------- Products Table --------
cur.execute("""
CREATE TABLE IF NOT EXISTS Products (
    ProductID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT,
    Price REAL,
    Stock INTEGER,
    SellerID INTEGER,
    FOREIGN KEY(SellerID) REFERENCES Users(UserID)
)
""")

# -------- Orders Table --------
cur.execute("""
CREATE TABLE IF NOT EXISTS Orders (
    OrderID INTEGER PRIMARY KEY AUTOINCREMENT,
    UserID INTEGER,
    ProductID INTEGER,
    Quantity INTEGER,
    OrderDate DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(UserID) REFERENCES Users(UserID),
    FOREIGN KEY(ProductID) REFERENCES Products(ProductID)
)
""")

conn.commit()
conn.close()
print("Tables created successfully!")
