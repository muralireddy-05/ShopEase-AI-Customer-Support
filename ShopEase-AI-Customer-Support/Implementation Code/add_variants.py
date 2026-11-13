import sqlite3

DATABASE = "shopease.db"

connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS product_variants (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    color TEXT,
    size TEXT,
    storage TEXT,
    price INTEGER NOT NULL,
    stock INTEGER DEFAULT 10,
    sku TEXT UNIQUE,
    FOREIGN KEY (product_id) REFERENCES products(id)
)
""")

connection.commit()
connection.close()

print("Product variants table created successfully!")