import csv
import os
from django.core.management.base import BaseCommand
from store.models import Product


class Command(BaseCommand):
    help = 'Import products from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']

        if not os.path.exists(csv_file):
            self.stderr.write(f'File not found: {csv_file}')
            return

        self.stdout.write(f'Importing products from {csv_file}...')

        seen_handles = {}
        count = 0

        with open(csv_file, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                handle = row.get('Handle', '').strip()
                name = row.get('Title', '').strip()
                description = row.get('Body (Description)', '').strip()
                price = row.get('Price', '0').strip()
                stock = row.get('Variant Inventory Qty', '0').strip()
                image_url = row.get('Image Src', '').strip()
                category = row.get('Type', 'other').strip().lower()

                # skip duplicate handles (variants), only import first row per product
                if handle in seen_handles:
                    # update stock by adding variant stock
                    try:
                        existing = seen_handles[handle]
                        existing.stock += int(stock) if stock.isdigit() else 0
                        existing.save()
                    except Exception:
                        pass
                    continue

                try:
                    price = float(price)
                except ValueError:
                    price = 0.0

                try:
                    stock = int(stock)
                except ValueError:
                    stock = 0

                product, created = Product.objects.get_or_create(
                    name=name,
                    defaults={
                        'description': description,
                        'price': price,
                        'stock': stock,
                        'image_url': image_url,
                        'category': category,
                    }
                )

                if not created:
                    product.description = description
                    product.price = price
                    product.stock = stock
                    product.image_url = image_url
                    product.category = category
                    product.save()

                seen_handles[handle] = product
                count += 1
                status = 'Added' if created else 'Updated'
                self.stdout.write(f'  {status}: {product.name} | ₹{product.price} | Stock: {product.stock}')

        self.stdout.write(self.style.SUCCESS(f'\nDone! {count} products imported.'))
