from admin import Admin
from customer import Customer
from product import Product
import json 

def register_customer():
    username = input("Enter username: ")
    password = input("Enter password: ")
    customer_data = {"username": username, "password": password}
    with open("customers.json", "a") as file:
        json.dump(customer_data, file)
        file.write("\n") 
def login_customer():
    customers = []
    with open("customers.json", "r") as file:
        for line in file:
            customers.append(json.loads(line)) 
    username = input("Enter username: ")
    password = input("Enter password: ")
    for customer in customers:
        if customer["username"] == username and customer["password"] == password:
            print("Login successful!")
            return True
    print("Invalid username or password.")
    return False

def admin_login_window():
    print("=====================")
    print("1. Display Menu")
    print("2. Add Product")
    print("3. Remove Product")
    print("4. Update Product Price")
    print("5. Products Goods Available")
    print("6. Total Income")
    print("7. Logout")
    print("=====================")

def admin_display_menu_window(products):
    print("Id\tName\tAvailable\tPrice\tOriginal Price")
    print("====================================================")
    for product in products:
        print(f"{product['id']}\t{product['Name']}\t{product['Available']}\t\t{product['Price']}\t{product['Original_Price']}")

def available_products(products):
    total = 0
    print("\n")
    for product in products:
        print(f"{product['Name']} = {product['Available']}")
        total += product['Available']
    print("\nTotal available goods is: ", total)

def total_income(products):
    total = 0
    for product in products:
        total += ((product['Available'] * product['Price']) - (product['Available'] * product['Original_Price']))
    print("\nTotal income is: ", total)

def admin_options(admin, products):
    while True:
        admin_login_window()
        choice = int(input("Please enter your choice: "))
        if choice == 1:
            admin_display_menu_window(products)
        elif choice == 2:
            product_id = int(input("Enter product ID: "))
            product_name = input("Enter product name: ")
            available = int(input("Enter available quantity: "))
            price = float(input("Enter price: "))
            original_price = float(input("Enter original price: "))
            new_product = {
                "id": product_id,
                "Name": product_name,
                "Available": available,
                "Price": price,
                "Original_Price": original_price
            }
            admin.add_product(new_product, products)
        elif choice == 3:
            product_id = int(input("Enter product ID to remove: "))
            admin.remove_product(product_id, products)
        elif choice == 4:
            product_id = int(input("Enter product ID: "))
            new_price = float(input("Enter new price: "))
            admin.update_product_price(product_id, new_price, products)
        elif choice == 5:
            available_products(products)
        elif choice == 6:
            total_income(products)
        elif choice == 7:
            break
        else:
            print("Invalid choice. Please try again.")

def user_login_window():
    print("=====================")
    print("1. View Products")
    print("2. Add Product to Cart")
    print("3. Remove Product from Cart")
    print("4. View Cart")
    print("5. Make Purchase")
    print("6. Logout")
    print("=====================")

def user_options(customer, products):
    while True:
        user_login_window()
        choice = int(input("Please enter your choice: "))
        if choice == 1:
            customer.view_products(products)
        elif choice == 2:
            product_id = int(input("Enter product ID to add to cart: "))
            customer.add_to_cart(product_id, products)
        elif choice == 3:
            product_id = int(input("Enter product ID to remove from cart: "))
            customer.remove_from_cart(product_id)
        elif choice == 4:
            print(customer.cart) 
        elif choice == 5:
            customer.make_purchase()
        elif choice == 6:
            break
        else:
            print("Invalid choice. Please try again.")
def login():
    print("Welcome to Zakriaish!")
    products = [
        {"id": 1001, "Name": "Hydrating Cleanser", "Available": 100, "Price": 1500, "Original_Price": 1400},
        {"id": 1002, "Name": "Vitamin C Serum", "Available": 100, "Price": 2500, "Original_Price": 2400},
        {"id": 1003, "Name": "Moisturizing Cream", "Available": 100, "Price": 2000, "Original_Price": 1900},
        {"id": 1004, "Name": "Sunscreen SPF 50", "Available": 100, "Price": 1800, "Original_Price": 1700},
        {"id": 1005, "Name": "Exfoliating Scrub", "Available": 100, "Price": 1200, "Original_Price": 1100},
        {"id": 1006, "Name": "Anti-aging Cream", "Available": 100, "Price": 3000, "Original_Price": 2900},
        {"id": 1007, "Name": "Eye Cream", "Available": 100, "Price": 2200, "Original_Price": 2100},
        {"id": 1008, "Name": "Lip Balm", "Available": 100, "Price": 500, "Original_Price": 450},
        {"id": 1009, "Name": "Face Mask", "Available": 100, "Price": 800, "Original_Price": 750},
        {"id": 1010, "Name": "Toner", "Available": 100, "Price": 1000, "Original_Price": 950}
    ]

    
    user_type = input("Login as Admin or Customer? (Type A for Admin, C for Customer): ").strip().lower()
    if user_type == 'a':
        password = input("Enter admin password: ")
        if password == "admin_pass":
            admin = Admin("admin", password)
            admin_options(admin, products)
        else:
            print("Invalid password.")
    elif user_type == 'c':
        user_choice = input("Do you want to login or register? (Type L for Login, R for Register): ").strip().lower()
        if user_choice == 'r':
            register_customer()
        elif user_choice == 'l':
            while not login_customer():
                print("Please try again.")
            customer = Customer("customer", "password") 
            user_options(customer, products)
        else:
            print("Invalid option.")
            return
if __name__ == "__main__":
    login()
