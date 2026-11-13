import sqlite3

DATABASE = "shopease.db"

connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

def get_product_id(product_name):
    cursor.execute(
        "SELECT id FROM products WHERE name = ?",
        (product_name,)
    )
    result = cursor.fetchone()

    if result:
        return result[0]

    print(f"Product not found: {product_name}")
    return None


def add_variant(product_name, color=None, size=None, storage=None,
                price=None, stock=10, sku=None):

    product_id = get_product_id(product_name)

    if product_id is None:
        return

    cursor.execute(
        """
        INSERT OR IGNORE INTO product_variants
        (product_id, color, size, storage, price, stock, sku)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            product_id,
            color,
            size,
            storage,
            price,
            stock,
            sku
        )
    )


# =========================================================
# iPhone 16
# =========================================================

iphone_colors = ["Black", "Blue", "Pink"]

for color in iphone_colors:
    add_variant(
        "iPhone 16",
        color=color,
        storage="128GB",
        price=69999,
        sku=f"IPH16-{color.upper()}-128"
    )

    add_variant(
        "iPhone 16",
        color=color,
        storage="256GB",
        price=79999,
        sku=f"IPH16-{color.upper()}-256"
    )


# =========================================================
# Samsung Galaxy S25
# =========================================================

samsung_colors = ["Black", "Blue", "Silver"]

for color in samsung_colors:
    add_variant(
        "Samsung Galaxy S25",
        color=color,
        storage="128GB",
        price=74999,
        sku=f"S25-{color.upper()}-128"
    )

    add_variant(
        "Samsung Galaxy S25",
        color=color,
        storage="256GB",
        price=84999,
        sku=f"S25-{color.upper()}-256"
    )


# =========================================================
# OnePlus 13
# =========================================================

oneplus_colors = ["Black", "Blue", "White"]

for color in oneplus_colors:
    add_variant(
        "OnePlus 13",
        color=color,
        storage="128GB",
        price=64999,
        sku=f"OP13-{color.upper()}-128"
    )

    add_variant(
        "OnePlus 13",
        color=color,
        storage="256GB",
        price=74999,
        sku=f"OP13-{color.upper()}-256"
    )


# =========================================================
# Premium T-Shirt
# =========================================================

tshirt_colors = ["Black", "White", "Blue", "Red"]
tshirt_sizes = ["S", "M", "L", "XL"]

for color in tshirt_colors:
    for size in tshirt_sizes:
        add_variant(
            "Premium T-Shirt",
            color=color,
            size=size,
            price=799,
            sku=f"TSHIRT-{color.upper()}-{size}"
        )


# =========================================================
# Casual Shirt
# =========================================================

shirt_colors = ["Black", "White", "Navy Blue"]
shirt_sizes = ["M", "L", "XL", "XXL"]

for color in shirt_colors:
    for size in shirt_sizes:
        add_variant(
            "Casual Shirt",
            color=color,
            size=size,
            price=1299,
            sku=f"SHIRT-{color.upper()}-{size}"
        )


# =========================================================
# Slim Fit Jeans
# =========================================================

jeans_colors = ["Black", "Blue", "Dark Blue"]
jeans_sizes = ["30", "32", "34", "36"]

for color in jeans_colors:
    for size in jeans_sizes:
        add_variant(
            "Slim Fit Jeans",
            color=color,
            size=size,
            price=1799,
            sku=f"JEANS-{color.upper()}-{size}"
        )


# =========================================================
# Hoodie
# =========================================================

hoodie_colors = ["Black", "Grey", "Blue"]
hoodie_sizes = ["S", "M", "L", "XL"]

for color in hoodie_colors:
    for size in hoodie_sizes:
        add_variant(
            "Hoodie",
            color=color,
            size=size,
            price=1499,
            sku=f"HOODIE-{color.upper()}-{size}"
        )


# =========================================================
# Smart Watch Pro
# =========================================================

watch_colors = ["Black", "Silver", "Rose Gold"]

for color in watch_colors:
    add_variant(
        "Smart Watch Pro",
        color=color,
        price=2999,
        sku=f"SWPRO-{color.upper()}"
    )


# =========================================================
# Classic Analog Watch
# =========================================================

analog_colors = ["Black", "Silver", "Gold"]

for color in analog_colors:
    add_variant(
        "Classic Analog Watch",
        color=color,
        price=1999,
        sku=f"ANALOG-{color.upper()}"
    )


# =========================================================
# Casual Sneakers
# =========================================================

sneaker_colors = ["Black", "White", "Grey"]
sneaker_sizes = ["7", "8", "9", "10", "11"]

for color in sneaker_colors:
    for size in sneaker_sizes:
        add_variant(
            "Casual Sneakers",
            color=color,
            size=size,
            price=2199,
            sku=f"SNEAKER-{color.upper()}-{size}"
        )


connection.commit()
connection.close()

print("Product variants added successfully!")