from flask import Flask, send_from_directory, jsonify, request, session
import sqlite3
import os
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "shopease-secret-key-2026"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, "shopease.db")


@app.route("/")
def home():
    return send_from_directory(BASE_DIR, "index.html")


@app.route("/api/products")
def get_products():

    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM products")

    products = cursor.fetchall()

    connection.close()

    return jsonify([dict(product) for product in products])

@app.route("/api/products/<int:product_id>/variants")
def get_product_variants(product_id):
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    try:
        cursor.execute(
            """
            SELECT id, color, size, storage, price, stock, sku
            FROM product_variants
            WHERE product_id = ?
            """,
            (product_id,)
        )

        variants = cursor.fetchall()
        connection.close()

        return jsonify([dict(variant) for variant in variants])

    except Exception as error:
        connection.close()
        print("Variant error:", error)

        return jsonify({
            "success": False,
            "message": "Unable to load product variants"
        }), 500

@app.route("/api/register", methods=["POST"])
def register():
    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    if not name or not email or not password:
        return jsonify({
            "success": False,
            "message": "All fields are required"
        }), 400

    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    # Check if email already exists
    cursor.execute(
        "SELECT id FROM users WHERE email = ?",
        (email,)
    )

    existing_user = cursor.fetchone()

    if existing_user:
        connection.close()

        return jsonify({
            "success": False,
            "message": "Email already registered"
        }), 400

    # Securely hash the password
    hashed_password = generate_password_hash(password)

    cursor.execute(
        """
        INSERT INTO users (name, email, password)
        VALUES (?, ?, ?)
        """,
        (name, email, hashed_password)
    )

    connection.commit()
    connection.close()

    return jsonify({
        "success": True,
        "message": "Account created successfully"
    })
@app.route("/api/login", methods=["POST"])

def login():
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({
            "success": False,
            "message": "Email and password are required"
        }), 400

    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE email = ?",
        (email,)
    )

    user = cursor.fetchone()

    connection.close()

    if user is None:
        return jsonify({
            "success": False,
            "message": "Account not found"
        }), 401

    if not check_password_hash(user["password"], password):
        return jsonify({
            "success": False,
            "message": "Incorrect password"
        }), 401

    session["user_id"] = user["id"]
    session["user_name"] = user["name"]
    session["user_email"] = user["email"]

    return jsonify({
        "success": True,
        "message": "Login successful",
        "user": {
            "id": user["id"],
            "name": user["name"],
            "email": user["email"]
        }
    })

@app.route("/<path:filename>")
def serve_file(filename):
    return send_from_directory(BASE_DIR, filename)

