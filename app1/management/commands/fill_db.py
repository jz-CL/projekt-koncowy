from django.core.management.base import BaseCommand
from app1.management.commands._private import create_size, create_category, create_color, create_brand, create_product

class Command(BaseCommand):
    help = 'wypełnij bazę danymi'

    def handle(self, *args, **options):
        create_size()
        create_category()
        create_color()
        create_brand()
        create_product()
        self.stdout.write(self.style.SUCCESS("dopisane"))