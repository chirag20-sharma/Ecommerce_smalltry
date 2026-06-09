# 🛍️ ShopEasy — Django Ecommerce Project

A fully functional ecommerce web application built with Django and MySQL. This project was originally started in 2025 and has been completely revamped with new features including user authentication, a database-driven cart, order management, delivery address collection, and CSV product importing.

> 🔗 GitHub: [https://github.com/chirag20-sharma/Ecommerce_smalltry](https://github.com/chirag20-sharma/Ecommerce_smalltry)

---

## ✨ Features

### 🛒 Shopping
- Product listing with grid layout and product cards
- Product images (upload or URL-based)
- Stock availability display (In Stock / Out of Stock)
- Product category badges

### 🔍 Filter & Search
- Search products by name
- Filter by category (Electronics, Clothing, Accessories, Footwear, Kitchen, etc.)
- Filter by price range (min / max)
- Sort by price (low to high, high to low) or name (A-Z)

### 🔐 Authentication
- User registration with email
- Login / Logout
- Protected routes (cart, checkout, orders require login)

### 🛒 Cart
- Add / remove / update product quantity
- Per-user cart stored in database (not session)
- Real-time subtotal and total calculation

### 📦 Checkout & Orders
- Full delivery address form (name, phone, address, city, state, pincode)
- All Indian states included in dropdown
- Cash on Delivery payment method
- Order confirmation page after placing order
- Order history with delivery address and status tracking

### ⚙️ Admin
- Full Django admin panel at `/admin/`
- Add, edit, delete products directly
- View and manage all orders

### 📥 Product Import
- Import products from CSV file
- Fetch 20 real products from Fake Store API automatically
- Variants (size/color) grouped into single product with combined stock

---

## 🗂️ Project Structure

```
ecommerce_project/
├── ecommerce_project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── store/
│   ├── management/
│   │   └── commands/
│   │       ├── fetch_products.py    # Fetch from Fake Store API
│   │       └── import_csv.py        # Import from CSV file
│   ├── migrations/
│   ├── static/store/
│   │   └── style.css
│   ├── templates/store/
│   │   ├── base.html
│   │   ├── product_list.html
│   │   ├── cart.html
│   │   ├── checkout.html
│   │   ├── order_confirm.html
│   │   ├── orders.html
│   │   ├── login.html
│   │   └── register.html
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
├── products.csv
├── requirements.txt
├── .env                # Not pushed to GitHub (secrets)
├── .gitignore
└── manage.py
```

---

## 🧰 Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django 6.0.6 |
| Database | MySQL |
| Frontend | HTML, CSS (custom) |
| Static Files | WhiteNoise |
| Image Handling | Pillow |
| Environment | python-dotenv |
| Product Data | Fake Store API / CSV Import |

---

## 🚀 Local Setup

### 1. Clone the repo
```bash
git clone https://github.com/chirag20-sharma/Ecommerce_smalltry.git
cd Ecommerce_smalltry
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Create `.env` file in the project root
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

DB_NAME=ecommerce_db
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_HOST=localhost
DB_PORT=3306
```

### 4. Create MySQL database
```sql
CREATE DATABASE ecommerce_db;
```

### 5. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create admin user
```bash
python manage.py createsuperuser
```

### 7. Import products
```bash
# Option A - Import from CSV
python manage.py import_csv products.csv

# Option B - Fetch from Fake Store API (20 products)
python manage.py fetch_products
```

### 8. Run the server
```bash
python manage.py runserver
```

Visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)
Admin: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

---

## 📸 Pages

| URL | Page |
|---|---|
| `/` | Product listing with filters |
| `/cart/` | Shopping cart |
| `/checkout/` | Delivery address + COD |
| `/orders/` | Order history |
| `/login/` | Login |
| `/register/` | Register |
| `/admin/` | Django admin panel |

---

## 🔄 What Changed from 2025 Version

- ✅ Replaced session-based cart with database-driven cart
- ✅ Added full user authentication (register, login, logout)
- ✅ Added Order model with delivery address fields
- ✅ Added Cash on Delivery checkout flow
- ✅ Added order confirmation and order history pages
- ✅ Added product filters (category, price range, search, sort)
- ✅ Added CSV product importer and Fake Store API command
- ✅ Added `image_url` field to support URL-based product images
- ✅ Moved all secrets to `.env` file
- ✅ Added WhiteNoise for static file serving in production
- ✅ Added `.gitignore` to protect sensitive files
- ✅ Switched timezone to Asia/Kolkata (IST)

---

## ⚠️ Important Notes

- Never push your `.env` file to GitHub — it contains your database password and secret key
- Change `DEBUG=False` in `.env` when deploying to production
- Add your domain to `ALLOWED_HOSTS` in `.env` when deploying

---

## 👨‍💻 Author

**Chirag Sharma**
GitHub: [@chirag20-sharma](https://github.com/chirag20-sharma)
