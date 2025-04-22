products = [("Хлеб", 40,17), ("Молоко", 60,44), ("Яблоки", 100,77)]
for product in products:
    name, price, quantity = product
    print(f"Товар: {name}, Цена: {price}, Количество на складе: {quantity}")

def print_cheap_products(products):
    name, price = product
    if price < 80:
        print(name)
        
def compute():     
    for name, price, quantity in products:
        result = price * quantity
        print(f"{name} — всего на {result} рублей")
compute()

max_product = None
max_value = 0
for name, price, quantity in products:
        total = price * quantity
        if total > max_value:
            max_value = total
            max_product = name
print(f"Самый ценный товар: {max_product} — {max_value} рублей")
