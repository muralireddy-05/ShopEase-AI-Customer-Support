import sqlite3

connection = sqlite3.connect("shopease.db")

cursor = connection.cursor()


# Users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
""")


# Products table
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price INTEGER NOT NULL,
    category TEXT,
    icon TEXT
)
""")


# Orders table
cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    total INTEGER NOT NULL,
    status TEXT DEFAULT 'Processing',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
)
""")


# Order items table
cursor.execute("""
CREATE TABLE IF NOT EXISTS order_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER,
    product_name TEXT NOT NULL,
    price INTEGER NOT NULL,
    quantity INTEGER DEFAULT 1,
    FOREIGN KEY (order_id) REFERENCES orders(id)
)
""")


# Contact messages table
cursor.execute("""
CREATE TABLE IF NOT EXISTS contact_messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    order_number TEXT,
    message TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")


# Add ShopEase products
products = [
    ("Wireless Headphones", 1499, "Electronics", "🎧"),
    ("Smart Watch", 1999, "Electronics", "⌚"),
    ("Bluetooth Speaker", 1299, "Electronics", "🔊"),
    ("Wireless Mouse", 699, "Electronics", "🖱️"),
    ("Running Shoes", 2499, "Fashion", "👟"),
    ("Premium T-Shirt", 799, "Fashion", "👕"),
    ("Skin Care Set", 1199, "Beauty", "🧴"),
    ("Urban Backpack", 999, "Accessories", "🎒")
]

cursor.executemany("""
INSERT OR IGNORE INTO products (name, price, category, icon)
VALUES (?, ?, ?, ?)
""", products)


connection.commit()
connection.close()

print("ShopEase database created successfully!")
print("8 products added to the database!")