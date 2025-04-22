products = [("Хлеб", 40), ("Молоко", 60), ("Яблоки", 100)]
for name, price in products:
    print(f"Товар: {name}, Цена: {price}")

def print_cheap_products(products):
    name, price = product
    if price < 80:
        print(name)
