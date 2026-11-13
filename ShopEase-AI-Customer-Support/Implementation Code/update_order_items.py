import sqlite3

DATABASE = "shopease.db"

connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

# Get existing columns
cursor.execute("PRAGMA table_info(order_items)")
columns = [column[1] for column in cursor.fetchall()]

# Add variant_id if it doesn't exist
if "variant_id" not in columns:
    cursor.execute("""
        ALTER TABLE order_items
        ADD COLUMN variant_id INTEGER
    """)

# Add color if it doesn't exist
if "color" not in columns:
    cursor.execute("""
        ALTER TABLE order_items
        ADD COLUMN color TEXT
    """)

# Add size if it doesn't exist
if "size" not in columns:
    cursor.execute("""
        ALTER TABLE order_items
        ADD COLUMN size TEXT
    """)

# Add storage if it doesn't exist
if "storage" not in columns:
    cursor.execute("""
        ALTER TABLE order_items
        ADD COLUMN storage TEXT
    """)

connection.commit()
connection.close()

print("Order items table updated successfully!")