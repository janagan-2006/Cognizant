class Razorpay:

    def make_payment(self):
        print("Razorpay Payment")

class PaymentAdapter:

    def __init__(self, razorpay):
        self.razorpay = razorpay

    def pay(self):
        self.razorpay.make_payment()

payment = PaymentAdapter(Razorpay())

payment.pay()