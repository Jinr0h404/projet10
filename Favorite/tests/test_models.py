import pytest
from Favorite.models import Favorites
from Product.models import Product, Store, Category
from User.models import CustomUser


@pytest.mark.django_db
def test_favorite_model():
    """test that the favorite model records the user, product and substitute information in the database"""
    product_list = (
        {
            "name": "nutella",
            "brand": "ferrero",
            "store": "leclerc",
            "category": "pate",
            "nutriscore": "D",
            "description": "petit déjeuner",
            "url": "http//cici",
            "product_image": "http//cici",
            "product_image_little": "http//cici",
            "fat": "0,145",
            "saturated_fat": "0,145",
            "salt": "0,145",
            "sugar": "0,145",
        },
        {
            "name": "lightella",
            "brand": "ferreclean",
            "store": "leclerc",
            "category": "pate",
            "nutriscore": "B",
            "description": "petit déjeuner",
            "url": "http//cici",
            "product_image": "http//cici",
            "product_image_little": "http//cici",
            "fat": "0,14",
            "saturated_fat": "0,04",
            "salt": "0,02",
            "sugar": "0,14",
        },
    )
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
    product = Product.objects.get(pk=2)
    substitute = Product.objects.get(pk=1)
    username = "test_user"
    email = "troubadour@gmail.com"
    password = "Troubadour"
    user = CustomUser.objects.create_user(
        username=username, email=email, password=password
    )
    favorite = Favorites.objects.create(
        substitute_id=product, product_id=substitute, user_id=user
    )
    expected_value = "lightella | nutella | test_user | troubadour@gmail.com"
    assert str(favorite) == expected_value
