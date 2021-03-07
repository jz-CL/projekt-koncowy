from django.core.management.base import BaseCommand
from app1.management.commands._private import create_size, create_category, create_color, create_brand

class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **options):
        # generate_grades(show_grades, grades_amount)
        create_size()
        create_category()
        create_color()
        create_brand()
        self.stdout.write(self.style.SUCCESS("dopisane"))