import stripe
from django.conf import settings

def create_stripe_checkout_session(request, order_id, total):
    return stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {'name': 'Order Total'},
                'unit_amount': int(total * 100),
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri(f'/stripe-success/') + '?session_id={CHECKOUT_SESSION_ID}',
        cancel_url=request.build_absolute_uri('/'),
        metadata={'order_id': str(order_id)},
    )