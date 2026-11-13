# ShopEase AI Chatbot

This folder contains chatbot documentation and knowledge-source examples for the ShopEase e-commerce customer-support project.

## Platform
- Botpress Cloud
- Botpress Webchat embedded in the ShopEase website

## Included files
- `product-catalog.txt` — sample product facts confirmed in the project demonstration.
- `faq-knowledge-base.txt` — support facts confirmed in the project context.
- `botpress-configuration-notes.md` — notes about the Botpress setup and website integration.

## Order-status integration
The Botpress HTTP tool is named `getOrderStatus`. It calls the Flask endpoint:

`/api/chatbot/order/{order_number}`

Use the full deployed backend URL when configuring the tool. Follow the exact HTTP method, headers, response format, and authentication requirements in your actual Flask code.

## Important
These are supporting documentation and sample knowledge files, **not an export of your live Botpress bot**. If your faculty requires the actual bot workflows/configuration, export or document those from your Botpress workspace separately.

Never upload passwords, Botpress tokens, API keys, `.env` files, or private customer data.
