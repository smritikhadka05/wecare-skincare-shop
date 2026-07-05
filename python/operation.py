def show_products(products):
    print("No.  Product" + " " * 10 + "Brand" + " " * 8 + "Stock" + " " * 6 + "Price" + " " * 8 + "Country")
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
        i = i + 1
    print("-" * 80)

def save_products(products, filename="products.txt"):
    with open(filename, 'w') as file:
        file.write("Product,Brand,Quantity,Cost Price,Country\n")
        for p in products:
            line = p[0] + "," + p[1] + "," + str(p[2]) + "," + str(p[3]) + "," + p[4] + "\n"
            file.write(line)
