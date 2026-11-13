// ================= CART FUNCTIONS =================

function addToCart(productName) {

    let cart =
        JSON.parse(localStorage.getItem("cart")) || [];

    // Old-style products are still supported
    cart.push({
        product_name: productName,
        price: getProductPrice(productName),
        quantity: 1
    });

    localStorage.setItem(
        "cart",
        JSON.stringify(cart)
    );

    alert(
        productName +
        " has been added to your cart! 🛒"
    );

    // If cart page is open, refresh it
    displayCart();
}


// ================= DISPLAY CART =================

function displayCart() {

    const cartItems =
        document.getElementById("cart-items");

    if (!cartItems) {
        return;
    }

    let cart =
        JSON.parse(localStorage.getItem("cart")) || [];

    if (cart.length === 0) {

        cartItems.innerHTML = `
            <div class="empty-cart">

                <div class="empty-cart-icon">
                    🛒
                </div>

                <h3>
                    Your cart is empty
                </h3>

                <p>
                    Add some products to your cart
                    to see them here.
                </p>

            </div>
        `;

        updateTotal(0);
        return;
    }

    let total = 0;

    cartItems.innerHTML = "";

    cart.forEach(function(product, index) {

        // Support both old string items
        // and new product objects
        if (typeof product === "string") {

            product = {
                product_name: product,
                price: getProductPrice(product),
                quantity: 1
            };

            cart[index] = product;
        }

        const price =
            Number(product.price) || 0;

        const quantity =
            Number(product.quantity) || 1;

        const lineTotal =
            price * quantity;

        total += lineTotal;

        const item =
            document.createElement("div");

        item.className =
            "cart-item";

        // Variant information
        let variantDetails = "";

        if (product.color) {
            variantDetails += `
                <p>Color: ${product.color}</p>
            `;
        }

        if (product.size) {
            variantDetails += `
                <p>Size: ${product.size}</p>
            `;
        }

        if (product.storage) {
            variantDetails += `
                <p>Storage: ${product.storage}</p>
            `;
        }

        item.innerHTML = `

            <div class="cart-item-info">

                <div class="cart-item-image">
                    ${getProductIcon(product)}
                </div>

                <div>

                    <h3>
                        ${product.product_name}
                    </h3>

                    <div class="cart-variant-details">
                        ${variantDetails}
                    </div>

                    <p class="cart-item-price">
                        ₹${price.toLocaleString("en-IN")}
                    </p>

                    <p>
                        Quantity: ${quantity}
                    </p>

                    <p>
                        Total:
                        ₹${lineTotal.toLocaleString("en-IN")}
                    </p>

                </div>

            </div>

            <button
                class="remove-btn"
                onclick="removeFromCart(${index})">

                Remove

            </button>
        `;

        cartItems.appendChild(item);

    });

    // Save converted old-style items
    // back into localStorage
    localStorage.setItem(
        "cart",
        JSON.stringify(cart)
    );

    updateTotal(total);
}


// ================= PRODUCT PRICE =================

function getProductPrice(product) {

    // New cart object
    if (typeof product === "object" && product !== null) {

        return Number(product.price) || 0;
    }

    // Old product-name format
    const prices = {

        "Wireless Headphones": 1499,

        "Smart Watch": 1999,

        "Bluetooth Speaker": 1299,

        "Wireless Mouse": 699,

        "Running Shoes": 2499,

        "Premium T-Shirt": 799,

        "Skin Care Set": 1199,

        "Urban Backpack": 999

    };

    return prices[product] || 0;
}


// ================= PRODUCT ICON =================

function getProductIcon(product) {

    const productName =
        typeof product === "object"
            ? product.product_name
            : product;

    const icons = {

        "Wireless Headphones": "🎧",

        "Smart Watch": "⌚",

        "Bluetooth Speaker": "🔊",

        "Wireless Mouse": "🖱️",

        "Running Shoes": "👟",

        "Premium T-Shirt": "👕",

        "Skin Care Set": "🧴",

        "Urban Backpack": "🎒",

        "iPhone 16": "📱",

        "Samsung Galaxy S25": "📱",

        "OnePlus 13": "📱",

        "Smart LED TV 43 inch": "📺",

        "Wireless Earbuds Pro": "🎧",

        "Gaming Keyboard": "⌨️",

        "Power Bank 20000mAh": "🔋",

        "Tablet 10 inch": "📱",

        "Casual Shirt": "👔",

        "Slim Fit Jeans": "👖",

        "Hoodie": "🧥",

        "Smart Watch Pro": "⌚",

        "Classic Analog Watch": "⌚",

        "Casual Sneakers": "👟",

        "Smart LED Table Lamp": "💡",

        "Wall Clock": "🕐",

        "Storage Organizer": "🗄️",

        "Cushion Set": "🛋️",

        "Desk Organizer": "📦",

        "Stainless Steel Water Bottle": "🍶"

    };

    return icons[productName] || "🛍️";
}


