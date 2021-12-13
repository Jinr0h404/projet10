import pytest
from Product.models import Product, Store, Category


@pytest.fixture
def product_fixture(db) -> Product:
    """creates the fixture for the test database with 3 products"""
    product_list = [
        {
            "name": "nutella",
            "store": "leclerc",
            "category": ["pate", "pate à tartiner", "petit déjeuner", "chocolat"],
            "nutriscore": "D",
            "description": "petit déjeuner",
            "fat": "0,145",
            "saturated_fat": "0,145",
            "salt": "0,145",
            "sugar": "0,145",
        },
        {
            "name": "lightella",
            "store": "leclerc",
            "category": ["pate"],
            "nutriscore": "B",
            "description": "petit déjeuner",
            "fat": "0,14",
            "saturated_fat": "0,04",
            "salt": "0,02",
            "sugar": "0,14",
        },
        {
            "name": "nutalla",
            "store": "leclerc",
            "category": ["pate à tartiner", "petit déjeuner", "chocolat"],
            "nutriscore": "B",
            "description": "petit déjeuner",
            "fat": "0,14",
            "saturated_fat": "0,04",
            "salt": "0,02",
            "sugar": "0,14",
        },
    ]
    for i in product_list:
        new_product = Product.objects.create(
            product_name=i["name"],
            nutriscore=i["nutriscore"],
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


def test_product_model(product_fixture):
    """test that the product model records the product information in the database"""
    product = Product.objects.get(product_name="nutella")
    expected_value = "nutella"
    assert str(product) == expected_value


@pytest.mark.django_db
def test_category_model():
    """test that the category model records the category information in the database"""
    category = Category.objects.create(category_name="pate à tartiner")
    expected_value = "pate à tartiner"
    assert str(category) == expected_value


@pytest.mark.django_db
def test_store_model():
    """test that the store model records the store information in the database"""
    store = Store.objects.create(store_name="auchan")
    expected_value = "auchan"
    assert str(store) == expected_value
