from django.core.management.base import BaseCommand
from shop.models import Product

class Command(BaseCommand):
    help = 'Seeds initial products into the database'

    def handle(self, *args, **kwargs):
        # Clear existing products
        Product.objects.all().delete()
        
        # Create new products
        products = [
            # Laptops & Computers
            Product(
                name='MacBook Pro M3',
                price=1499.99,
                description='Latest MacBook Pro with M3 chip, 14-inch display, 16GB RAM.',
                image_url='https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=500'
            ),
            Product(
                name='ASUS ROG Gaming Laptop',
                price=1799.99,
                description='Gaming laptop with RTX 4080, 32GB RAM, 1TB SSD.',
                image_url='https://images.unsplash.com/photo-1603302576837-37561b2e2302?w=500'
            ),
            # Peripherals
            Product(
                name='Logitech MX Master 3',
                price=99.99,
                description='Premium wireless mouse with advanced scrolling and ergonomic design.',
                image_url='https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=500'
            ),
            Product(
                name='Keychron K2 Keyboard',
                price=89.99,
                description='Wireless mechanical keyboard with RGB backlighting.',
                image_url='https://images.unsplash.com/photo-1587829741301-dc798b83add3?w=500'
            ),
            # Displays
            Product(
                name='Dell 27" 4K Monitor',
                price=449.99,
                description='Professional 4K monitor with USB-C connectivity and HDR.',
                image_url='https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=500'
            ),
            Product(
                name='Samsung 49" Ultrawide',
                price=899.99,
                description='Super ultrawide curved gaming monitor, 240Hz.',
                image_url='https://images.unsplash.com/photo-1619953942547-233eab5a70d6?w=500'
            ),
            # Audio
            Product(
                name='Sony WH-1000XM5',
                price=349.99,
                description='Premium noise-cancelling headphones.',
                image_url='https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500'
            ),
            Product(
                name='Bose QuietComfort Earbuds',
                price=279.99,
                description='True wireless noise cancelling earbuds.',
                image_url='https://images.unsplash.com/photo-1590658268037-6bf12165a8df?w=500'
            ),
            # Tablets
            Product(
                name='iPad Pro 12.9"',
                price=1099.99,
                description='Latest iPad Pro with M2 chip, perfect for creatives.',
                image_url='https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=500'
            ),
            Product(
                name='Samsung Galaxy Tab S9',
                price=899.99,
                description='Android tablet with S-Pen and AMOLED display.',
                image_url='https://images.unsplash.com/photo-1589739900268-5c1a01773df1?w=500'
            ),
            # Smart Devices
            Product(
                name='Apple Watch Series 9',
                price=399.99,
                description='Latest Apple Watch with health monitoring.',
                image_url='https://images.unsplash.com/photo-1546868871-7041f2a55e12?w=500'
            ),
            Product(
                name='DJI Mini 3 Pro Drone',
                price=749.99,
                description='Compact drone with 4K camera and obstacle avoidance.',
                image_url='https://images.unsplash.com/photo-1473968512647-3e447244af8f?w=500'
            )
        ]
        Product.objects.bulk_create(products)
        
        self.stdout.write(self.style.SUCCESS('Successfully seeded 3 products!'))