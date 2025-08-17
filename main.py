import products
import store

def initialize_store():
    """Initial setup of the store"""
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250)
               ]
    return store.Store(product_list)

def list_all_products(best_buy):
    """Helper function to be called in start function to list all active products in store"""
    print("\n--- Available products ---")
    products = best_buy.get_all_products()
    if not products:
        print("No active procuts in store")
    for i, product in enumerate(products, start=1):
        print(f"{i}. {product.name:25}, Price: {product.price:5} dollars, Quantity: {product.get_quantity():5}")
    print()

def print_menu():
    """Prints the main menu."""
    print("\n----- Welcome to Best Buy Store -----")
    print("1. List all products in store")
    print("2. Show total quantity in store")
    print("3. Make an order")
    print("4. Quit")

def show_shopping_list(shopping_list): 
    """Displays the current shopping list"""
    if not shopping_list:
        print("Your shopping list is empty")
        return
    print("\n--- Your Shopping List ---")
    total_items = 0
    for product, quantity in shopping_list:
        print(f"{quantity} x {product.name}")
        total_items += quantity
    print(f"Total items: {total_items}")
    print("-------------------------\n")

def make_order(best_buy):
    """
    Handles the order process: lets user select products and quantities.
    :param best_buy: Store instance
    """
    shopping_list = []
    products_list = best_buy.get_all_products()

    if not products_list:
        print("There are no products available for ordering")
        return

    while True:
        try:
            print("Which item would you like to order?")
            list_all_products(best_buy) # used list function, formatting is also there now

            choice = input("Enter a product number or 'done' to finish or v to view you shopping list\n>> ")
            if choice.lower() == "done":
                break
            if choice.lower() =="v":
                show_shopping_list(shopping_list)        
            product_index = int(choice) - 1
            if product_index < 0 or product_index >= len(products_list):
                print("Invalid product number, try again")
                continue
        
            product = products_list[product_index]
            quantity = int(input(f"How many {product.name} would you like to order?\n>> "))
            if quantity <= 0:
                print("Quantity must be greater than 0")
                continue
            if quantity > product.get_quantity():
                print("We do not have that many in stock, please select a number lower or equal to our stock")
                continue
            #added this block for display remaining stock without setting product qty yet
            remaining_stock = product.get_quantity() - quantity
            print(f"Remaining stock for {product.name}: {remaining_stock}")

            shopping_list.append((product, quantity))
            print(f"Added {quantity} x {product.name} to your order")
                    
        except ValueError:
            print("Please enter a valid number")

    if shopping_list:
        total_cost = best_buy.order(shopping_list)
        print(f"Thank you for your order. Total cost: {total_cost} dollars")
    else:
        print("No items ordered")


def start(best_buy):
    """Main loop with user interface"""
    while True:
        print_menu()
        try:
            choice = int(input("What do you wanna do? (Choose between options 1-4)\n>> "))
            if choice == 1:
                list_all_products(best_buy)
            elif choice == 2:
                total = best_buy.get_total_quantity()
                print(f"Total quantity in store: {total}")

            elif choice == 3:
                make_order(best_buy)

            elif choice == 4:
                print("Thank you for visiting our shop")
                break

            else:
                print("Invalid choice, choice must be in range 1-4")
        except ValueError:
            print("Please enter a valid number")
            continue

def main():
    """Main function to initialize the store and start the user interface."""
    best_buy = initialize_store()
    start(best_buy)


if __name__ == "__main__":
    main()