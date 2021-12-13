import pytest
from django.urls import reverse
from django.test import Client
from User.models import CustomUser
from Favorite.models import Favorites
from pytest_django.asserts import assertTemplateUsed
from Product.tests.test_models import product_fixture


@pytest.mark.django_db(reset_sequences=True)
def test_search_substitute_view(product_fixture):
    """Creates a test client. Make a request on the URL retrieved using the reverse () function.
        Check that the HTTP status code is 200. Check that the template used is the expected one"""
    client = Client()
    path = reverse("product-search_substitute")
    response = client.get(path, {"query": "1"})
    assert response.status_code == 200
    assertTemplateUsed(response, "Product/search_substitute.html")


def test_search_view(product_fixture):
    """Creates a test client. Make a request on the URL retrieved using the reverse () function.
    Check that the HTTP status code is 200. Check that the template used is the expected one"""
    client = Client()
    path = reverse("product-search")
    response = client.get(path, {"query": "nutella"})
    assert response.status_code == 200
    assertTemplateUsed(response, "Product/search.html")


def test_product_view(product_fixture):
    """Creates a test client. Make a request on the URL retrieved using the reverse () function.
        Check that the HTTP status code is 200. Check that the template used is the expected one"""
    client = Client()
    path = reverse("product-product_info", args=["1"])
    response = client.get(path)
    assert response.status_code == 200
    assertTemplateUsed(response, "Product/product_info.html")


@pytest.mark.django_db(reset_sequences=True)
def test_save_substitute_view(product_fixture):
    """Creates a test client. Make a post request on the URL retrieved using the reverse () function.
        Check that the new favorite is register. Check that the HTTP status code is 302 due to the redirect."""
    client = Client()
    username = "test_user"
    email = "troubadour@gmail.com"
    password = "Troubadour"
    CustomUser.objects.create_user(username=username, email=email, password=password)
    client.login(username=email, password=password)
    old_favorite = Favorites.objects.count()
    path = reverse("product-save_substitute")
    response = client.post(path, {"save": "1,1"})
    new_favorite = Favorites.objects.count()
    assert new_favorite == old_favorite + 1
    assert response.status_code == 302
