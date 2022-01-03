from django.core.management.base import BaseCommand
from Product.models import Product, Category, Store
from .api_get import Api_get


class Command(BaseCommand):
    help = "update database"

    def handle(self, *args, **kwargs):
        """retrieve a list of products in JSON format through Open Food Fact
        API. The loop goes through each element of the number of pages given,
        checks if the main categories are correctly entered for the product
        and creates a dictionary list."""
        product = Api_get()
        product_list = product.food()
        for i in product_list:
            if Product.objects.filter(product_name=i["name"], url=i["url"]):
                old_product = Product.objects.get(product_name=i["name"], url=i["url"])
                old_product.brand=i["brand"]
                old_product.description=i["description"]
                old_product.nutriscore=i["nutriscore"]
                old_product.fat=str(i["fat"])
                old_product.saturated_fat=str(i["saturated_fat"])
                old_product.salt=str(i["salt"])
                old_product.sugar=str(i["sugar"])
                old_product.save()
