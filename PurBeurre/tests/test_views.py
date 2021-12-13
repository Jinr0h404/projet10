from django.urls import reverse
from django.test import Client
from pytest_django.asserts import assertTemplateUsed


def test_index_purBeurre_view():
    """Creates a test client. Make a request on the URL retrieved using the reverse () function.
    Check that the HTTP status code is 200 or the expected code. Check that the template used is the expected one"""
    client = Client()
    path = reverse("index")
    response = client.get(path)
    assert response.status_code == 200
    assertTemplateUsed(response, "PurBeurre/index.html", "PurBeurre/base.html")


def test_legal_view():
    """Creates a test client. Make a request on the URL retrieved using the reverse () function.
    Check that the HTTP status code is 200 or the expected code. Check that the template used is the expected one"""
    client = Client()
    path = reverse("home-legal")
    response = client.get(path)
    assert response.status_code == 200
    assertTemplateUsed(response, "PurBeurre/legal_notice.html", "PurBeurre/base.html")
