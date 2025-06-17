# interface
class PaymentProcessor:
    def pay(self, amount):
        pass

# new payment method
class PayFastAPI:
    def make_payment(self, cost):
        print(f"PayFast processed payment of ${cost}")

# Adapter
class PayFastAdapter(PaymentProcessor):
    def __init__(self, payfast_api):
        self.payfast_api = payfast_api

    def pay(self, amount):
        # Translate the call to the new provider's method
        self.payfast_api.make_payment(amount)

def process_payment(payment_processor, amount):
    payment_processor.pay(amount)

payfast_api = PayFastAPI()
adapter = PayFastAdapter(payfast_api)

process_payment(adapter, 50)  # Your app can use PayFast via adapter!