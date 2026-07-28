class Payment:

    def pay(self):
        pass


class UpiPayment(Payment):

    def pay(self):
        print("UPI Payment")


class CardPayment(Payment):

    def pay(self):
        print("Card Payment")

class PaymentFactory:

    @staticmethod
    def create_payment(payment_type):

        if payment_type == "upi":
            return UpiPayment()

        elif payment_type == "card":
            return CardPayment()

        raise ValueError("Invalid payment type")
    
payment = PaymentFactory.create_payment("upi")

payment.pay()