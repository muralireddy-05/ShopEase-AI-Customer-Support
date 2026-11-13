SHOPEASE - ONLINE SHOPPING WEBSITE WITH AI CUSTOMER-SUPPORT CHATBOT
======================================================================


Project documentation / ReadMe
Version: Student project submission
Last updated: 06 November 2026


1. PROJECT OVERVIEW
-------------------
ShopEase is an online shopping web application developed using Python and
HTML/CSS/JavaScript, with a database for storing application data. The project
also includes an AI customer-support chatbot built and configured using
Botpress.


The website presents product categories and product listings, and includes
pages/features for the home page, products, login, cart, orders, FAQ and
contact/support. The product catalogue includes electronics, fashion, beauty,
accessories, mobile phones, watches, footwear and home accessories.


The Botpress assistant is intended to answer ShopEase-related questions,
including product prices and details, order information, and store policies.
A knowledge document (for example, product-catalog.txt) is added to the
Botpress agent so that answers can be grounded in ShopEase project information.


Live website:
https://muralireddy.pythonanywhere.com/




2. TECHNOLOGIES USED
--------------------
- Python: backend application logic.
- Flask: web framework, if used by the supplied app.py.
- SQLite: local database (the project directory previously contained
  shopease.db).
- HTML: website page structure.
- CSS: page styling and responsive layout.
- JavaScript: client-side interactions.
- PythonAnywhere: hosting/deployment platform for the website.
- Botpress: AI customer-support chatbot and knowledge-base management.


3. PROJECT FILE STRUCTURE
-------------------------
The project files previously identified in the ShopEase application are:


Shopease/
|
|-- app.py                 Python web application / server entry point
|-- database.py            Database-related functions
|-- shopease.db            SQLite database file (if included in final copy)
|-- index.html             Home page
|-- products.html          Product listing page
|-- cart.html              Shopping cart page
|-- login.html             Login page
|-- orders.html            Orders page
|-- faq.html               Frequently asked questions
|-- contact.html           Contact/support page
|-- style.css              Website styles
|-- script.js              Client-side JavaScript
|-- sitemap.xml            Sitemap
|-- product-catalog.txt    Product knowledge document for the chatbot
|-- requirements.txt       Python dependencies (create/verify this file)
|-- README.txt             This instruction file


4. REQUIREMENTS
---------------
Before running the project, make sure the computer has:


- Python 3 installed.
- pip (Python package installer).
- A web browser.
- Internet access for installing dependencies and accessing Botpress.
- The project source files.


The exact Python package versions must be taken from the final application's
requirements.txt. If requirements.txt is not yet present, inspect app.py and
database.py and create it with the packages actually imported by the project.
Do not add packages that the application does not use.


5. SETUP AND RUN THE WEBSITE LOCALLY
------------------------------------
Step 1: Download and extract the project
- Copy the submitted ShopEase project folder to your computer.
- Extract the ZIP file, if the project was submitted as a ZIP.
- Open a terminal or command prompt in the project folder (the folder
  containing app.py).


Step 2: Create a virtual environment (recommended)


Windows:
    py -m venv venv
    venv\Scripts\activate


macOS / Linux:
    python3 -m venv venv
    source venv/bin/activate


Step 3: Install Python dependencies


If requirements.txt is included:
    python -m pip install --upgrade pip
    pip install -r requirements.txt


If requirements.txt is not included, inspect the imports in app.py and
database.py and install the required packages before proceeding. For example,
if the application imports Flask and Flask is not installed:
    pip install Flask


The example above is not a complete dependency list. Use the actual
requirements of the submitted code.


Step 4: Check database setup
- Confirm whether shopease.db is included in the submission.
- If it is included, keep it in the location expected by database.py.
- If the database is not included, inspect database.py for the database
  initialization function or table-creation commands and run the project's
  initialization procedure.
- Do not create a blank database manually if the application expects specific
  tables or sample records.
- If the project uses a different database path or database engine, follow
  the settings in database.py.


Step 5: Start the application


From the project folder, try:
    python app.py


If your system uses python3:
    python3 app.py


Use the local address and port printed in the terminal. For a typical Flask
development server this may be:
http://127.0.0.1:5000/


The exact command and URL depend on the run configuration in app.py. If the
application does not start, read the error message and check the configuration
and installed dependencies. Do not assume the example port is correct.