// ================= REMOVE FROM CART =================

function removeFromCart(index) {

    let cart =
        JSON.parse(localStorage.getItem("cart")) || [];

    cart.splice(index, 1);

    localStorage.setItem(
        "cart",
        JSON.stringify(cart)
    );

    displayCart();
}


// ================= UPDATE TOTAL =================

function updateTotal(total) {

    const subtotal =
        document.getElementById("cart-subtotal");

    const cartTotal =
        document.getElementById("cart-total");

    if (subtotal) {

        subtotal.textContent =
            "₹" +
            total.toLocaleString("en-IN");
    }

    if (cartTotal) {

        cartTotal.textContent =
            "₹" +
            total.toLocaleString("en-IN");
    }
}


async function checkout() {

    let cart = JSON.parse(localStorage.getItem("cart")) || [];

    // Check if cart is empty
    if (cart.length === 0) {
        alert("Your cart is empty. Please add a product first.");
        return;
    }

    try {

        const response = await fetch("/api/orders", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                cart: cart
            })
        });

        const result = await response.json();

        // If user is not logged in
        if (response.status === 401) {
            alert("Please login first to place your order.");
            window.location.href = "login.html";
            return;
        }

        // If order was successful
        if (result.success) {

            alert(
                "Order placed successfully! 🎉\n\n" +
                "Order ID: #" + result.order_id +
                "\nTotal: ₹" + result.total.toLocaleString("en-IN")
            );

            // Clear cart
            localStorage.removeItem("cart");

            // Refresh cart display
            displayCart();

            // Go to Orders page
            window.location.href = "orders.html";

        } else {

            alert(result.message);
        }

    } catch (error) {

        console.error("Checkout error:", error);

        alert(
            "Something went wrong while placing your order. Please try again."
        );
    }
}


displayCart();


function toggleFAQ(button) {

    const faqItem =
        button.parentElement;

    faqItem.classList.toggle("active");

}

async function submitContactForm(event) {

    event.preventDefault();

    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const orderNumber = document.getElementById("order").value;
    const message = document.getElementById("message").value;

    try {

        const response = await fetch("/api/contact", {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                name: name,
                email: email,
                order_number: orderNumber,
                message: message
            })
        });

        const result = await response.json();

        if (result.success) {

            alert(
                "Thank you, " +
                name +
                "! Your message has been submitted successfully. 📩"
            );

            event.target.reset();

        } else {

            alert(result.message);
        }

    } catch (error) {

        console.error("Contact form error:", error);

        alert(
            "Something went wrong. Please try again."
        );
    }
}

async function loginUser(event) {
    event.preventDefault();

    const email = document.getElementById("login-email").value;
    const password = document.getElementById("login-password").value;

    try {
        const response = await fetch("/api/login", {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                email: email,
                password: password
            })
        });

        const result = await response.json();

        if (result.success) {

            alert("Welcome " + result.user.name + "! 🎉");

            localStorage.setItem(
                "loggedInUser",
                JSON.stringify(result.user)
            );

        } else {

            alert(result.message);

        }

    } catch (error) {

        console.error("Login error:", error);

        alert("Something went wrong. Please try again.");

    }
}

function forgotPassword(event) {

    event.preventDefault();

    alert(
        "Password reset feature will be available soon."
    );

}

function createAccount(event) {
    event.preventDefault();

    const registerForm = document.getElementById("register-form");

    if (registerForm) {
        registerForm.style.display = "block";
        registerForm.scrollIntoView({
            behavior: "smooth"
        });
    }
}


async function registerUser(event) {
    event.preventDefault();

    const name = document.getElementById("register-name").value;
    const email = document.getElementById("register-email").value;
    const password = document.getElementById("register-password").value;

    try {

        const response = await fetch("/api/register", {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                name: name,
                email: email,
                password: password
            })
        });

        const result = await response.json();

        if (result.success) {

            alert("Account created successfully! 🎉");

            document.getElementById("register-form").style.display = "none";

        } else {

            alert(result.message);

        }

    } catch (error) {

        console.error("Registration error:", error);

        alert("Something went wrong. Please try again.");

    }
}

// ================= GLOBAL PRODUCT SEARCH =================

function globalProductSearch() {

    const searchInput =
        document.getElementById("search-input");

    if (!searchInput) {
        return;
    }

    const searchText =
        searchInput.value.trim();

    if (searchText === "") {
        return;
    }

    // Save search text so products.html can use it
    localStorage.setItem(
        "productSearch",
        searchText
    );

    // Open Products page
    window.location.href = "products.html";
}