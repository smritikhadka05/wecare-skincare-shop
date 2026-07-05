import datetime

# products from file
file = open("products.txt", 'r')
lines = file.readlines()[1:]  # skip header
products = []

for line in lines:
    parts = line.split(',')
    if len(parts) == 5:
        name = parts[0]
        brand = parts[1]
        quantity = int(parts[2])
        cost = float(parts[3])
        country = parts[4].strip()
        products.append([name, brand, quantity, cost, country])

file.close()

# Function to display product table
def show_products():
    print("\nUpdated Product List:")
    print("No.  Product" + " " * 10 + "Brand" + " " * 8 + "Stock" + " " * 6 + "Price" + " " * 8+ "Country")
    print("-" * 80)
    i = 1
    for product in products:
        name = product[0]
        brand = product[1]
        quantity = product[2]
        price = product[3] * 2
        country = product[4]

        print(str(i).ljust(5) + name + " " * (16 - len(name)) + brand + " " * (15 - len(brand)) +
              str(quantity) + " " * (10 - len(str(quantity))) +
              "Rs." + str(round(price, 2)) + " " * (10 - len(str(round(price, 2)))) +
              country)
        i += 1
    print("-" * 80)

# Show product list at startup
show_products()

# Main program loop
while True:
    print("\n=== Welcome to WeCare Skincare Shop ===")
    print("Choose an option (1- Show, 2- Sell, 3- Restock, 4- Exit):")
    choice = input()

    if choice == "1":
        show_products()

    elif choice == "2":
        print("Enter customer's name:")
        customer = input()
        show_products()
        print("Enter product number to sell:")
        try:
            index = int(input()) - 1
            if index < 0 or index >= len(products):
                print("Invalid product number.")
                continue
            p = products[index]
        except:
            print("Invalid input.")
            continue

        print("Quantity to buy:")
        try:
            qty = int(input())
        except:
            print("Invalid quantity.")
            continue

        if qty <= 0:
            print("Quantity must be a positive number.")
            continue

        free = qty // 3
        total = qty + free

        if total > p[2]:
            print("Not enough stock.")
            continue

        p[2] -= total
        total_price = qty * (p[3] * 2)
        now = datetime.datetime.now()
        date_str = str(now).replace(":", "-").replace(" ", "_")
        filename = "invoice_" + customer + "_" + date_str + ".txt"

        with open(filename, 'w') as invoice:
            invoice.write("Customer: " + customer + "\n")
            invoice.write("Date: " + str(now) + "\n")
            invoice.write("Product: " + p[0] + "\n")
            invoice.write("Brand: " + p[1] + "\n")
            invoice.write("Bought: " + str(qty) + ", Free: " + str(free) + "\n")
            invoice.write("Total Given: " + str(total) + "\n")
            invoice.write("Total Bill: Rs." + str(round(total_price, 2)) + "\n")

        print("Invoice saved as", filename)
        print("\n--- Invoice Preview ---")
        with open(filename, 'r') as f:
            print(f.read())
        print("------------------------")

        show_products()

    elif choice == "3":
        print("Enter vendor name:")
        vendor = input()
        show_products()
        print("Enter product number to restock:")
        try:
            index = int(input()) - 1
            if index < 0 or index >= len(products):
                print("Invalid product number.")
                continue
            p = products[index]
        except:
            print("Invalid input.")
            continue

        print("Enter quantity to add:")
        try:
            add_qty = int(input())
            print("Enter new cost price:")
            new_cost = float(input())
        except:
            print("Invalid input.")
            continue

        if add_qty <= 0 or new_cost <= 0:
            print("Quantity and cost price must be positive numbers.")
            continue

        p[2] += add_qty
        p[3] = new_cost
        total_cost = add_qty * new_cost
        now = datetime.datetime.now()
        date_str = str(now).replace(":", "-").replace(" ", "_")
        filename = "restock_" + vendor + "_" + date_str + ".txt"

        with open(filename, 'w') as restock_file:
            restock_file.write("Vendor: " + vendor + "\n")
            restock_file.write("Date: " + str(now) + "\n")
            restock_file.write("Product: " + p[0] + "\n")
            restock_file.write("Brand: " + p[1] + "\n")
            restock_file.write("Added Quantity: " + str(add_qty) + "\n")
            restock_file.write("New Cost Price: Rs." + str(new_cost) + "\n")
            restock_file.write("Total Cost: Rs." + str(round(total_cost, 2)) + "\n")

        print("Restock note saved as", filename)
        print("\n--- Restock Note Preview ---")
        with open(filename, 'r') as f:
            print(f.read())
        print("-----------------------------")

        show_products()

    elif choice == "4":
        with open("products.txt", 'w') as output:
            output.write("Product,Brand,Quantity,Cost Price,Country\n")
            for p in products:
                output.write(p[0] + "," + p[1] + "," + str(p[2]) + "," + str(p[3]) + "," + p[4] + "\n")
        print("Changes saved. Exiting program...")
        break

    else:
        print("Please enter a valid option (1-4).")