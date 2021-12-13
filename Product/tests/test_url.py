import pytest

from django.urls import reverse, resolve
from Product.models import Product


def test_search_url():
    """Check if the name of the view is correct and that the URL matches the name of the view."""
    assert resolve("/product/search").view_name == "product-search"


def test_search_substitute_url():
    """Check if the name of the view is correct and that the URL matches the name of the view."""
    assert (
        resolve("/product/search_substitute").view_name == "product-search_substitute"
    )


def test_save_substitute_url():
    """Check if the name of the view is correct and that the URL matches the name of the view."""
    assert resolve("/product/save_substitute").view_name == "product-save_substitute"


@pytest.mark.django_db
def test_product_infos_url():
    """Create a book using the Book template.
    Generates the URL using the name of the view passed as a parameter. Check if the URL is correct.
    Check if the name of the view is correct and that the URL matches the name of the view."""
    Product.objects.create(
        product_name="nutella",
        nutriscore="E",
        fat="NC",
        saturated_fat="NC",
        salt="NC",
        sugar="NC",
    )
    path = reverse("product-product_info", kwargs={"product_id": 1})
    assert path == "/product/product_info-1"
    assert resolve(path).view_name == "product-product_info"
