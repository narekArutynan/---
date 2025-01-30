import stripe
import os

stripe.api_key = os.getenv('STRIPE_SECRET_KEY')

def create_payment_intent(amount: int, currency: str = 'usd'):
    return stripe.PaymentIntent.create(
        amount=amount,
        currency=currency
    )
