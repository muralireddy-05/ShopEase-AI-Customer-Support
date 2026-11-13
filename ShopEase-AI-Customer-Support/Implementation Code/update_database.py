import sqlite3

DATABASE = "shopease.db"


def add_column_if_missing(cursor, table, column, column_type):
    cursor.execute(f"PRAGMA table_info({table})")
    columns = [row[1] for row in cursor.fetchall()]

    if column not in columns:
        cursor.execute(
            f"ALTER TABLE {table} ADD COLUMN {column} {column_type}"
        )
        print(f"Added column: {table}.{column}")


connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

print("Connected to ShopEase database.")


# =========================================================
# 1. PRODUCT VARIANTS TABLE
# =========================================================

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

print("Product variants table checked.")


# =========================================================
# 2. UPDATE ORDER ITEMS TABLE
# =========================================================

add_column_if_missing(
    cursor,
    "order_items",
    "variant_id",
    "INTEGER"
)

add_column_if_missing(
    cursor,
    "order_items",
    "color",
    "TEXT"
)

add_column_if_missing(
    cursor,
    "order_items",
    "size",
    "TEXT"
)

add_column_if_missing(
    cursor,
    "order_items",
    "storage",
    "TEXT"
)


# =========================================================
# 3. NEW PRODUCTS
# =========================================================

products = [
    ("iPhone 16", 69999, "Mobile Phones", "📱"),
    ("Samsung Galaxy S25", 74999, "Mobile Phones", "📱"),
    ("OnePlus 13", 64999, "Mobile Phones", "📱"),

    ("Smart LED TV 43 inch", 29999, "Electronics", "📺"),
    ("Wireless Earbuds Pro", 2499, "Electronics", "🎧"),
    ("Gaming Keyboard", 1799, "Electronics", "⌨️"),
    ("Power Bank 20000mAh", 1499, "Electronics", "🔋"),
    ("Tablet 10 inch", 12999, "Electronics", "📱"),

    ("Premium T-Shirt", 799, "Fashion", "👕"),
    ("Casual Shirt", 1299, "Fashion", "👔"),
    ("Slim Fit Jeans", 1799, "Fashion", "👖"),
    ("Hoodie", 1499, "Fashion", "🧥"),

    ("Smart Watch Pro", 2999, "Watches", "⌚"),
    ("Classic Analog Watch", 1999, "Watches", "⌚"),

    ("Running Shoes", 2499, "Footwear", "👟"),
    ("Casual Sneakers", 2199, "Footwear", "👟"),

    ("Smart LED Table Lamp", 999, "Home Accessories", "💡"),
    ("Wall Clock", 699, "Home Accessories", "🕐"),
    ("Storage Organizer", 599, "Home Accessories", "🗄️"),
    ("Cushion Set", 899, "Home Accessories", "🛋️"),
    ("Desk Organizer", 499, "Home Accessories", "📦"),

    ("Skin Care Set", 1199, "Beauty", "🧴"),

    ("Urban Backpack", 999, "Accessories", "🎒"),
    ("Stainless Steel Water Bottle", 699, "Accessories", "🍶")
]


# =========================================================
# 4. INSERT PRODUCTS ONLY IF THEY DON'T EXIST
# =========================================================

product_ids = {}

for name, price, category, icon in products:

    cursor.execute(
        "SELECT id FROM products WHERE name = ?",
        (name,)
    )

    existing = cursor.fetchone()

    if existing:
        product_id = existing[0]
        print(f"Already exists: {name}")

    else:
        cursor.execute("""
            INSERT INTO products
            (name, price, category, icon)
            VALUES (?, ?, ?, ?)
        """, (name, price, category, icon))

        product_id = cursor.lastrowid

        print(f"Added product: {name}")

    product_ids[name] = product_id


# =========================================================
# 5. PRODUCT VARIANTS
# =========================================================

