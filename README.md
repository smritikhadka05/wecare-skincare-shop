# wecare-skincare-shop
A command-line inventory and billing system for a skincare shop. Supports 
viewing products, selling items (with a "buy 3, get 1 free" promotion), 
restocking inventory, and auto-generates invoices and restock notes.

## Files
- `main.py` – runs the program
- `read.py` – loads products from `products.txt`
- `write.py` – generates invoice and restock note files
- `operation.py` – displays the product table and saves changes
- `products.txt` – product data (name, brand, quantity, cost, country)

## How to Run
1. Make sure all files are in the same folder.
2. Run:
   python main.py
3. Follow the on-screen menu:
   - `1` – Show products
   - `2` – Sell products
   - `3` – Restock products
   - `4` – Exit (saves changes to `products.txt`)

## Notes
- Selling a product generates an `invoice_<customer>_<date>.txt` file.
- Restocking generates a `restock_<vendor>_<date>.txt` file.
- Prices shown are double the cost price.
