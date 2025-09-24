import sqlite3
import os
from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from datetime import datetime

# ---------- Blueprint ----------
orders_bp = Blueprint(
    "orders",
    __name__,
    template_folder=os.path.join(os.getcwd(), "templates/orders")
)

DB_PATH = os.path.join("instance", "ecommerce.db")

# ---------- Helper ----------
def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

# ---------------- Place Order Route ----------------
@orders_bp.route("/place_order/<int:product_id>", methods=["GET", "POST"])
def place_order(product_id):
    if "user_id" not in session or session["role"] != "Customer":
        flash("Only customers can place orders!", "warning")
        return redirect(url_for("auth.login"))

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Products WHERE ProductID=?", (product_id,))
    product = cur.fetchone()

    if not product:
        flash("Product not found!", "danger")
        conn.close()
        return redirect(url_for("products.view_products"))

    if request.method == "POST":
        qty = int(request.form.get("quantity", 1))
        if qty <= 0 or qty > product["Stock"]:
            flash("Invalid quantity!", "danger")
            return redirect(url_for("orders.place_order", product_id=product_id))

        # Insert order
        cur.execute(
            "INSERT INTO Orders (UserID, ProductID, Quantity, OrderDate) VALUES (?, ?, ?, ?)",
            (session["user_id"], product_id, qty, datetime.now())
        )
        # Update stock
        new_stock = product["Stock"] - qty
        cur.execute("UPDATE Products SET Stock=? WHERE ProductID=?", (new_stock, product_id))
        conn.commit()
        conn.close()
        flash("Order placed successfully!", "success")
        return redirect(url_for("orders.view_orders"))

    conn.close()
    return render_template("place_order.html", product=product)

# ---------------- View Orders / Order History ----------------
@orders_bp.route("/orders")
def view_orders():
    if "user_id" not in session:
        flash("Please login first.", "warning")
        return redirect(url_for("auth.login"))

    conn = get_db_connection()
    cur = conn.cursor()

    if session["role"] == "Customer":
        cur.execute("""
            SELECT Orders.OrderID, Products.Name as ProductName, Products.Price, Orders.Quantity, Orders.OrderDate
            FROM Orders
            JOIN Products ON Orders.ProductID = Products.ProductID
            WHERE Orders.UserID=?
            ORDER BY Orders.OrderDate DESC
        """, (session["user_id"],))
    elif session["role"] == "Seller":
        cur.execute("""
            SELECT Orders.OrderID, Products.Name as ProductName, Products.Price, Orders.Quantity, Orders.OrderDate
            FROM Orders
            JOIN Products ON Orders.ProductID = Products.ProductID
            WHERE Products.SellerID=?
            ORDER BY Orders.OrderDate DESC
        """, (session["user_id"],))
    elif session["role"] == "Admin":
        cur.execute("""
            SELECT Orders.OrderID, Products.Name as ProductName, Products.Price, Orders.Quantity, Orders.OrderDate
            FROM Orders
            JOIN Products ON Orders.ProductID = Products.ProductID
            ORDER BY Orders.OrderDate DESC
        """)

    orders = cur.fetchall()
    conn.close()
    return render_template("orders.html", orders=orders)
