# your_app/management/commands/update_slugs.py

from django.core.management.base import BaseCommand
from django.utils.text import slugify
from store.models import Product


class Command(BaseCommand):
    help = "Update slugs for all products based on their unique title"

    def handle(self, *args, **kwargs):
        products = Product.objects.all()
        for product in products:
            product.save()
