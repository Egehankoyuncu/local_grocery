import json
from django.core.management.base import BaseCommand
from grocery.models import Store, Product
from django.core.files import File
import os
from django.conf import settings

class Command(BaseCommand):
    help = 'Loads initial grocery data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Product.objects.all().delete()
        Store.objects.all().delete()

        # Create stores
        stores = {
            'Kroger': {
                'name': 'Kroger',
                'address': '123 Main St, Cincinnati, OH',
                'phone': '555-1234'
            },
            'Walmart': {
                'name': 'Walmart',
                'address': '456 Oak St, Bentonville, AR',
                'phone': '555-5678'
            },
            'Target': {
                'name': 'Target',
                'address': '789 Pine St, Minneapolis, MN',
                'phone': '555-9012'
            }
        }

        for store_name, store_data in stores.items():
            store, created = Store.objects.get_or_create(
                name=store_name,
                defaults=store_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created store: {store_name}'))

        # Create products
        products = [
            {
                'name': 'Bread',
                'price': 2.99,
                'store': 'Kroger',
                'image': 'kroger_bread.jpeg'
            },
            {
                'name': 'Milk',
                'price': 3.49,
                'store': 'Kroger',
                'image': 'kroger_milk.webp'
            },
            {
                'name': 'Eggs',
                'price': 2.99,
                'store': 'Kroger',
                'image': 'kroger_egg.jpeg'
            },
            {
                'name': 'Bread',
                'price': 2.79,
                'store': 'Walmart',
                'image': 'walmart_bread.jpeg'
            },
            {
                'name': 'Milk',
                'price': 3.29,
                'store': 'Walmart',
                'image': 'walmart_milk.jpeg'
            },
            {
                'name': 'Eggs',
                'price': 2.79,
                'store': 'Walmart',
                'image': 'walmart_egg.jpeg'
            },
            {
                'name': 'Bread',
                'price': 2.89,
                'store': 'Target',
                'image': 'target_bread.jpeg'
            },
            {
                'name': 'Milk',
                'price': 3.39,
                'store': 'Target',
                'image': 'targer_milk.jpeg'
            },
            {
                'name': 'Eggs',
                'price': 2.89,
                'store': 'Target',
                'image': 'target_egg.jpeg'
            }
        ]

        for product_data in products:
            store = Store.objects.get(name=product_data['store'])
            image_path = os.path.join(settings.BASE_DIR, 'static', 'store_images', product_data['image'])
            
            product = Product.objects.create(
                name=product_data['name'],
                store=store,
                price=product_data['price']
            )
            
            if os.path.exists(image_path):
                try:
                    with open(image_path, 'rb') as f:
                        product.image.save(product_data['image'], File(f), save=True)
                    self.stdout.write(self.style.SUCCESS(f'Created product with image: {product.name} at {store.name}'))
                except Exception as e:
                    self.stdout.write(self.style.WARNING(f'Could not load image {product_data["image"]}: {str(e)}'))
            else:
                self.stdout.write(self.style.WARNING(f'Image file not found: {image_path}'))

        self.stdout.write(self.style.SUCCESS('Successfully loaded grocery data')) 