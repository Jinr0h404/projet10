import requests


class Api_get:
    help = "initialize database"

    def __init__(self):
        """retrieve a list of products in JSON format through Open Food Fact
        API. The loop goes through each element of the number of pages given,
        checks if the main categories are correctly entered for the product
        and creates a dictionary list."""
        self.product_list = []
        self.pages = 20
        self.json = 1
        self.page_size = 30
        self.request_url = "https://fr.openfoodfacts.org/cgi/search.pl"
        self.clean_list = []

    def food(self):
        for i in range(1, self.pages):
            params = {
                "action": "process",
                "page_size": self.page_size,
                "page": i,
                "json": self.json,
            }
            r = requests.get(self.request_url, params)
            data_json = r.json()
            for product in data_json["products"]:
                if (
                    product.get("product_name_fr") and
                        product.get("categories") and
                        product.get("nutrition_grade_fr") and
                        product.get("stores")
                ):
                    """generate a list of dict where each dict = a product"""
                    if product.get("product_name_fr").lower() not in self.product_list:
                        nutriments = product.get("nutriments")
                        if "fat_100g" not in nutriments:
                            fat = "NC"
                        else:
                            fat = nutriments["fat_100g"]
                        if "saturated-fat_100g" not in nutriments:
                            saturated_fat = "NC"
                        else:
                            saturated_fat = nutriments["saturated-fat_100g"]
                        if "salt_100g" not in nutriments:
                            salt = "NC"
                        else:
                            salt = nutriments["salt_100g"]
                        if "sugars_100g" not in nutriments:
                            sugar = "NC"
                        else:
                            sugar = nutriments["sugars_100g"]
                        self.product_list.append(
                            {
                                "name": product.get("product_name_fr").lower(),
                                "brand": product.get("brands").lower(),
                                "store": product.get("stores").lower().split(","),
                                "category": product.get("categories")
                                .lower()
                                .split(","),
                                "nutriscore": product.get("nutrition_grade_fr").upper(),
                                "description": product.get("generic_name_fr"),
                                "url": product.get("url"),
                                "product_image": product.get("image_url"),
                                "product_image_little": product.get("image_small_url"),
                                "fat": fat,
                                "saturated_fat": saturated_fat,
                                "salt": salt,
                                "sugar": sugar,
                            }
                        )
        return self.product_list