@app.route("/api/orders", methods=["POST"])
def create_order():

    user_id = session.get("user_id")

    if not user_id:
        return jsonify({
            "success": False,
            "message": "Please login first"
        }), 401

    data = request.get_json()
    cart = data.get("cart", [])

    if not cart:
        return jsonify({
            "success": False,
            "message": "Your cart is empty"
        }), 400

    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    try:

        total = 0
        order_items = []

        # ===============================
        # CHECK EACH CART ITEM
        # ===============================

        for item in cart:

            # Support new object-style cart
            if isinstance(item, dict):

                product_id = item.get("product_id")
                product_name = item.get("product_name")
                variant_id = item.get("variant_id")
                color = item.get("color")
                size = item.get("size")
                storage = item.get("storage")
                quantity = int(item.get("quantity", 1))

                if quantity < 1:
                    quantity = 1

                # Make sure the product exists
                cursor.execute(
                    """
                    SELECT id, name, price
                    FROM products
                    WHERE id = ?
                    """,
                    (product_id,)
                )

                product = cursor.fetchone()

                if product is None:
                    connection.rollback()
                    connection.close()

                    return jsonify({
                        "success": False,
                        "message": "Product not found"
                    }), 400

                # =================================
                # VARIANT PRODUCT
                # =================================

                if variant_id:

                    cursor.execute(
                        """
                        SELECT
                            id,
                            product_id,
                            color,
                            size,
                            storage,
                            price,
                            stock
                        FROM product_variants
                        WHERE id = ?
                        AND product_id = ?
                        """,
                        (variant_id, product_id)
                    )

                    variant = cursor.fetchone()

                    if variant is None:
                        connection.rollback()
                        connection.close()

                        return jsonify({
                            "success": False,
                            "message": "Selected product variant not found"
                        }), 400

                    # Check stock
                    if variant["stock"] < quantity:

                        connection.rollback()
                        connection.close()

                        return jsonify({
                            "success": False,
                            "message":
                                f"Only {variant['stock']} item(s) "
                                f"available for {product['name']}"
                        }), 400

                    item_price = variant["price"]

                    order_items.append({
                        "product_name": product["name"],
                        "price": item_price,
                        "quantity": quantity,
                        "variant_id": variant["id"],
                        "color": variant["color"],
                        "size": variant["size"],
                        "storage": variant["storage"]
                    })

                # =================================
                # NORMAL PRODUCT WITHOUT VARIANT
                # =================================

                else:

                    item_price = product["price"]

                    order_items.append({
                        "product_name": product["name"],
                        "price": item_price,
                        "quantity": quantity,
                        "variant_id": None,
                        "color": None,
                        "size": None,
                        "storage": None
                    })

                total += item_price * quantity

            # =====================================
            # OLD CART FORMAT
            # =====================================

            else:

                product_name = item

                cursor.execute(
                    """
                    SELECT name, price
                    FROM products
                    WHERE name = ?
                    """,
                    (product_name,)
                )

                product = cursor.fetchone()

                if product is None:

                    connection.rollback()
                    connection.close()

                    return jsonify({
                        "success": False,
                        "message":
                            f"Product not found: {product_name}"
                    }), 400

                item_price = product["price"]

                order_items.append({
                    "product_name": product["name"],
                    "price": item_price,
                    "quantity": 1,
                    "variant_id": None,
                    "color": None,
                    "size": None,
                    "storage": None
                })

                total += item_price

        # ===============================
        # CREATE ORDER
        # ===============================

        cursor.execute(
            """
            INSERT INTO orders
            (user_id, total, status)
            VALUES (?, ?, ?)
            """,
            (
                user_id,
                total,
                "Processing"
            )
        )

        order_id = cursor.lastrowid

        # ===============================
        # SAVE ORDER ITEMS
        # ===============================

        for item in order_items:

            cursor.execute(
                """
                INSERT INTO order_items
                (
                    order_id,
                    product_name,
                    price,
                    quantity,
                    variant_id,
                    color,
                    size,
                    storage
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    order_id,
                    item["product_name"],
                    item["price"],
                    item["quantity"],
                    item["variant_id"],
                    item["color"],
                    item["size"],
                    item["storage"]
                )
            )

        connection.commit()
        connection.close()

        return jsonify({
            "success": True,
            "message": "Order placed successfully",
            "order_id": order_id,
            "total": total
        })

    except Exception as error:

        connection.rollback()
        connection.close()

        print("Order error:", error)

        return jsonify({
            "success": False,
            "message":
                "Something went wrong while placing your order"
        }), 500
        
@app.route("/api/orders", methods=["GET"])
def get_orders():

    user_id = session.get("user_id")

    if not user_id:
        return jsonify({
            "success": False,
            "message": "Please login first"
        }), 401

    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    try:

        cursor.execute(
            """
            SELECT id, total, status, created_at
            FROM orders
            WHERE user_id = ?
            ORDER BY id DESC
            """,
            (user_id,)
        )

        orders = cursor.fetchall()

        order_list = []

        for order in orders:

            cursor.execute(
                """
                SELECT
                    product_name,
                    price,
                    quantity,
                    variant_id,
                    color,
                    size,
                    storage
                FROM order_items
                WHERE order_id = ?
                """,
                (order["id"],)
            )

            items = cursor.fetchall()

            order_list.append({

                "id": order["id"],

                "total": order["total"],

                "status": order["status"],

                "created_at": order["created_at"],

                "items": [
                    dict(item)
                    for item in items
                ]

            })

        connection.close()

        return jsonify({
            "success": True,
            "orders": order_list
        })

    except Exception as error:

        connection.close()

        print(
            "Get orders error:",
            error
        )

        return jsonify({
            "success": False,
            "message":
                "Unable to load orders"
        }), 500
        
@app.route("/api/contact", methods=["POST"])
def submit_contact():

    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    order_number = data.get("order_number")
    message = data.get("message")

    # Check required fields
    if not name or not email or not message:
        return jsonify({
            "success": False,
            "message": "Please fill in all required fields"
        }), 400

    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    try:

        cursor.execute(
            """
            INSERT INTO contact_messages
            (name, email, order_number, message)
            VALUES (?, ?, ?, ?)
            """,
            (
                name,
                email,
                order_number,
                message
            )
        )

        connection.commit()
        connection.close()

        return jsonify({
            "success": True,
            "message": "Your message has been submitted successfully"
        })

    except Exception as error:

        connection.rollback()
        connection.close()

        print("Contact form error:", error)

        return jsonify({
            "success": False,
            "message": "Something went wrong. Please try again."
        }), 500
        
@app.route("/api/order/<int:order_id>", methods=["GET"])
def get_order_status(order_id):

    user_id = session.get("user_id")

    if not user_id:
        return jsonify({
            "success": False,
            "message": "Please login first"
        }), 401

    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    try:

        cursor.execute(
            """
            SELECT id, total, status, created_at
            FROM orders
            WHERE id = ? AND user_id = ?
            """,
            (order_id, user_id)
        )

        order = cursor.fetchone()

        if order is None:
            connection.close()

            return jsonify({
                "success": False,
                "message": "Order not found"
            }), 404

        cursor.execute(
            """
            SELECT product_name, price, quantity
            FROM order_items
            WHERE order_id = ?
            """,
            (order_id,)
        )

        items = cursor.fetchall()

        connection.close()

        return jsonify({
            "success": True,
            "order": {
                "id": order["id"],
                "total": order["total"],
                "status": order["status"],
                "created_at": order["created_at"],
                "items": [dict(item) for item in items]
            }
        })

    except Exception as error:

        connection.close()

        print("Order status error:", error)

        return jsonify({
            "success": False,
            "message": "Unable to check order status"
        }), 500
        
@app.route("/api/chatbot/order/<order_number>", methods=["GET"])
def chatbot_order_status(order_number):

    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    try:

        # Convert SE0001 into database ID 1
        if order_number.upper().startswith("SE"):
            order_id = int(order_number[2:])
        else:
            order_id = int(order_number)

        cursor.execute(
            """
            SELECT id, total, status, created_at
            FROM orders
            WHERE id = ?
            """,
            (order_id,)
        )

        order = cursor.fetchone()

        if order is None:
            connection.close()

            return jsonify({
                "success": False,
                "message": "Order not found"
            }), 404

        cursor.execute(
            """
            SELECT product_name, price, quantity
            FROM order_items
            WHERE order_id = ?
            """,
            (order_id,)
        )

        items = cursor.fetchall()

        connection.close()

        return jsonify({
            "success": True,
            "order": {
                "order_number": "SE" + str(order["id"]).zfill(4),
                "total": order["total"],
                "status": order["status"],
                "created_at": order["created_at"],
                "items": [dict(item) for item in items]
            }
        })

    except ValueError:

        connection.close()

        return jsonify({
            "success": False,
            "message": "Invalid order number"
        }), 400

    except Exception as error:

        connection.close()

        print("Chatbot order error:", error)

        return jsonify({
            "success": False,
            "message": "Unable to check order status"
        }), 500
        
if __name__ == "__main__":
    app.run(debug=True)