Step 6: Open and test the website
- Open the local URL in a browser.
- Visit the Home and Products pages.
- Check that product cards and prices appear.
- Test the cart and login/order pages according to the functionality actually
  implemented in the submitted version.
- Check FAQ and Contact pages.
- Confirm that the browser developer console and terminal do not show errors.


6. DEPLOYMENT ON PYTHONANYWHERE
-------------------------------
The project website was hosted on PythonAnywhere.


Live website:
https://muralireddy.pythonanywhere.com/


To maintain or redeploy the project:
1. Sign in to the PythonAnywhere account that owns the application.
2. Open the relevant project files and confirm that the latest source files
   have been uploaded.
3. Check the Web tab and confirm the web application configuration points to
   the correct project directory and WSGI configuration.
4. Check the virtual environment and install the dependencies listed in the
   final requirements.txt into that environment.
5. Confirm that the WSGI file imports the correct Flask application object
   from app.py. The exact import statement depends on the variable name used
   in app.py.
6. Check the configured working directory and any database/file paths.
7. Review the PythonAnywhere error log if the website does not load.
8. Reload the web application from the PythonAnywhere Web tab after making
   server-side changes.
9. Open the live URL in a browser and test the main pages.


Do not upload passwords, secret keys, API tokens, or other credentials in the
submission. Configure secrets privately in the hosting environment or a
local environment file that is excluded from the submitted ZIP.


7. DATASET / PRODUCT CATALOGUE
------------------------------
The project uses a small ShopEase product catalogue. The catalogue information
available during development included the following products and prices:


ID   Product                         Category              Price (INR)
1    Wireless Headphones             Electronics            1,499
2    Smart Watch                     Electronics            1,999
3    Bluetooth Speaker               Electronics            1,299
4    Wireless Mouse                  Electronics              699
5    Running Shoes                   Fashion                2,499
6    Premium T-Shirt                 Fashion                  799
7    Skin Care Set                   Beauty                 1,199
8    Urban Backpack                  Accessories               999
9    iPhone 16                       Mobile Phones          69,999
10   Samsung Galaxy S25              Mobile Phones          74,999
11   OnePlus 13                      Mobile Phones          64,999
12   Smart LED TV 43 inch            Electronics            29,999
13   Wireless Earbuds Pro             Electronics             2,499
14   Gaming Keyboard                 Electronics             1,799
15   Power Bank 20000mAh             Electronics             1,499
16   Tablet 10 inch                  Electronics             12,999
17   Casual Shirt                    Fashion                1,299
18   Slim Fit Jeans                  Fashion                1,799
19   Hoodie                          Fashion                1,499
20   Smart Watch Pro                 Watches                2,999
21   Classic Analog Watch            Watches                1,999
22   Casual Sneakers                 Footwear               2,199
23   Smart LED Table Lamp            Home Accessories          999
24   Wall Clock                      Home Accessories          699
25   Storage Organizer               Home Accessories          599
26   Cushion Set                     Home Accessories          899
27   Desk Organizer                  Home Accessories          499
28   Stainless Steel Water Bottle    Accessories               699


Prices and product availability can change. Treat the live application
database/catalogue as the source of truth if it differs from this list.


Dataset files to include in the final submission, if present in the project:
- products.json: structured product records, if this file is created/used.
- product-catalog.txt: readable product information supplied to Botpress.
- sample-orders.json: sample order records, only if the project uses/provides it.


Do not claim that a dataset file exists unless it is actually included in the
submitted project folder. If the product records are stored only in SQLite,
include the database file or provide a safe database export, as permitted by
your faculty.


8. BOTPRESS CHATBOT SETUP AND TESTING
------------------------------------
The ShopEase customer-support assistant was created/configured in Botpress.
Its knowledge source includes ShopEase product and support information, such
as product-catalog.txt.


To review or configure the chatbot:
1. Sign in to the Botpress workspace used for this project.
2. Open the ShopEase bot/agent.
3. Open its Knowledge section (the exact label may vary with the Botpress UI).
4. Confirm that the relevant ShopEase knowledge document, such as
   product-catalog.txt, is present and processed/indexed.
5. Review the agent instructions so that the assistant answers questions
   about ShopEase rather than unrelated general topics.
6. Open the bot's test/chat panel or use the configured webchat channel to
   test the assistant.
