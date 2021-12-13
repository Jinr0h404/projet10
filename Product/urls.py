from django.urls import path
from .views import search, search_substitute, product_info, save_substitute
"""the url file is used to associate an url path to a view with path"""

urlpatterns = [
    path("search", search, name="product-search"),
    path("search_substitute", search_substitute, name="product-search_substitute"),
    path("product_info-<int:product_id>", product_info, name="product-product_info"),
    path("save_substitute", save_substitute, name="product-save_substitute"),
]
