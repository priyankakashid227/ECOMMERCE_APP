# ECOMMERCE_APP
Flask-based Mini E-Commerce Web Application with Customer, Seller, and Admin roles, using SQLite for database management.


# ECOMMERCE_APP
**Description:**  
Flask-based Mini E-Commerce Web Application supporting Customer, Seller, and Admin roles, with SQLite as the database. Users can browse products, place orders, and manage inventory efficiently.


### Customer
- Register / Login
- Browse products
- Place orders
- View order history

### Seller
- Login
- Add new products
- Update stock and price

### Admin
- Manage users
- Manage products
- View all orders

---
## Directory Structure
'''
ECOMMERCE_APP/
├── app.py
├── requirements.txt
├── ecommerce.db
├── routes/
│   ├── users/
│   │   └── users.py
│   ├── products/
│   │   └── products.py
│   └── orders/
│       └── orders.py
├── templates/
│   ├── users/
│   │   ├── register.html
│   │   ├── login.html
│   │   └── dashboard.html
│   ├── products/
│   │   └── products.html
│   └── orders/
│       └── orders.html
└── static/
    ├── css/
    └── js/

'''  



---

## Database

**Database Used:** SQLite (`ecommerce.db`)

**Tables:**

### Users
- UserID, Username, Password, Email, Role (Customer/Seller/Admin)

### Products
- ProductID, Name, Price, Stock, SellerID

### Orders
- OrderID, UserID, ProductID, Quantity, OrderDate

---

## How to Run

1. Clone the repository:
```bash
git clone https://github.com/priyankakashid227/ECOMMERCE_APP.git

