# Botpress Configuration Notes — ShopEase

## Platform
The project uses Botpress Cloud and Botpress Webchat.

## Knowledge sources
The chatbot uses product information and website/FAQ content as knowledge sources. Check the accompanying text files against the live website before importing them.

## Website integration
Botpress Webchat is integrated with the ShopEase frontend. Keep the actual Webchat embed snippet in the frontend source file where it is already configured. Do not publish private workspace credentials or secret tokens.

## Order-status tool
- Tool name: `getOrderStatus`
- Backend: ShopEase Flask application
- Route pattern: `/api/chatbot/order/{order_number}`
- Purpose: retrieve an order's status from the backend.

Configure the full deployed backend URL and copy the exact HTTP method, headers, response JSON, and authentication requirements from the actual Flask implementation. Those details are intentionally not guessed in this document.

## Tests recorded in the project
- iPhone 16 — ₹69,999; 128GB and 256GB options.
- Samsung Galaxy S25 — ₹74,999; 128GB and 256GB options.
- OnePlus 13 — Black, Blue, and White variants.
- Return-policy question — configured seven-day policy.
- Order SE0001 — Processing; Wireless Headphones; ₹1,499.
- An unrelated general-knowledge question was politely declined as out of scope.

## Repository safety
Do not commit Botpress tokens, API keys, passwords, `.env` files, or real customer/order records. Use sanitized demonstration data only.
