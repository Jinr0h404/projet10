from Product.management.commands.api_get import Api_get


class MockResponse:
    """mock the request to the openfood fact"""

    @staticmethod
    def json():
        return {
            "count": 853836,
            "page": 2,
            "page_count": 20,
            "page_size": 20,
            "products": [
                {
                    "_id": "3168930010265",
                    "brands": "QUAKER,Cruesli",
                    "categories": "Breakfasts,Cereals and their products,Breakfast cereals,Mueslis",
                    "checkers_tags": [],
                    "ciqual_food_name_tags": ["muesli-average"],
                    "generic_name": "",
                    "generic_name_fr": "Pépites de céréales croustillantes avec Mélange de Noix",
                    "image_front_small_url": "https://images.openfoodfacts.org/images/products/316/893/001/0265/front_fr.170.200.jpg",
                    "image_packaging_url": "https://images.openfoodfacts.org/images/products/316/893/001/0265/packaging_fr.134.400.jpg",
                    "image_small_url": "https://images.openfoodfacts.org/images/products/316/893/001/0265/front_fr.170.200.jpg",
                    "image_url": "https://images.openfoodfacts.org/images/products/316/893/001/0265/front_fr.170.400.jpg",
                    "nutriments": {
                        "carbohydrates": 57,
                        "fat": 19,
                        "fat_100g": 19,
                        "fat_serving": 8.55,
                        "fat_unit": "g",
                        "fat_value": 19,
                        "nova-group_serving": 4,
                        "nutrition-score-fr": -2,
                        "nutrition-score-fr_100g": -2,
                        "phosphorus": 0.215,
                        "salt": 0,
                        "salt_100g": 0,
                        "saturated-fat": 2,
                        "saturated-fat_100g": 2,
                        "sugars": 12,
                        "sugars_100g": 12,
                    },
                    "nutrition_grade_fr": "a",
                    "nutrition_grades": "a",
                    "product_name": "",
                    "product_name_fr": "Quaker Cruesli Mélange de noix",
                    "product_name_fr_imported": "Quaker Cruesli Mélange de noix",
                    "stores": "Intermarché,Magasins U",
                    "url": "https://fr.openfoodfacts.org/produit/3168930010265/quaker-cruesli-melange-de-noix",
                }
            ],
        }


def test_api_get(mocker):
    """mock the request to the openfood fact api in order to check if the api get function does return a dictionary
    with the elements formatted and sorted"""
    mocker.patch(
        "requests.get",
        return_value=MockResponse(),
    )
    list_product = Api_get()
    sut = list_product.food()
    expected_value = {
        "name": "quaker cruesli mélange de noix",
        "brand": "quaker,cruesli",
        "store": ["intermarché", "magasins u"],
        "category": [
            "breakfasts",
            "cereals and their products",
            "breakfast cereals",
            "mueslis",
        ],
        "nutriscore": "A",
        "description": "Pépites de céréales croustillantes avec Mélange de Noix",
        "url": "https://fr.openfoodfacts.org/produit/3168930010265/quaker-cruesli-melange-de-noix",
        "product_image": "https://images.openfoodfacts.org/images/products/316/893/001/0265/front_fr.170.400.jpg",
        "product_image_little": "https://images.openfoodfacts.org/images/products/316/893/001/0265/front_fr.170.200.jpg",
        "fat": 19,
        "saturated_fat": 2,
        "salt": 0,
        "sugar": 12,
    }
    assert sut[0] == expected_value
