def read_products(filename="products.txt"):
    products = []
    with open(filename, 'r') as file:
        lines = file.readlines()[1:]  # Skip header
        for line in lines:
            parts = line.strip().split(',')
            if len(parts) == 5:
                name = parts[0]
                brand = parts[1]
                quantity = int(parts[2])
                cost = float(parts[3])
                country = parts[4].strip()
                products.append([name, brand, quantity, cost, country])
    return products
