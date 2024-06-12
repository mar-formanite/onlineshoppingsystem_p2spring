class Cart:
    def __init__(self):
        self.items = []

    def add_to_cart(self, product):
        self.items.append(product)
        product["Available"] -= 1
        print(f"Added {product['Name']} to the cart.")

    def remove_from_cart(self, product_id):
        for product in self.items:
            if product["id"] == product_id:
                self.items.remove(product)
                product["Available"] += 1
                print(f"Removed {product['Name']} from the cart.")
                return
        print(f"Product with ID {product_id} not found in the cart.")

    def get_total_price(self):
        return sum(product["Price"] for product in self.items)

    def __str__(self):
        if not self.items:
            return "Your cart is empty."
        return "\n".join(str(product) for product in self.items)
