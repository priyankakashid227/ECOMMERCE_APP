# import sqlite3, os
# from flask import Blueprint, render_template, request, redirect, url_for, flash, session

# product_bp = Blueprint(
#     "products",
#     __name__,
#     template_folder=os.path.join(os.getcwd(), "templates/products")
# )

# DB_PATH = os.path.join("instance", "ecommerce.db")

# def get_db_connection():
#     conn = sqlite3.connect(DB_PATH)
#     conn.row_factory = sqlite3.Row
#     return conn

# # ---------------- View Products (Customer & Seller) ----------------
# @product_bp.route("/products")
# def view_products():
#     if "user_id" not in session:
#         flash("Please login first.","warning")
#         return redirect(url_for("auth.login"))

#     conn = get_db_connection()
#     cur = conn.cursor()
#     cur.execute("""
#         SELECT p.ProductID, p.Name, p.Price, p.Stock, p.SellerID, u.Username as SellerName
#         FROM Products p
#         LEFT JOIN Users u ON p.SellerID = u.UserID
#     """)
#     products = cur.fetchall()
#     conn.close()
#     return render_template("products.html", products=products, username=session["username"], role=session["role"])

# # ---------------- Add Product (Seller) ----------------
# @product_bp.route("/add_product", methods=["GET","POST"])
# def add_product():
#     if "user_id" not in session or session.get("role") != "Seller":
#         flash("Access denied.","danger")
#         return redirect(url_for("auth.login"))
#     if request.method=="POST":
#         name = request.form["name"].strip()
#         price = float(request.form["price"])
#         stock = int(request.form["stock"])
#         seller_id = session["user_id"]
#         conn = get_db_connection()
#         cur = conn.cursor()
#         cur.execute(
#             "INSERT INTO Products (Name, Price, Stock, SellerID) VALUES (?, ?, ?, ?)",
#             (name, price, stock, seller_id)
#         )
#         conn.commit()
#         conn.close()
#         flash("Product added successfully!","success")
#         return redirect(url_for("products.view_products"))
#     return render_template("add_products.html")
# import sqlite3
# import os
# from flask import Blueprint, render_template, request, redirect, url_for, flash, session

# # ---------- Blueprint ----------
# product_bp = Blueprint(
#     "products",
#     __name__,
#     template_folder=os.path.join(os.getcwd(), "templates/products")  # template path
# )

# DB_PATH = os.path.join("instance", "ecommerce.db")

# # ---------- Database Connection ----------
# def get_db_connection():
#     conn = sqlite3.connect(DB_PATH)
#     conn.row_factory = sqlite3.Row
#     return conn

# # ---------------- View Products ----------------
# @product_bp.route("/products")
# def view_products():
#     if "user_id" not in session:
#         flash("Please login first.", "warning")
#         return redirect(url_for("auth.login"))

#     conn = get_db_connection()
#     cur = conn.cursor()
#     cur.execute("""
#         SELECT p.ProductID, p.Name, p.Price, p.Stock, p.SellerID, u.Username as SellerName
#         FROM Products p
#         LEFT JOIN Users u ON p.SellerID = u.UserID
#     """)
#     products = cur.fetchall()
#     conn.close()
#     return render_template(
#         "products.html",
#         products=products,
#         username=session.get("username"),
#         role=session.get("role")
#     )

# # ---------------- Add Product ----------------
# @product_bp.route("/add_product", methods=["GET", "POST"])
# def add_product():
#     if "user_id" not in session or session.get("role") != "Seller":
#         flash("Access denied. Only sellers can add products.", "danger")
#         return redirect(url_for("auth.login"))

#     if request.method == "POST":
#         try:
#             name = request.form.get("name").strip()
#             price = float(request.form.get("price"))
#             stock = int(request.form.get("stock"))
#             seller_id = session["user_id"]

#             conn = get_db_connection()
#             cur = conn.cursor()
#             cur.execute(
#                 "INSERT INTO Products (Name, Price, Stock, SellerID) VALUES (?, ?, ?, ?)",
#                 (name, price, stock, seller_id)
#             )
#             conn.commit()
#             conn.close()

#             flash("Product added successfully!", "success")
#             return redirect(url_for("products.view_products"))

#         except Exception as e:
#             flash(f"Error adding product: {e}", "danger")
#             return redirect(url_for("products.add_product"))

#     return render_template("add_products.html")

