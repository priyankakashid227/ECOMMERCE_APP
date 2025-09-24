import sqlite3, os
from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash

# ---------------- Blueprint ----------------
auth_bp = Blueprint(
    "auth",
    __name__,
    template_folder=os.path.join(os.getcwd(), "templates/users")
)

# ---------------- Database Path ----------------
DB_PATH = os.path.join("instance", "ecommerce.db")

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

# ---------------- Register ----------------
@auth_bp.route("/register", methods=["GET","POST"])
def register():
    if request.method=="POST":
        username = request.form["username"].strip()
        email = request.form["email"].strip()
        password = request.form["password"].strip()
        role = request.form["role"].strip()
        if not username or not email or not password or not role:
            flash("All fields are required!","danger")
            return redirect(url_for("auth.register"))
        hashed = generate_password_hash(password)
        conn = get_db_connection()
        cur = conn.cursor()
        try:
            cur.execute(
                "INSERT INTO Users (Username, Password, Email, Role) VALUES (?,?,?,?)",
                (username, hashed, email, role)
            )
            conn.commit()
            flash("Registration successful! Please login.","success")
            return redirect(url_for("auth.login"))
        except sqlite3.IntegrityError:
            flash("Username already exists!","danger")
            return redirect(url_for("auth.register"))
        finally:
            conn.close()
    return render_template("register.html")

# ---------------- Login ----------------
@auth_bp.route("/login", methods=["GET","POST"])
def login():
    if request.method=="POST":
        username = request.form["username"].strip()
        password = request.form["password"].strip()
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM Users WHERE Username=?",(username,))
        user = cur.fetchone()
        conn.close()
        if user and check_password_hash(user["Password"],password):
            session["user_id"] = user["UserID"]
            session["username"] = user["Username"]
            session["role"] = user["Role"]
            flash(f"Welcome {user['Username']}!","success")
            return redirect(url_for("auth.dashboard"))
        else:
            flash("Invalid credentials.","danger")
            return redirect(url_for("auth.login"))
    return render_template("login.html")

# ---------------- Dashboard ----------------
@auth_bp.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        flash("Please login first.","warning")
        return redirect(url_for("auth.login"))
    return render_template(
        "dashboard.html",
        username=session["username"],
        role=session["role"]
    )

# ---------------- Logout ----------------
@auth_bp.route("/logout")
def logout():
    session.clear()
    flash("Logged out successfully.","success")
    return redirect(url_for("auth.login"))

# ---------------- Manage Users (Admin Only) ----------------
@auth_bp.route("/manage_users")
def manage_users():
    if "user_id" not in session or session.get("role") != "Admin":
        flash("Access denied.","danger")
        return redirect(url_for("auth.login"))
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT UserID, Username, Email, Role FROM Users")
    users = cur.fetchall()
    conn.close()
    return render_template("manage_users.html", users=users)
