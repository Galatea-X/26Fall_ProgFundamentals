# cafe.py

cafe_name = "Python Café"
tax_rate = 0.08

menu = {
    "espresso": 3.00,
    "latte": 4.50,
    "cappuccino": 4.25,
    "mocha": 5.00,
    "muffin": 2.50,
    "croissant": 3.25,
}

order = []


def greet(name):
    print(f"Welcome to {cafe_name}, {name}!")


def show_menu(menu):
    print("\n--- MENU ---")
    for item, price in menu.items():
        print(f"{item}: ${price:.2f}")


def show_order(order, menu):
    if not order:
        print("Your order is empty.")
    else:
        print("\n--- YOUR ORDER ---")
        for item in order:
            print(f"{item}: ${menu[item]:.2f}")
        print(f"Items: {len(order)}")


def calculate_subtotal(order, menu):
    total = 0.0
    for item in order:
        total += menu[item]
    return total


def get_discount(subtotal, is_member):
    if is_member and subtotal >= 20:
        return subtotal * 0.15
    elif is_member and subtotal >= 10:
        return subtotal * 0.10
    elif not is_member and subtotal >= 25:
        return subtotal * 0.05
    else:
        return 0.0


def print_receipt(name, order, menu, is_member):
    subtotal = calculate_subtotal(order, menu)
    discount = get_discount(subtotal, is_member)
    after_discount = subtotal - discount
    tax = after_discount * tax_rate
    total = after_discount + tax

    print(f"\n===== {cafe_name} RECEIPT =====")
    print(f"Customer: {name}")
    for item in order:
        print(f"{item}: ${menu[item]:.2f}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Discount: -${discount:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Total: ${total:.2f}")

    if not is_member:
        print("Join our rewards club for bigger discounts next time!")

    print(f"Thanks for visiting, {name}!")


# ========== MAIN PROGRAM ==========

print(f"*** {cafe_name} ***")

name = input("What's your name? ")
greet(name)

member_answer = input("Are you a rewards member? (yes/no) ").lower()
is_member = member_answer == "yes"

while True:
    print("\n1. View menu")
    print("2. Add an item")
    print("3. Remove an item")
    print("4. View my order")
    print("5. Checkout")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        show_menu(menu)

    elif choice == "2":
        item = input("What would you like? ").lower()
        if item in menu:
            quantity = int(input("How many? "))
            if quantity >= 1:
                for _ in range(quantity):
                    order.append(item)
                print(f"Added {quantity} {item} to your order.")
            else:
                print("Quantity must be at least 1.")
        else:
            print(f"Sorry, '{item}' is not on the menu.")

    elif choice == "3":
        item = input("Which item should I remove? ").lower()
        if item in order:
            order.remove(item)
            print(f"Removed one {item}.")
        else:
            print(f"'{item}' is not in your order.")

    elif choice == "4":
        show_order(order, menu)

    elif choice == "5":
        if not order:
            print("Your order is empty. Please add something first.")
        else:
            print_receipt(name, order, menu, is_member)
            break

    else:
        print("Please choose a number from 1 to 5.")
