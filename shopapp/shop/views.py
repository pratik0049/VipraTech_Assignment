from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.core.paginator import Paginator
from decimal import Decimal
import stripe
from .models import Product, Order
from .utils import create_stripe_checkout_session
from .forms import RegisterForm

stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def index(request):
    products = Product.objects.all().order_by('?')  # Randomize product order
    recent_orders = Order.objects.filter(user=request.user).order_by('-created_at')[:3]  # Show only last 3 orders
    
    if request.method == 'POST':
        total = Decimal(0)
        line_items = []
        for product in products:
            qty_key = f'qty_{product.id}'
            qty = int(request.POST.get(qty_key, 0))
            if qty > 0 and qty <= 10:
                subtotal = product.price * qty
                total += subtotal
                line_items.append({
                    'product_id': product.id,
                    'name': product.name,
                    'qty': qty,
                    'price': float(product.price)
                })
        
        if total > 0:
            order = Order.objects.create(user=request.user, total_amount=total, line_items=line_items)
            session = create_stripe_checkout_session(request, order.id, total)
            return redirect(session.url, code=303)
        else:
            messages.error(request, 'Please select at least one item with quantity > 0.')
    
    return render(request, 'index.html', {'products': products, 'recent_orders': recent_orders})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required
def stripe_success(request):
    session_id = request.GET.get('session_id', '').replace('{CHECKOUT_SESSION_ID}', '')
    
    if not session_id:
        messages.error(request, 'No payment session ID provided.')
        return redirect('index')
    
    stripe.api_key = settings.STRIPE_SECRET_KEY
    
    try:
        # Retrieve the session
        session = stripe.checkout.Session.retrieve(session_id)
        
        # Get the order ID from session metadata
        order_id = session.metadata.get('order_id')
        if not order_id:
            messages.error(request, 'Order ID not found in session metadata.')
            return redirect('index')
        
        # Get the order
        try:
            order = Order.objects.get(id=int(order_id))
        except Order.DoesNotExist:
            messages.error(request, 'Order not found.')
            return redirect('index')
        
        # Update order status if payment was successful
        if session.payment_status == 'paid' and order.status != 'paid':
            order.stripe_payment_intent = session.payment_intent
            order.status = 'paid'
            order.save()
            
            messages.success(request, 'Payment successful! Your order has been confirmed.')
            
            # Show success page with order details
            return render(request, 'payment_success.html', {
                'order': order,
                'session': session,
                'payment_intent': session.payment_intent,
                'customer_email': session.customer_details.email if session.customer_details else None,
            })
        elif order.status == 'paid':
            messages.info(request, 'This order has already been processed.')
            return render(request, 'payment_success.html', {
                'order': order,
                'session': session,
                'payment_intent': session.payment_intent,
                'customer_email': session.customer_details.email if session.customer_details else None,
            })
        else:
            messages.warning(request, f'Payment not completed. Status: {session.payment_status}')
            return redirect('index')
            
    except stripe.error.StripeError as e:
        messages.error(request, f'Stripe error: {str(e)}')
        return redirect('index')
    except Exception as e:
        messages.error(request, f'An error occurred: {str(e)}')
        return redirect('index')

@login_required
def order_history(request):
    # Get user's orders and annotate with user-specific order number
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    
    # Add user_order_number to each order
    for index, order in enumerate(orders):
        order.user_order_number = orders.count() - index
    
    paginator = Paginator(orders, 10)  # Show 10 orders per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'order_history.html', {'page_obj': page_obj})

@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'order_details.html', {'order': order})

@login_required
def complete_payment(request, order_id):
    if request.method == 'POST':
        order = get_object_or_404(Order, id=order_id, user=request.user, status='pending')
        session = create_stripe_checkout_session(request, order.id, order.total_amount)
        return redirect(session.url, code=303)
    return redirect('order_history')