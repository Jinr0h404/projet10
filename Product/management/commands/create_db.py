from django.core.management.base import BaseCommand
from Product.models import Product, Category, Store
from .api_get import Api_get


class Command(BaseCommand):
    help = "initialize database"

    def handle(self, *args, **kwargs):
        """retrieve a list of products in JSON format through Open Food Fact
        API. The loop goes through each element of the number of pages given,
        checks if the main categories are correctly entered for the product
        and creates a dictionary list."""
        product = Api_get()
        product_list = product.food()
        for i in product_list:
            new_product = Product.objects.create(
                product_name=i["name"],
                brand=i["brand"],
                description=i["description"],
                nutriscore=i["nutriscore"],
                url=i["url"],
                product_image=i["product_image"],
                product_image_little=i["product_image_little"],
                fat=str(i["fat"]),
                saturated_fat=str(i["saturated_fat"]),
                salt=str(i["salt"]),
                sugar=str(i["sugar"]),
            )
            last_product = Product.objects.last()
            prod_id = last_product.pk
            for category in i["category"]:
                """the value of the category key in the dictionary can contain
                several elements. I therefore loop on the category to fill my
                table with get_or_create function of peewee to haven't a
                duplicate"""
                category = category.strip()
                """ strip() remove spaces before and after item"""
                new_category, created = Category.objects.get_or_create(
                    category_name=category
                )
                cat_id = new_category.pk
                last_product.category.add(cat_id)
            """ make a loop for each store"""
            for store in i["store"]:
                """like category, the value of the store key in the dictionary
                can contain several elements. loop to fill my table with the
                get_or_create function"""
                store = store.strip()
                new_store, created = Store.objects.get_or_create(store_name=store)
                store_id = new_store.pk
                last_product.store.add(store_id)
