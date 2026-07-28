from abc import ABC, abstractmethod

class PaymentStrategy(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

class UPI(PaymentStrategy):

    def pay(self, amount):
        print(f"UPI payment: {amount}")

class Card(PaymentStrategy):

    def pay(self, amount):
        print(f"Card payment: {amount}")

class PaymentProcessor:

    def __init__(self, strategy):
        self.strategy = strategy

    def process(self, amount):
        self.strategy.pay(amount)

processor = PaymentProcessor(UPI())
processor.process(1000)