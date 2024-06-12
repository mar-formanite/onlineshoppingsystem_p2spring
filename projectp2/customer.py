from cart import Cart
from payment import Payment

class Customer:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.cart = Cart()

    def view_products(self, products):
        print("Available Products:")
        for product in products:
            print(f"ID: {product['id']}, Name: {product['Name']}, Available: {product['Available']}, Price: {product['Price']}")

    def add_to_cart(self, product_id, products):
        for product in products:
            if product['id'] == product_id:
                self.cart.add_to_cart(product)
                return
        print(f"Product with ID '{product_id}' not found.")

    def remove_from_cart(self, product_id):
        self.cart.remove_from_cart(product_id)

    def make_purchase(self):
        total_price = self.cart.get_total_price()
        print(f"Total Price: {total_price}")
        payment = Payment(total_price)
        payment.process_payment()