# import sqlite3, os
# from flask import Blueprint, render_template, request, redirect, url_for, flash, session

# # ---------- Blueprint ----------
# product_bp = Blueprint(
#     "products",
#     __name__,
#     template_folder=os.path.join(os.getcwd(), "templates/products")
# )

# DB_PATH = os.path.join("instance", "ecommerce.db")

# # ---------- Database Connection ----------
# def get_db_connection():
#     conn = sqlite3.connect(DB_PATH)
#     conn.row_factory = sqlite3.Row
#     return conn

# # ---------------- View Products (Customer & Seller) ----------------
# @product_bp.route("/products")
# def view_products():
#     if "user_id" not in session:
#         flash("Please login first.", "warning")
#         return redirect(url_for("auth.login"))

#     conn = get_db_connection()
#     cur = conn.cursor()
#     cur.execute("""
#         SELECT p.ProductID, p.Name, p.Price, p.Stock, p.SellerID, u.Username as SellerName
#         FROM Products p
#         LEFT JOIN Users u ON p.SellerID = u.UserID
#     """)
#     products = cur.fetchall()
#     conn.close()

#     return render_template(
#         "products.html",
#         products=products,
#         username=session.get("username"),
#         role=session.get("role")
#     )

# # ---------------- Add Product (Seller Only) ----------------
# @product_bp.route("/add_product", methods=["GET", "POST"])
# def add_product():
#     if "user_id" not in session or session.get("role") != "Seller":
#         flash("Access denied.", "danger")
#         return redirect(url_for("auth.login"))

#     if request.method == "POST":
#         name = request.form["name"].strip()
#         price = request.form.get("price", 0)
#         stock = request.form.get("stock", 0)

#         try:
#             price = float(price)
#             stock = int(stock)
#         except ValueError:
#             flash("Invalid price or stock value.", "danger")
#             return redirect(url_for("products.add_product"))

#         seller_id = session["user_id"]
#         conn = get_db_connection()
#         cur = conn.cursor()
#         cur.execute(
#             "INSERT INTO Products (Name, Price, Stock, SellerID) VALUES (?, ?, ?, ?)",
#             (name, price, stock, seller_id)
#         )
#         conn.commit()
#         conn.close()

#         flash("Product added successfully!", "success")
#         return redirect(url_for("products.view_products"))

#     return render_template("add_products.html")
# import sqlite3
# from flask import Blueprint, render_template, request, redirect, url_for, flash, session

# # Blueprint with relative template folder
# product_bp = Blueprint(
#     "products",
#     __name__,
#     template_folder="products"  # relative to templates/
# )

# DB_PATH = "instance/ecommerce.db"

# # ---------- Helper Function ----------
# def get_db_connection():
#     conn = sqlite3.connect(DB_PATH)
#     conn.row_factory = sqlite3.Row
#     return conn

# # ---------------- View Products ----------------
# @product_bp.route("/products")
# def view_products():
#     if "user_id" not in session:
#         flash("Please login first.", "warning")
#         return redirect(url_for("auth.login"))

#     conn = get_db_connection()
#     cur = conn.cursor()
#     cur.execute("""
#         SELECT p.ProductID, p.Name, p.Price, p.Stock, p.SellerID, u.Username as SellerName
#         FROM Products p
#         LEFT JOIN Users u ON p.SellerID = u.UserID
#     """)
#     products = cur.fetchall()
#     conn.close()
#     return render_template("products.html", products=products, username=session["username"], role=session["role"])

# # ---------------- Add Product ----------------
# @product_bp.route("/add_product", methods=["GET", "POST"])
# def add_product():
#     if "user_id" not in session or session.get("role") != "Seller":
#         flash("Access denied.", "danger")
#         return redirect(url_for("auth.login"))

#     if request.method == "POST":
#         name = request.form["name"].strip()
#         price = float(request.form["price"])
#         stock = int(request.form["stock"])
#         seller_id = session["user_id"]

#         conn = get_db_connection()
#         cur = conn.cursor()
#         cur.execute(
#             "INSERT INTO Products (Name, Price, Stock, SellerID) VALUES (?, ?, ?, ?)",
#             (name, price, stock, seller_id)
#         )
#         conn.commit()
#         conn.close()

#         flash("Product added successfully!", "success")
#         return redirect(url_for("products.view_products"))

