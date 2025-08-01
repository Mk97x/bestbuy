class Product:

    def __init__(self, name, price, quantity): #
        if type(name) != str:
            raise TypeError("Name must be a string")
        if type(price) != float and type(price) != int: # input could be an int i guess
            raise TypeError("Price must be a number (float or int)")
        if type(quantity) != int:
            raise TypeError("Quantity must be an integer")
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        
        
    def is_active(self):
        return self.active

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.quantity = quantity
        return self.quantity

    def activate(self):
        self.active = True
    
    def deactivate(self):
        self.active = False

    def show(self):
        status = "Active" if self.active else "Inactive"
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Status: {status}")

    def buy(self, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        if not self.active:
            raise Exception("Product is not active")
        if self.quantity < quantity:
            raise Exception("Not enough items in stock")
        
        self.quantity -= quantity

        if self.quantity == 0:
            self.deactivate() 

        total = quantity * self.price
        return total
        
        

bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = Product("MacBook Air M2", price=1450, quantity=100)

print(bose.buy(50))
print(mac.buy(100))
print(mac.is_active())

bose.show()
mac.show()

bose.set_quantity(1000)
bose.show()