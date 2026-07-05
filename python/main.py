import datetime
from read import read_products
from write import generate_invoice, generate_restock_note
from operation import show_products, save_products

products = read_products()


print("\n=== Welcome to WeCare Skincare Shop ===")
show_products(products)  # Show product list initially

while True:
    print("\nChoose an option (1- Show Products, 2- Sell Products, 3- Restock, 4- Exit):")
    choice = input()

    if choice == "1":
        show_products(products)

    elif choice == "2":
        print("Enter customer's name:")
        customer = input()
        show_products(products)
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

        p[2] = p[2] - total
        total_price = qty * (p[3] * 2)

        filename = generate_invoice(customer, [(p, qty)], total_price)

        print("Invoice saved as", filename)
        print("\n--- Invoice Preview ---")
        with open(filename, 'r') as f:
            print(f.read())
        print("------------------------")

        show_products(products)

    elif choice == "3":
        print("Enter vendor name:")
        vendor = input()
        show_products(products)
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

        p[2] = p[2] + add_qty
        p[3] = new_cost

        filename = generate_restock_note(vendor, p, add_qty, new_cost)

        print("Restock note saved as", filename)
        print("\n--- Restock Note Preview ---")
        with open(filename, 'r') as f:
            print(f.read())
        print("-----------------------------")

        show_products(products)

    elif choice == "4":
        save_products(products)
        print("Changes saved. Exiting program...")
        break

    else:
        print("Please enter a valid option (1-4).")