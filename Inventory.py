import prettytable

products = [
    {"Name": "milk", "Price": 2, "Quantity": 3500},
    {"Name": "oil", "Price": 4, "Quantity": 2500},
    {"Name": "chipcy", "Price": 3, "Quantity": 3700},
    {"Name": "chocolate", "Price": 6, "Quantity": 4000}
]

def find_product(name):
    return next((p for p in products if p["Name"] == name), None)

def stationary_store():
    table = prettytable.PrettyTable(["Name", "Price $", "Available Quantity"])
    for p in products:
        table.add_row([p["Name"], p["Price"], p["Quantity"]])
    print(table)

def calculate_price(product_name, quantity):
    product = find_product(product_name)
    if not product:
        return 0, 0
    price = product["Price"]
    if quantity >= 1250:
        discount = 0.25 * price * quantity
    else:
        quantity_sale = [250, 500, 750, 1000]
        count = sum(1 for m in quantity_sale if m <= quantity)
        discount = count * 0.05 * price * quantity
    return price * quantity, discount

def update_store(product_name, quantity):
    product = find_product(product_name)
    if product:
        product["Quantity"] -= quantity

def get_request(product_name):
    product = find_product(product_name)
    if not product:
        print("Product not found.")
        return None
    available = product["Quantity"]
    if available == 0:
        print("Out of stock.")
        return None
    while True:
        try:
            quantity = int(input(f"Enter quantity (max {available}): "))
            if 0 < quantity <= available:
                update_store(product_name, quantity)
                return quantity
            else:
                print("Invalid quantity. Try again.")
        except ValueError:
            print("Please enter a number.")

def delivery_pickup(total):
    while True:
        choice = input("Delivery or pickup? ").lower()
        if choice == "delivery":
            return total + 200
        elif choice == "pickup":
            return total + 50
        else:
            print("Invalid option.")

def currency_conversion(total):
    rates = {"usd": 1, "eur": 0.92, "egp": 30.90}
    while True:
        currency = input("Choose currency (USD, EUR, EGP): ").lower()
        if currency in rates:
            return total * rates[currency], currency
        else:
            print("Invalid currency.")


stationary_store()
total = 0
discount = 0

while True:
    product = input("What do you need? ").lower()
    quantity = get_request(product)
    if quantity is None:
        continue
    item_total, item_discount = calculate_price(product, quantity)
    total += item_total
    discount += item_discount
    if input("Add more items? (yes/no) ").lower() != "yes":
        break

final_total = total - discount
print(f"Total: ${total}\nDiscount: ${discount}\nFinal Total: ${final_total}")

final_total = delivery_pickup(final_total)
final_total, currency = currency_conversion(final_total)
print(f"Total in {currency.upper()}: {final_total}")

stationary_store()