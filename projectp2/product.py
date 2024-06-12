class Product:
    def __init__(self, product_id, name, available, price, original_price):
        self.id = product_id
        self.name = name
        self.available = available
        self.price = price
        self.original_price = original_price

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Available: {self.available}, Price: {self.price}, Original Price: {self.original_price}"
