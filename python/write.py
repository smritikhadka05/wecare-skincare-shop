import datetime

def generate_invoice(customer, selected_products, total_price):
    now = datetime.datetime.now()
    date_str = str(now).replace(":", "-").replace(" ", "_")
    filename = "invoice_" + customer + "_" + date_str + ".txt"

    with open(filename, 'w') as invoice:
        invoice.write("Customer: " + customer + "\n")
        invoice.write("Date: " + str(now) + "\n\n")
        invoice.write("Purchased Items:\n")
        invoice.write("-" * 60 + "\n")
        invoice.write("Product       Brand         Qty  Free  TotalQty  Subtotal\n")
        invoice.write("-" * 60 + "\n")
        for product, qty in selected_products:
            free = qty // 3
            total = qty + free
            subtotal = qty * (product[3] * 2)
            invoice.write(f"{product[0]:13}{product[1]:13}{qty:<5}{free:<6}{total:<9}Rs.{subtotal:.2f}\n")
        invoice.write("-" * 60 + "\n")
        invoice.write("Total Bill: Rs." + str(round(total_price, 2)) + "\n")

    return filename

def generate_restock_note(vendor, product, add_qty, new_cost):
    now = datetime.datetime.now()
    date_str = str(now).replace(":", "-").replace(" ", "_")
    filename = "restock_" + vendor + "_" + date_str + ".txt"
    total_cost = add_qty * new_cost
    with open(filename, 'w') as f:
        f.write("Vendor: " + vendor + "\n")
        f.write("Date: " + str(now) + "\n")
        f.write("Product: " + product[0] + "\n")
        f.write("Brand: " + product[1] + "\n")
        f.write("Added Quantity: " + str(add_qty) + "\n")
        f.write("New Cost Price: Rs." + str(new_cost) + "\n")
        f.write("Total Cost: Rs." + str(round(total_cost, 2)) + "\n")
    return filename
