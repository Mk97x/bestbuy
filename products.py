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
        """Getter function for active. Returns True if the product is active, otherwise False."""
        return self.active

    def get_quantity(self):
        """Getter function for quantity. Returns the quantity (int)."""
        return self.quantity

    def set_quantity(self, quantity):
        """Setter function for quantity. If quantity reaches 0, deactivates the product."""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.quantity = quantity
        return self.quantity

    def activate(self):
        """Activates the product."""
        self.active = True
    
    def deactivate(self):
        """Deactivates the product."""
        self.active = False

    def show(self):
        """Prints a string that represents the product, for example:"""
        status = "Active" if self.active else "Inactive"
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Status: {status}")

    def buy(self, quantity):
        """Buys a given quantity of the product. Returns the total price (float) of the purchase. Updates the quantity of the product. Handles errors."""
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        if not self.active:
            raise Exception("Product is not active")
        if self.quantity < quantity:
            raise Exception("Not enough items in stock")
        
        self.set_quantity(self.quantity - quantity)

        if self.quantity == 0:
            self.deactivate() 

        total = quantity * self.price
        return total
        
        
