class Payment:
    def __init__(self, total_amount):
        self.total_amount = total_amount

    def process_payment(self):
        payment_method = input("Select payment method (cash/card): ").lower()
        if payment_method == 'cash':
            self.process_cash_payment()
        elif payment_method == 'card':
            self.process_card_payment()
        else:
            print("Invalid payment method. Please choose 'cash' or 'card'.")
            self.process_payment()

    def process_cash_payment(self):
        print(f"Processing cash payment of {self.total_amount}...")
        print("Payment successful.")

    def process_card_payment(self):
        card_number = input("Enter card number: ")
        cvv = input("Enter CVV: ")
        print(f"Processing card payment of {self.total_amount}...")
        print("Payment successful.")
