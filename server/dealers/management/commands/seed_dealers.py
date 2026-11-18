
from django.core.management.base import BaseCommand
from dealers.models import Dealer


class Command(BaseCommand):
    help = 'Add sample dealership records'

    def handle(self, *args, **kwargs):
        dealers = [
            {
                'name': 'Kansas City Auto Center',
                'city': 'Kansas City',
                'state': 'Kansas',
                'address': '100 Main Street',
                'zip_code': '66101',
                'phone': '9135550101',
                'website': 'https://example.com'
            },
            {
                'name': 'Wichita Motors',
                'city': 'Wichita',
                'state': 'Kansas',
                'address': '200 Central Avenue',
                'zip_code': '67202',
                'phone': '3165550102',
                'website': 'https://example.com'
            },
            {
                'name': 'Denver Auto Group',
                'city': 'Denver',
                'state': 'Colorado',
                'address': '300 Market Street',
                'zip_code': '80202',
                'phone': '3035550103',
                'website': 'https://example.com'
            },
            {
                'name': 'Dallas Car World',
                'city': 'Dallas',
                'state': 'Texas',
                'address': '400 Commerce Street',
                'zip_code': '75201',
                'phone': '2145550104',
                'website': 'https://example.com'
            },
        ]

        for item in dealers:
            Dealer.objects.update_or_create(
                name=item['name'],
                defaults=item
            )

        self.stdout.write(
            self.style.SUCCESS('Dealership records added successfully!')
        )
