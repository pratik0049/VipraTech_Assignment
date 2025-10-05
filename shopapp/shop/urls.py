from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('stripe-success/', views.stripe_success, name='stripe_success'),
    path('success/', views.stripe_success, name='payment_success'),  # Alternative URL pattern
    path('orders/', views.order_history, name='order_history'),
    path('orders/<int:order_id>/', views.order_detail, name='order_detail'),
    path('orders/<int:order_id>/complete-payment/', views.complete_payment, name='complete_payment'),
]
