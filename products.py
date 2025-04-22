products = [("Хлеб", 40,17), ("Молоко", 60,44), ("Яблоки", 100,77)]
for product in products:
    name, price, quantity = product
    print(f"Товар: {name}, Цена: {price}, Количество на складе: {quantity}")

def print_cheap_products(products):
    name, price = product
    if price < 80:
        print(name)