variants = [

    # iPhone 16
    ("iPhone 16", "Black", None, "128GB", 69999, 10, "IPH16-BLK-128"),
    ("iPhone 16", "Black", None, "256GB", 74999, 10, "IPH16-BLK-256"),
    ("iPhone 16", "Blue", None, "128GB", 69999, 10, "IPH16-BLU-128"),
    ("iPhone 16", "Blue", None, "256GB", 74999, 10, "IPH16-BLU-256"),
    ("iPhone 16", "Pink", None, "128GB", 69999, 10, "IPH16-PNK-128"),
    ("iPhone 16", "Pink", None, "256GB", 74999, 10, "IPH16-PNK-256"),

    # Samsung Galaxy S25
    ("Samsung Galaxy S25", "Black", None, "128GB", 74999, 10, "S25-BLK-128"),
    ("Samsung Galaxy S25", "Black", None, "256GB", 79999, 10, "S25-BLK-256"),
    ("Samsung Galaxy S25", "Blue", None, "128GB", 74999, 10, "S25-BLU-128"),
    ("Samsung Galaxy S25", "Blue", None, "256GB", 79999, 10, "S25-BLU-256"),
    ("Samsung Galaxy S25", "Silver", None, "128GB", 74999, 10, "S25-SLV-128"),
    ("Samsung Galaxy S25", "Silver", None, "256GB", 79999, 10, "S25-SLV-256"),

    # OnePlus 13
    ("OnePlus 13", "Black", None, "128GB", 64999, 10, "OP13-BLK-128"),
    ("OnePlus 13", "Black", None, "256GB", 69999, 10, "OP13-BLK-256"),
    ("OnePlus 13", "Blue", None, "128GB", 64999, 10, "OP13-BLU-128"),
    ("OnePlus 13", "Blue", None, "256GB", 69999, 10, "OP13-BLU-256"),
    ("OnePlus 13", "White", None, "128GB", 64999, 10, "OP13-WHT-128"),
    ("OnePlus 13", "White", None, "256GB", 69999, 10, "OP13-WHT-256"),

    # Premium T-Shirt
    ("Premium T-Shirt", "Black", "S", None, 799, 10, "TSH-BLK-S"),
    ("Premium T-Shirt", "Black", "M", None, 799, 10, "TSH-BLK-M"),
    ("Premium T-Shirt", "Black", "L", None, 799, 10, "TSH-BLK-L"),
    ("Premium T-Shirt", "Black", "XL", None, 799, 10, "TSH-BLK-XL"),

    ("Premium T-Shirt", "White", "S", None, 799, 10, "TSH-WHT-S"),
    ("Premium T-Shirt", "White", "M", None, 799, 10, "TSH-WHT-M"),
    ("Premium T-Shirt", "White", "L", None, 799, 10, "TSH-WHT-L"),
    ("Premium T-Shirt", "White", "XL", None, 799, 10, "TSH-WHT-XL"),

    ("Premium T-Shirt", "Blue", "S", None, 799, 10, "TSH-BLU-S"),
    ("Premium T-Shirt", "Blue", "M", None, 799, 10, "TSH-BLU-M"),
    ("Premium T-Shirt", "Blue", "L", None, 799, 10, "TSH-BLU-L"),
    ("Premium T-Shirt", "Blue", "XL", None, 799, 10, "TSH-BLU-XL"),

    ("Premium T-Shirt", "Red", "S", None, 799, 10, "TSH-RED-S"),
    ("Premium T-Shirt", "Red", "M", None, 799, 10, "TSH-RED-M"),
    ("Premium T-Shirt", "Red", "L", None, 799, 10, "TSH-RED-L"),
    ("Premium T-Shirt", "Red", "XL", None, 799, 10, "TSH-RED-XL"),

    # Casual Shirt
    ("Casual Shirt", "Black", "M", None, 1299, 10, "CSH-BLK-M"),
    ("Casual Shirt", "Black", "L", None, 1299, 10, "CSH-BLK-L"),
    ("Casual Shirt", "Black", "XL", None, 1299, 10, "CSH-BLK-XL"),
    ("Casual Shirt", "Black", "XXL", None, 1299, 10, "CSH-BLK-XXL"),

    ("Casual Shirt", "White", "M", None, 1299, 10, "CSH-WHT-M"),
    ("Casual Shirt", "White", "L", None, 1299, 10, "CSH-WHT-L"),
    ("Casual Shirt", "White", "XL", None, 1299, 10, "CSH-WHT-XL"),
    ("Casual Shirt", "White", "XXL", None, 1299, 10, "CSH-WHT-XXL"),

    ("Casual Shirt", "Navy Blue", "M", None, 1299, 10, "CSH-NAV-M"),
    ("Casual Shirt", "Navy Blue", "L", None, 1299, 10, "CSH-NAV-L"),
    ("Casual Shirt", "Navy Blue", "XL", None, 1299, 10, "CSH-NAV-XL"),
    ("Casual Shirt", "Navy Blue", "XXL", None, 1299, 10, "CSH-NAV-XXL"),

    # Slim Fit Jeans
    ("Slim Fit Jeans", "Black", "30", None, 1799, 10, "JEAN-BLK-30"),
    ("Slim Fit Jeans", "Black", "32", None, 1799, 10, "JEAN-BLK-32"),
    ("Slim Fit Jeans", "Black", "34", None, 1799, 10, "JEAN-BLK-34"),
    ("Slim Fit Jeans", "Black", "36", None, 1799, 10, "JEAN-BLK-36"),

    ("Slim Fit Jeans", "Blue", "30", None, 1799, 10, "JEAN-BLU-30"),
    ("Slim Fit Jeans", "Blue", "32", None, 1799, 10, "JEAN-BLU-32"),
    ("Slim Fit Jeans", "Blue", "34", None, 1799, 10, "JEAN-BLU-34"),
    ("Slim Fit Jeans", "Blue", "36", None, 1799, 10, "JEAN-BLU-36"),

    ("Slim Fit Jeans", "Dark Blue", "30", None, 1799, 10, "JEAN-DBL-30"),
    ("Slim Fit Jeans", "Dark Blue", "32", None, 1799, 10, "JEAN-DBL-32"),
    ("Slim Fit Jeans", "Dark Blue", "34", None, 1799, 10, "JEAN-DBL-34"),
    ("Slim Fit Jeans", "Dark Blue", "36", None, 1799, 10, "JEAN-DBL-36"),

    # Hoodie
    ("Hoodie", "Black", "S", None, 1499, 10, "HOD-BLK-S"),
    ("Hoodie", "Black", "M", None, 1499, 10, "HOD-BLK-M"),
    ("Hoodie", "Black", "L", None, 1499, 10, "HOD-BLK-L"),
    ("Hoodie", "Black", "XL", None, 1499, 10, "HOD-BLK-XL"),

    ("Hoodie", "Grey", "S", None, 1499, 10, "HOD-GRY-S"),
    ("Hoodie", "Grey", "M", None, 1499, 10, "HOD-GRY-M"),
    ("Hoodie", "Grey", "L", None, 1499, 10, "HOD-GRY-L"),
    ("Hoodie", "Grey", "XL", None, 1499, 10, "HOD-GRY-XL"),

    ("Hoodie", "Blue", "S", None, 1499, 10, "HOD-BLU-S"),
    ("Hoodie", "Blue", "M", None, 1499, 10, "HOD-BLU-M"),
    ("Hoodie", "Blue", "L", None, 1499, 10, "HOD-BLU-L"),
    ("Hoodie", "Blue", "XL", None, 1499, 10, "HOD-BLU-XL"),

    # Smart Watch Pro
    ("Smart Watch Pro", "Black", None, None, 2999, 10, "SWP-BLK"),
    ("Smart Watch Pro", "Silver", None, None, 2999, 10, "SWP-SLV"),
    ("Smart Watch Pro", "Rose Gold", None, None, 2999, 10, "SWP-RSG"),

    # Classic Analog Watch
    ("Classic Analog Watch", "Black", None, None, 1999, 10, "CAW-BLK"),
    ("Classic Analog Watch", "Silver", None, None, 1999, 10, "CAW-SLV"),
    ("Classic Analog Watch", "Gold", None, None, 1999, 10, "CAW-GLD"),

    # Casual Sneakers
    ("Casual Sneakers", "Black", "7", None, 2199, 10, "SNK-BLK-7"),
    ("Casual Sneakers", "Black", "8", None, 2199, 10, "SNK-BLK-8"),
    ("Casual Sneakers", "Black", "9", None, 2199, 10, "SNK-BLK-9"),
    ("Casual Sneakers", "Black", "10", None, 2199, 10, "SNK-BLK-10"),
    ("Casual Sneakers", "Black", "11", None, 2199, 10, "SNK-BLK-11"),

    ("Casual Sneakers", "White", "7", None, 2199, 10, "SNK-WHT-7"),
    ("Casual Sneakers", "White", "8", None, 2199, 10, "SNK-WHT-8"),
    ("Casual Sneakers", "White", "9", None, 2199, 10, "SNK-WHT-9"),
    ("Casual Sneakers", "White", "10", None, 2199, 10, "SNK-WHT-10"),
    ("Casual Sneakers", "White", "11", None, 2199, 10, "SNK-WHT-11"),

    ("Casual Sneakers", "Grey", "7", None, 2199, 10, "SNK-GRY-7"),
    ("Casual Sneakers", "Grey", "8", None, 2199, 10, "SNK-GRY-8"),
    ("Casual Sneakers", "Grey", "9", None, 2199, 10, "SNK-GRY-9"),
    ("Casual Sneakers", "Grey", "10", None, 2199, 10, "SNK-GRY-10"),
    ("Casual Sneakers", "Grey", "11", None, 2199, 10, "SNK-GRY-11")
]


# =========================================================
# 6. INSERT VARIANTS WITHOUT DUPLICATES
# =========================================================

for (
    product_name,
    color,
    size,
    storage,
    price,
    stock,
    sku
) in variants:

    product_id = product_ids.get(product_name)

    if not product_id:
        print(f"Product not found for variant: {product_name}")
        continue

    cursor.execute(
        "SELECT id FROM product_variants WHERE sku = ?",
        (sku,)
    )

    existing = cursor.fetchone()

    if existing:
        continue

    cursor.execute("""
        INSERT INTO product_variants
        (product_id, color, size, storage, price, stock, sku)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        product_id,
        color,
        size,
        storage,
        price,
        stock,
        sku
    ))

    print(f"Added variant: {sku}")


# =========================================================
# 7. SAVE CHANGES
# =========================================================

connection.commit()
connection.close()

print()
print("======================================")
print("ShopEase database update completed!")
print("Existing users and orders were preserved.")
print("======================================")