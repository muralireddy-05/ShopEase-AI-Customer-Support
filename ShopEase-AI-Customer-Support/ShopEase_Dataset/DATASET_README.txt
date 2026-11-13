SHOPEASE DATASET FILES
======================

Files
-----
products.json
    Structured catalogue data in JSON format.

products.csv
    Spreadsheet-friendly version of the product catalogue.

product-catalog.txt
    Human-readable catalogue knowledge document suitable for adding to the
    Botpress knowledge base.

store-policies.txt
    Small support-policy and chatbot-scope knowledge document.

sample-orders.json
    One minimal synthetic/demo order record corresponding to the order
    example used in chatbot testing (SE0001). It contains no personal data.

Source and accuracy
-------------------
The 28 product IDs, names, categories, icons and prices were transcribed from
the product data supplied in the project conversation. Some mobile-phone
storage/colour options and the seven-day return statement were recorded from
the chatbot test responses in the project conversation. Those option and
policy details should be checked against the final ShopEase database and
approved policy before production use.

This is application/catalogue and chatbot knowledge data. It is not a
machine-learning model training dataset.

How to use
----------
1. Keep products.json / products.csv with the project dataset materials.
2. If the website reads products directly from SQLite or an API, the JSON/CSV
   files are reference/export files; they do not automatically update the
   database.
3. Upload product-catalog.txt and store-policies.txt to the correct Botpress
   agent's Knowledge section, then confirm they are processed/indexed.
4. Test the chatbot in its live website channel after publishing the updated
   agent.
5. Only use sample-orders.json if your demo endpoint/database is configured
   with the matching SE0001 record. Otherwise replace it with a safe test
   order exported from your own project database.

Do not include real customer personal information or credentials.