7. If the website contains an embedded Botpress webchat, confirm that the
   integration code/configuration in the website uses the correct bot and
   deployment identifiers. Never publish those identifiers as secrets if
   they are private credentials.


Suggested chatbot test questions:
- What is the price of iPhone 16?
- What is the price of Samsung Galaxy S25?
- What colors are available for OnePlus 13?
- What is the price of Wireless Headphones?
- What is your return policy?
- What is the status of order SE0001? (Use only if this sample order exists.)
- Who is the Prime Minister of India?


Expected behavior:
- The bot should answer ShopEase product and policy questions using the
  configured knowledge.
- For an order-specific request, it should ask for the required order details
  or return only information available in the configured order data/system.
- For unrelated general questions, the configured assistant may politely
  explain that it supports ShopEase-related queries only.


Important:
- Preview/testing inside Botpress and the live website channel may be separate.
  A successful preview test does not by itself prove that the live website
  chatbot is updated.
- After changing knowledge or bot configuration, follow the current Botpress
  publish/deploy procedure for the channel used by this project.
- Verify the live website chatbot in a separate browser session after updating.
- Botpress menus and deployment steps may change over time; use the current
  Botpress interface and the configuration saved in the project.


9. TESTING CHECKLIST
--------------------
Website:
[ ] Website starts without Python errors.
[ ] Home page opens.
[ ] Products page displays the expected catalogue.
[ ] Product categories/navigation work as implemented.
[ ] Add-to-cart action works, if implemented.
[ ] Cart page opens and displays cart contents, if implemented.
[ ] Login/order pages behave as implemented.
[ ] FAQ and Contact pages open.
[ ] Website works at the PythonAnywhere live URL.


Chatbot:
[ ] Botpress agent opens in the correct workspace.
[ ] ShopEase knowledge document is present and indexed.
[ ] Product price questions return the expected catalogue information.
[ ] Product detail questions return supported information.
[ ] Return-policy questions return the configured policy.
[ ] Order questions do not expose information without the required details.
[ ] Unrelated questions are handled according to the agent instructions.
[ ] The live website chat channel is tested separately from Botpress preview.


10. TROUBLESHOOTING
-------------------
Problem: 'python' or 'pip' is not recognized.
Solution: Install Python, enable the PATH option on Windows if applicable,
and reopen the terminal. Try using python3 or py instead.


Problem: ModuleNotFoundError when starting app.py.
Solution: Activate the project's virtual environment and install the
dependencies from requirements.txt. Confirm that the correct interpreter is
being used.


Problem: Database/table not found.
Solution: Check the database path and initialization logic in database.py.
Make sure the database file is in the expected location and that required
tables have been created.


Problem: Website does not open locally.
Solution: Check the terminal output, the host/port configured in app.py, and
whether another process is using the same port.


Problem: PythonAnywhere website shows an error.
Solution: Check the PythonAnywhere error log, WSGI import path, working
directory, virtual environment, dependencies and database path. Reload the
web app after correcting the issue.


Problem: Chatbot does not know a product or gives an outdated answer.
Solution: Update the source knowledge document, confirm that it is uploaded
and indexed in the correct Botpress agent, and test again. Then publish/update
the relevant channel and verify the live website chat.


Problem: Bot works in preview but not on the website.
Solution: Check that the website's webchat integration points to the correct
Botpress bot/channel and that the current bot version has been published or
deployed to that channel.


11. SECURITY AND SUBMISSION NOTES
---------------------------------
- Never include account passwords, API tokens, private keys, or personal
  credentials in README.txt, source files, screenshots, or the ZIP submission.
- If the project requires a secret key or API credential, provide a placeholder
  in the documentation and explain that the evaluator must configure their own
  authorized value.
- Do not include real customer personal information in sample datasets.
- Use only dummy/test customer and order records in the submitted dataset.
- Keep the database and source files consistent with the version described in
  the project report and presentation.


12. PROJECT EXECUTION SUMMARY
-----------------------------
To run the project, the evaluator should:
1. Extract the ShopEase source folder.
2. Install Python and the dependencies listed in requirements.txt.
3. Configure or initialize the database as described in database.py.
4. Run the application using the actual entry point in app.py.
5. Open the local URL printed by the application.
6. Sign in to the authorized Botpress workspace, verify the ShopEase knowledge
   document and test the chatbot, or use the configured live website chat.
7. Use the testing checklist above to verify the result.