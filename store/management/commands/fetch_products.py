import requests
from django.core.management.base import BaseCommand
from store.models import Product


class Command(BaseCommand):
    help = 'Fetch products from Fake Store API and save to database'

    def handle(self, *args, **kwargs):
        self.stdout.write('Fetching products from Fake Store API...')

        try:
            response = requests.get('https://fakestoreapi.com/products', timeout=10)
            response.raise_for_status()
            products = response.json()
        except Exception as e:
            self.stderr.write(f'Failed to fetch products: {e}')
            return

        count = 0
        for item in products:
            product, created = Product.objects.get_or_create(
                name=item['title'],
                defaults={
                    'description': item['description'],
                    'price': item['price'],
                    'stock': 50,
                    'category': item['category'],
                }
            )
            if created:
                count += 1
                self.stdout.write(f'  Added: {product.name}')
            else:
                self.stdout.write(f'  Already exists: {product.name}')

        self.stdout.write(self.style.SUCCESS(f'\nDone! {count} new products added.'))
