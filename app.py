# from flask import Flask
# from routes.users.users import auth_bp
# from routes.products.products import product_bp
# from routes.orders.orders import orders_bp
# import os
# import sqlite3

# app = Flask(__name__)
# app.secret_key = "your_secret_key"  # Required for session & flash messages

# # Register Blueprints
# app.register_blueprint(auth_bp)
# app.register_blueprint(product_bp)
# app.register_blueprint(orders_bp)

# # Database path inside instance folder
# DB_PATH = os.path.join("instance", "ecommerce.db")

# # Create instance folder if not exists
# if not os.path.exists("instance"):
#     os.makedirs("instance")

# # Create DB and tables if not exists
# if not os.path.exists(DB_PATH):
#     conn = sqlite3.connect(DB_PATH)
#     cursor = conn.cursor()

#     # Users table
#     cursor.execute("""
#     CREATE TABLE Users (
#         UserID INTEGER PRIMARY KEY AUTOINCREMENT,
#         Username TEXT UNIQUE,
#         Password TEXT,
#         Email TEXT,
#         Role TEXT CHECK(Role IN ('Customer','Seller','Admin'))
#     )
#     """)

#     # Products table
#     cursor.execute("""
#     CREATE TABLE Products (
#         ProductID INTEGER PRIMARY KEY AUTOINCREMENT,
#         Name TEXT,
#         Price REAL,
#         Stock INTEGER,
#         SellerID INTEGER,
#         FOREIGN KEY (SellerID) REFERENCES Users(UserID)
#     )
#     """)

#     # Orders table
#     cursor.execute("""
#     CREATE TABLE Orders (
#         OrderID INTEGER PRIMARY KEY AUTOINCREMENT,
#         UserID INTEGER,
#         ProductID INTEGER,
#         Quantity INTEGER,
#         OrderDate DATETIME,
#         FOREIGN KEY (UserID) REFERENCES Users(UserID),
#         FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
#     )
#     """)

#     conn.commit()
#     conn.close()
#     print("Database created successfully in instance/ecommerce.db")

# # Run Flask app
# if __name__ == "__main__":
#     app.run(debug=True)
# from flask import Flask
# from routes.users.users import auth_bp
# from routes.products.products import product_bp
# from routes.orders.orders import orders_bp
# import os
# import sqlite3

# app = Flask(__name__)
# app.secret_key = "your_secret_key"

# # Register Blueprints
# app.register_blueprint(auth_bp)
# app.register_blueprint(product_bp)
# app.register_blueprint(orders_bp)

# # Database path
# DB_PATH = os.path.join("instance", "ecommerce.db")

# if not os.path.exists("instance"):
#     os.makedirs("instance")

# if not os.path.exists(DB_PATH):
#     conn = sqlite3.connect(DB_PATH)
#     cursor = conn.cursor()

#     cursor.execute("""
#     CREATE TABLE Users (
#         UserID INTEGER PRIMARY KEY AUTOINCREMENT,
#         Username TEXT UNIQUE,
#         Password TEXT,
#         Email TEXT,
#         Role TEXT CHECK(Role IN ('Customer','Seller','Admin'))
#     )
#     """)

#     cursor.execute("""
#     CREATE TABLE Products (
#         ProductID INTEGER PRIMARY KEY AUTOINCREMENT,
#         Name TEXT,
#         Price REAL,
#         Stock INTEGER,
#         SellerID INTEGER,
#         FOREIGN KEY (SellerID) REFERENCES Users(UserID)
#     )
#     """)

#     cursor.execute("""
#     CREATE TABLE Orders (
#         OrderID INTEGER PRIMARY KEY AUTOINCREMENT,
#         UserID INTEGER,
#         ProductID INTEGER,
#         Quantity INTEGER,
#         OrderDate DATETIME,
#         FOREIGN KEY (UserID) REFERENCES Users(UserID),
#         FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
#     )
#     """)

#     conn.commit()
#     conn.close()
#     print("Database created successfully.")

# if __name__ == "__main__":
#     app.run(debug=True)

# from flask import Flask
# from routes.users.users import auth_bp
# from routes.products.products import product_bp
# from routes.orders.orders import orders_bp   # 👈 correct import
# import os

# app = Flask(__name__)
# app.secret_key = "supersecretkey"

#  # Register Blueprints
# app.register_blueprint(auth_bp)
# app.register_blueprint(product_bp)
# app.register_blueprint(orders_bp)   # 👈 correct register

# # Run the App
# if __name__ == "__main__":
#      app.run(debug=True)
# from flask import Flask
# from routes.users.users import auth_bp
# from routes.products.products import product_bp
# from routes.orders.orders import orders_bp  # orders_bp ka naam products.py aur orders.py ke hisaab se match hona chahiye
# import os

# app = Flask(__name__)
# app.secret_key = "supersecretkey"

# # # ---------------- Register Blueprints ----------------
# app.register_blueprint(auth_bp)
# app.register_blueprint(product_bp)
# app.register_blueprint(orders_bp)  # yahan orders_bp use karein

# # # ---------------- Run the App ----------------
# if __name__ == "__main__":
#      app.run(debug=True)
# app.py
import os
from flask import Flask

# ---------------- Flask App ----------------
app = Flask(__name__)
app.secret_key = "your_secret_key"  # Change this to a strong secret in production

# ---------------- Blueprints ----------------
from routes.users.users import auth_bp
from routes.products.products import product_bp
from routes.orders.orders import orders_bp

app.register_blueprint(auth_bp)
app.register_blueprint(product_bp)
app.register_blueprint(orders_bp)

# ---------------- Home Route ----------------
@app.route("/")
def home():
    return "Welcome to Mini E-Commerce App! <br> <a href='/login'>Login</a> | <a href='/register'>Register</a>"

# ---------------- Run App ----------------
if __name__ == "__main__":
    # Ensure instance folder exists
    if not os.path.exists("instance"):
        os.makedirs("instance")
    app.run(debug=True)
