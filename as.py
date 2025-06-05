class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def show_order(self):
        print("\nYour Order:")
        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item.name} - ${item.price}")
        print(f"Total: ${self.total()}")

    def total(self):
        return sum(item.price for item in self.items)


# Coffee Menu
menu = {
    "Espresso": 3.0,
    "Latte": 4.0,
    "Cappuccino": 4.5
}

# Create an order
order = Order()

print("Welcome to the Coffee Shop!")
print("Menu:")
for i, (name, price) in enumerate(menu.items(), 1):
    print(f"{i}. {name} - ${price}")

while True:
    choice = input("\nEnter coffee name to add to order (or type 'done' to finish): ").strip()
    if choice.lower() == "done":
        break
    elif choice in menu:
        item = Item(choice, menu[choice])
        order.add_item(item)
        print(f"{choice} added to your order.")
    else:
        print("Invalid selection, please try again.")

order.show_order()
