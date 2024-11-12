## Open/Closed Principle (OCP)

# OCP asserts that software entities (classes, modules, functions) should be open for extension but closed for modification. 
# This means you should be able to add new functionality without altering existing code.

# Importance
# Flexibility: Easily add new features without breaking existing functionality.
# Stability: Reduces the risk of introducing bugs when extending functionality.
# Scalability: Facilitates the growth of the codebase over time.

# Violation Example
# Modifying a class to handle new payment methods:
# Violates OCP: Must modify PaymentProcessor to add new methods

class PaymentProcessor:
    def process_payment(self, payment_type, amount):
        if payment_type == "credit_card":
            self.process_credit_card(amount)
        elif payment_type == "paypal":
            self.process_paypal(amount)

    # Adding a new payment type requires modifying this method
    def process_credit_card(self, amount):
        # Process credit card payment
        pass

    def process_paypal(self, amount):
        # Process PayPal payment
        pass



# OCP-Compliant Example
# Use abstraction to allow extension without modifying existing classes:

from abc import ABC, abstractmethod
# Abstract base class for payment methods

class PaymentMethod(ABC):
    @abstractmethod
    def process(self, amount):
        pass


# Concrete implementation for credit card
class CreditCardPayment(PaymentMethod):
    def process(self, amount):
        # Process credit card payment
        print(f"Processing credit card payment of ${amount}")


# Concrete implementation for PayPal
class PayPalPayment(PaymentMethod):
    def process(self, amount):
        # Process PayPal payment
        print(f"Processing PayPal payment of ${amount}")


# Payment processor using OCP
class PaymentProcessor:

    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method

    def process_payment(self, amount):
        self.payment_method.process(amount)

# Usage
credit_card = CreditCardPayment()
paypal = PayPalPayment()

processor = PaymentProcessor(credit_card)
processor.process_payment(100)

processor = PaymentProcessor(paypal)
processor.process_payment(200)


# Adding a new payment method doesn't require modifying PaymentProcessor
class BitcoinPayment(PaymentMethod):
    def process(self, amount):
        print(f"Processing Bitcoin payment of ${amount}")


bitcoin = BitcoinPayment()
processor = PaymentProcessor(bitcoin)
processor.process_payment(300)


# Benefits:
# Adding `BitcoinPayment` doesn't require changes to `PaymentProcessor`.
# Encourages the use of polymorphism and abstraction.