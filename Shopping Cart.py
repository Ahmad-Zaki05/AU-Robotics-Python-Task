class Item:
    def __init__ (self, item_name, price, quantity):
        self.name = item_name
        self.price = price
        self.quantity = quantity

    def print_item (self):
        print (f"Item Name: {self.name}, Price per item : ${self.price}, Quanrity: {self.quantity}")
    
class ShoppingCart:
    def __init__ (self):
        self.items_list = []

    def add_item (self, name, price, quantity):
        item = Item (name, price, quantity)
        self.items_list.append (item)

    def remove_item (self, name):
        found = 0

        for item in self.items_list:
            if item.name == name:
                self.items_list.remove (item)
                found = 1
                break
        if not found:
            print ("The item you want to remove doesn't exist in the shopping cart")

    def calculate_total (self):
        total = 0

        for item in self.items_list:
            total += item.price * item.quantity

        return total

    def display_cart (self):
        for item in self.items_list:
            item.print_item()

cart = ShoppingCart ()

cart.add_item ("watermelon", 2.5, 4)
cart.add_item ("apple", 1.25, 5)
cart.add_item ("banana", 0.8, 10)

print (cart.calculate_total())
cart.display_cart()

cart.remove_item("blueberries")
cart.remove_item("apple")

print (cart.calculate_total())
cart.display_cart()
