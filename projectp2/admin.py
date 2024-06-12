from product import Product
class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def add_product(self, product, products):
        products.append(product)
        print(f"Product '{product['Name']}' added successfully.")

    def remove_product(self, product_id, products):
        for product in products:
            if product['id'] == product_id:
                products.remove(product)
                print(f"Product with ID '{product_id}' removed successfully.")
                return
        print(f"Product with ID '{product_id}' not found.")

    def update_product_price(self, product_id, new_price, products):
        for product in products:
            if product['id'] == product_id:
                product['Price'] = new_price
                print(f"Price of product with ID '{product_id}' updated successfully to '{new_price}'.")
                return
        print(f"Product with ID '{product_id}' not found.")
