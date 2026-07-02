import csv
from datetime import date
from decimal import Decimal

from django.conf import settings
from django.core.management.base import BaseCommand

from phones.models import Phone


class Command(BaseCommand):
    help = 'Import phones from the configured CSV file'

    def handle(self, *args, **options):
        with open(settings.PHONES_CSV, encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file, delimiter=';')
            imported = 0

            for row in reader:
                phone, _ = Phone.objects.update_or_create(
                    id=int(row['id']),
                    defaults={
                        'name': row['name'],
                        'image': row['image'],
                        'price': Decimal(row['price']),
                        'release_date': date.fromisoformat(row['release_date']),
                        'lte_exists': row['lte_exists'] == 'True',
                    },
                )
                imported += 1

        self.stdout.write(self.style.SUCCESS(f'Imported {imported} phones'))