#     # Render add_products.html from templates/products/
#     return render_template("add_products.html")
# import sqlite3, os
# from flask import Blueprint, render_template, request, redirect, url_for, flash, session

# # ---------------- Blueprint ----------------
# product_bp = Blueprint(
#     "products",
#     __name__,
#     template_folder=os.path.join(os.getcwd(), "templates")
# )

# DB_PATH = os.path.join("instance", "ecommerce.db")

# # ---------------- Helper ----------------
# def get_db_connection():
#     conn = sqlite3.connect(DB_PATH)
#     conn.row_factory = sqlite3.Row
#     return conn

# # ---------------- View Products (Customer & Seller) ----------------
# @product_bp.route("/products")
# def view_products():
#     if "user_id" not in session:
#         flash("Please login first.","warning")
#         return redirect(url_for("auth.login"))

#     conn = get_db_connection()
#     cur = conn.cursor()
#     cur.execute("""
#         SELECT p.ProductID, p.Name, p.Price, p.Stock, p.SellerID, u.Username as SellerName
#         FROM Products p
#         LEFT JOIN Users u ON p.SellerID = u.UserID
#     """)
#     products = cur.fetchall()
#     conn.close()
    
#     return render_template(
#         "products/products.html",
#         products=products,
#         username=session["username"],
#         role=session["role"]
#     )

# # ---------------- Add Product (Seller) ----------------
# @product_bp.route("/add_product", methods=["GET","POST"])
# def add_product():
#     if "user_id" not in session or session.get("role") != "Seller":
#         flash("Access denied.","danger")
#         return redirect(url_for("auth.login"))
    
#     if request.method == "POST":
#         name = request.form["name"].strip()
#         price = float(request.form["price"])
#         stock = int(request.form["stock"])
#         seller_id = session["user_id"]

#         conn = get_db_connection()
#         cur = conn.cursor()
#         cur.execute(
#             "INSERT INTO Products (Name, Price, Stock, SellerID) VALUES (?, ?, ?, ?)",
#             (name, price, stock, seller_id)
#         )
#         conn.commit()
#         conn.close()
#         flash("Product added successfully!","success")
#         return redirect(url_for("products.view_products"))
    
#     # Correct template path
#     return render_template("products/add_products.html")
# import sqlite3, os
# from flask import Blueprint, render_template, request, redirect, url_for, flash, session

# # ---------------- Blueprint ----------------
# # template_folder sirf "templates" rakha hai
# product_bp = Blueprint(
#     "products",
#     __name__,
#     template_folder=os.path.join(os.getcwd(), "templates")
# )

# # ---------------- Database Path ----------------
# DB_PATH = os.path.join("instance", "ecommerce.db")

# def get_db_connection():
#     conn = sqlite3.connect(DB_PATH)
#     conn.row_factory = sqlite3.Row
#     return conn

# # ---------------- View Products (Customer & Seller) ----------------
# @product_bp.route("/products")
# def view_products():
#     if "user_id" not in session:
#         flash("Please login first.", "warning")
#         return redirect(url_for("auth.login"))

#     conn = get_db_connection()
#     cur = conn.cursor()
#     cur.execute("""
#         SELECT p.ProductID, p.Name, p.Price, p.Stock, p.SellerID, u.Username as SellerName
#         FROM Products p
#         LEFT JOIN Users u ON p.SellerID = u.UserID
#     """)
#     products = cur.fetchall()
#     conn.close()
    
#     return render_template(
#         "products/products.html",
#         products=products,
#         username=session["username"],
#         role=session["role"]
#     )

# # ---------------- Add Product (Seller) ----------------
# @product_bp.route("/add_product", methods=["GET", "POST"])
# def add_product():
#     if "user_id" not in session or session.get("role") != "Seller":
#         flash("Access denied.", "danger")
#         return redirect(url_for("auth.login"))

#     if request.method == "POST":
#         name = request.form["name"].strip()
#         price = float(request.form["price"])
#         stock = int(request.form["stock"])
#         seller_id = session["user_id"]

#         conn = get_db_connection()
#         cur = conn.cursor()
#         cur.execute(
#             "INSERT INTO Products (Name, Price, Stock, SellerID) VALUES (?, ?, ?, ?)",
#             (name, price, stock, seller_id)
#         )
#         conn.commit()
#         conn.close()

#         flash("Product added successfully!", "success")
#         return redirect(url_for("products.view_products"))

