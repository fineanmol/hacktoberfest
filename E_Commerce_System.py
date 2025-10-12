import csv
from datetime import datetime

FILENAME = "orders.csv"

products = {
    1: {"name": "Laptop", "price": 55000},
    2: {"name": "Smartphone", "price": 25000},
    3: {"name": "Headphones", "price": 1500},
    4: {"name": "Smartwatch", "price": 5000},
    5: {"name": "Keyboard", "price": 800}
}

cart = []

def save_order(order_items, total):
    with open(FILENAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        for item in order_items:
            writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), item['name'], item['price'], item['qty'], total])

def show_products():
    print("\n===== Product List =====")
    for pid, info in products.items():
        print(f"{pid}. {info['name']} - ₹{info['price']}")

def add_to_cart():
    show_products()
    pid = int(input("Enter product ID to add: "))
    if pid in products:
        qty = int(input("Enter quantity: "))
        cart.append({"name": products[pid]["name"], "price": products[pid]["price"], "qty": qty})
        print("Added to cart!")
    else:
        print("Invalid product ID!")

def view_cart():
    if not cart:
        print("Cart is empty!")
        return
    total = 0
    print("\n===== Your Cart =====")
    for item in cart:
        subtotal = item['price'] * item['qty']
        total += subtotal
        print(f"{item['name']} x {item['qty']} = ₹{subtotal}")
    print(f"Total Amount: ₹{total}")

def checkout():
    if not cart:
        print("Cart is empty!")
        return
    total = sum(item['price'] * item['qty'] for item in cart)
    print(f"\nTotal Bill: ₹{total}")
    confirm = input("Confirm checkout? (Y/N): ").upper()
    if confirm == "Y":
        save_order(cart, total)
        cart.clear()
        print("Order placed successfully!")
    else:
        print("Checkout cancelled.")

def main():
    while True:
        print("\n===== E-Commerce System =====")
        print("1. View Products")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Exit")
        choice = input("Enter choice (1-5): ")
        if choice == "1":
            show_products()
        elif choice == "2":
            add_to_cart()
        elif choice == "3":
            view_cart()
        elif choice == "4":
            checkout()
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
