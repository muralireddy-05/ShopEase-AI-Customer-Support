import sqlite3

DATABASE = "shopease.db"

connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

products = [
    # Mobile Phones
    ("iPhone 16", 69999, "Mobile Phones", "📱"),
    ("Samsung Galaxy S25", 74999, "Mobile Phones", "📱"),
    ("OnePlus 13", 64999, "Mobile Phones", "📱"),

    # Electronics
    ("Smart LED TV 43 inch", 29999, "Electronics", "📺"),
    ("Wireless Earbuds Pro", 2499, "Electronics", "🎧"),
    ("Gaming Keyboard", 1799, "Electronics", "⌨️"),
    ("Power Bank 20000mAh", 1499, "Electronics", "🔋"),
    ("Tablet 10 inch", 12999, "Electronics", "📱"),

    # Fashion
    ("Premium T-Shirt", 799, "Fashion", "👕"),
    ("Casual Shirt", 1299, "Fashion", "👔"),
    ("Slim Fit Jeans", 1799, "Fashion", "👖"),
    ("Hoodie", 1499, "Fashion", "🧥"),

    # Watches
    ("Smart Watch Pro", 2999, "Watches", "⌚"),
    ("Classic Analog Watch", 1999, "Watches", "⌚"),

    # Footwear
    ("Running Shoes", 2499, "Footwear", "👟"),
    ("Casual Sneakers", 2199, "Footwear", "👟"),

    # Home Accessories
    ("Smart LED Table Lamp", 999, "Home Accessories", "💡"),
    ("Wall Clock", 699, "Home Accessories", "🕐"),
    ("Storage Organizer", 599, "Home Accessories", "🗄️"),
    ("Cushion Set", 899, "Home Accessories", "🛋️"),
    ("Desk Organizer", 499, "Home Accessories", "📦"),

    # Beauty
    ("Skin Care Set", 1199, "Beauty", "🧴"),

    # Accessories
    ("Urban Backpack", 999, "Accessories", "🎒"),
    ("Stainless Steel Water Bottle", 699, "Accessories", "🍶")
]

for product in products:
    cursor.execute(
        """
        INSERT INTO products (name, price, category, icon)
        SELECT ?, ?, ?, ?
        WHERE NOT EXISTS (
            SELECT 1 FROM products WHERE name = ?
        )
        """,
        (*product, product[0])
    )

connection.commit()
connection.close()

print("New ShopEase products added successfully!")