#     return render_template("products/add_products.html")
# import sqlite3, os
# from flask import Blueprint, render_template, request, redirect, url_for, flash, session

# # ---------------- Blueprint ----------------
# # template_folder "templates" rakhenge, Flask automatically 'templates/' root se dhundhta hai
# product_bp = Blueprint(
#     "products",
#     __name__,
#     template_folder="templates"
# )

# # ---------------- Database Path ----------------
# DB_PATH = os.path.join("instance", "ecommerce.db")

# def get_db_connection():
#     conn = sqlite3.connect(DB_PATH)
#     conn.row_factory = sqlite3.Row
#     return conn

# # ---------------- View Products ----------------
# @product_bp.route("/products")
# def view_products():
#     if "user_id" not in session:
#         flash("Please login first.", "warning")
#         return redirect(url_for("auth.login"))

#     conn = get_db_connection()
#     cur = conn.cursor()
#     cur.execute("""
#         SELECT p.ProductID, p.Name, p.Price, p.Stock, p.SellerID, u.Username as SellerName
#         FROM Products p
#         LEFT JOIN Users u ON p.SellerID = u.UserID
#     """)
#     products = cur.fetchall()
#     conn.close()
    
#     return render_template(
#         "products/products.html",
#         products=products,
#         username=session["username"],
#         role=session["role"]
#     )

# # ---------------- Add Product ----------------
# @product_bp.route("/add_product", methods=["GET", "POST"])
# def add_product():
#     if "user_id" not in session or session.get("role") != "Seller":
#         flash("Access denied.", "danger")
#         return redirect(url_for("auth.login"))

#     if request.method == "POST":
#         name = request.form["name"].strip()
#         price = float(request.form["price"])
#         stock = int(request.form["stock"])
#         seller_id = session["user_id"]

#         conn = get_db_connection()
#         cur = conn.cursor()
#         cur.execute(
#             "INSERT INTO Products (Name, Price, Stock, SellerID) VALUES (?, ?, ?, ?)",
#             (name, price, stock, seller_id)
#         )
#         conn.commit()
#         conn.close()

#         flash("Product added successfully!", "success")
#         return redirect(url_for("products.view_products"))

#     return render_template("products/add_product.html")
# import sqlite3, os
# from flask import Blueprint, render_template, request, redirect, url_for, flash, session

# # ---------------- Blueprint ----------------
# product_bp = Blueprint(
#     "products",
#     __name__,
#     template_folder="templates"
# )

# # ---------------- Database Path ----------------
# DB_PATH = os.path.join("instance", "ecommerce.db")

# def get_db_connection():
#     conn = sqlite3.connect(DB_PATH)
#     conn.row_factory = sqlite3.Row
#     return conn

# # ---------------- View Products ----------------
# @product_bp.route("/products")
# def view_products():
#     if "user_id" not in session:
#         flash("Please login first.", "warning")
#         return redirect(url_for("auth.login"))

#     conn = get_db_connection()
#     cur = conn.cursor()
#     cur.execute("""
#         SELECT p.ProductID, p.Name, p.Price, p.Stock, p.SellerID, u.Username as SellerName
#         FROM Products p
#         LEFT JOIN Users u ON p.SellerID = u.UserID
#     """)
#     products = cur.fetchall()
#     conn.close()
    
#     return render_template(
#         "products/products.html",
#         products=products,
#         username=session["username"],
#         role=session["role"]
#     )

# # ---------------- Add Product ----------------
# @product_bp.route("/add_product", methods=["GET", "POST"])
# def add_product():
#     if "user_id" not in session or session.get("role") != "Seller":
#         flash("Access denied.", "danger")
#         return redirect(url_for("auth.login"))

#     product = None
#     if request.method == "POST":
#         name = request.form["name"].strip()
#         price = float(request.form["price"])
#         stock = int(request.form["stock"])
#         seller_id = session["user_id"]

#         if request.form.get("product_id"):  # Update product
#             product_id = int(request.form["product_id"])
#             conn = get_db_connection()
#             cur = conn.cursor()
#             cur.execute(
#                 "UPDATE Products SET Name = ?, Price = ?, Stock = ? WHERE ProductID = ?",
#                 (name, price, stock, product_id)
#             )
#             conn.commit()
#             conn.close()
#             flash("Product updated successfully!", "success")
#         else:  # Add new product
#             conn = get_db_connection()
#             cur = conn.cursor()
#             cur.execute(
#                 "INSERT INTO Products (Name, Price, Stock, SellerID) VALUES (?, ?, ?, ?)",
#                 (name, price, stock, seller_id)
#             )
#             conn.commit()
#             conn.close()
#             flash("Product added successfully!", "success")

#         return redirect(url_for("products.view_products"))

#     # If GET request with product_id (for editing)
#     product_id = request.args.get("product_id")
#     if product_id:
#         conn = get_db_connection()
#         cur = conn.cursor()
#         cur.execute("SELECT * FROM Products WHERE ProductID = ?", (product_id,))
#         product = cur.fetchone()
#         conn.close()

#     return render_template("products/add_product.html", product=product)

# # ---------------- Delete Product ----------------
# @product_bp.route("/delete_product/<int:product_id>")
# def delete_product(product_id):
#     if "user_id" not in session or session.get("role") != "Seller":
#         flash("Access denied.", "danger")
#         return redirect(url_for("auth.login"))

#     conn = get_db_connection()
#     cur = conn.cursor()
#     cur.execute("DELETE FROM Products WHERE ProductID = ?", (product_id,))
#     conn.commit()
#     conn.close()
#     flash("Product deleted successfully!", "success")
#     return redirect(url_for("products.view_products"))

import sqlite3, os
from flask import Blueprint, render_template, request, redirect, url_for, flash, session

product_bp = Blueprint("products", __name__, template_folder="templates")

DB_PATH = os.path.join("instance", "ecommerce.db")

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

# ---------------- View Products ----------------
@product_bp.route("/products")
def view_products():
    if "user_id" not in session:
        flash("Please login first.", "warning")
        return redirect(url_for("auth.login"))

    conn = get_db_connection()
    cur = conn.cursor()

    if session.get("role") == "Seller":
        # Seller sees only their own products
        cur.execute("""
            SELECT p.ProductID, p.Name, p.Price, p.Stock, p.SellerID, u.Username as SellerName
            FROM Products p
            LEFT JOIN Users u ON p.SellerID = u.UserID
            WHERE p.SellerID = ?
        """, (session["user_id"],))
    else:
        # Admin or Customer sees all products
        cur.execute("""
            SELECT p.ProductID, p.Name, p.Price, p.Stock, p.SellerID, u.Username as SellerName
            FROM Products p
            LEFT JOIN Users u ON p.SellerID = u.UserID
        """)

    products = cur.fetchall()
    conn.close()

    return render_template("products/products.html",
                           products=products,
                           username=session["username"],
                           role=session["role"])

# ---------------- Add / Update Product ----------------
@product_bp.route("/add_product", methods=["GET", "POST"])
def add_product():
    if "user_id" not in session or session.get("role") != "Seller":
        flash("Access denied.", "danger")
        return redirect(url_for("auth.login"))

    product = None
    if request.method == "POST":
        name = request.form["name"].strip()
        price = float(request.form["price"])
        stock = int(request.form["stock"])
        seller_id = session["user_id"]

        if request.form.get("product_id"):  # Update
            product_id = int(request.form["product_id"])
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute(
                "UPDATE Products SET Name=?, Price=?, Stock=? WHERE ProductID=? AND SellerID=?",
                (name, price, stock, product_id, seller_id)
            )
            conn.commit()
            conn.close()
            flash("Product updated successfully!", "success")
        else:  # Add new
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO Products (Name, Price, Stock, SellerID) VALUES (?, ?, ?, ?)",
                (name, price, stock, seller_id)
            )
            conn.commit()
            conn.close()
            flash("Product added successfully!", "success")

        return redirect(url_for("products.view_products"))

    # GET request with product_id (for editing)
    product_id = request.args.get("product_id")
    if product_id:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM Products WHERE ProductID=? AND SellerID=?", (product_id, session["user_id"]))
        product = cur.fetchone()
        conn.close()

    return render_template("products/add_product.html", product=product)

# ---------------- Delete Product ----------------
@product_bp.route("/delete_product/<int:product_id>", methods=["POST"])
def delete_product(product_id):
    if "user_id" not in session or session.get("role") != "Seller":
        flash("Access denied.", "danger")
        return redirect(url_for("auth.login"))

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM Products WHERE ProductID=? AND SellerID=?", (product_id, session["user_id"]))
    conn.commit()
    conn.close()
    flash("Product deleted successfully!", "success")
    return redirect(url_for("products.view_products"))
