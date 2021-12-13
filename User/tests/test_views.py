import pytest
from django.urls import reverse
from django.test import Client
from pytest_django.asserts import assertTemplateUsed
from User.models import CustomUser


def test_index_user_view():
    """Creates a test client. Make a request on the URL retrieved using the reverse () function.
    Check that the HTTP status code is 200 or the expected code. Check that the template used is the expected one"""
    client = Client()
    path = reverse("user-index")
    response = client.get(path)
    assert response.status_code == 200
    assertTemplateUsed(response, "User/index_user.html", "PurBeurre/base.html")


def test_account_user_view():
    """Creates a test client. Make a request on the URL retrieved using the reverse () function.
    Check that the HTTP status code is 302 if user is not connected"""
    client = Client()
    path = reverse("user-account")
    response = client.get(path)
    assert response.status_code == 302


@pytest.mark.django_db
def test_account_user_connected_view():
    """Creates a test client. Make a request on the URL retrieved using the reverse () function.
    Check that the HTTP status code is 200 if user is connected. Check that the template used is the expected one"""
    client = Client()
    username = "test_user"
    email = "troubadour@gmail.com"
    password = "Troubadour"
    CustomUser.objects.create_user(username=username, email=email, password=password)
    client.login(username=email, password=password)
    path = reverse("user-account")
    response = client.get(path)
    assert response.status_code == 200
    assertTemplateUsed(response, "User/account.html")


def test_signup_user_view():
    """Creates a test client. Make a request on the URL retrieved using the reverse () function.
    Check that the HTTP status code is 200. Check that the template used is the expected one"""
    client = Client()
    path = reverse("user-signup")
    response = client.get(path)
    assert response.status_code == 200
    assertTemplateUsed(response, "User/signup.html")


def test_signin_user_view():
    """Creates a test client. Make a request on the URL retrieved using the reverse () function.
    Check that the HTTP status code is 200. Check that the template used is the expected one"""
    client = Client()
    path = reverse("user-signin")
    response = client.get(path)
    assert response.status_code == 200
    assertTemplateUsed(response, "User/signin.html")


@pytest.mark.django_db
def test_logout_user_view():
    """Creates a test client. Make a request on the URL retrieved using the reverse () function.
    Check that the HTTP status code is 200 or the expected code. Check that the template used is the expected one"""
    client = Client()
    username = "test_user"
    email = "troubadour@gmail.com"
    password = "Troubadour"
    CustomUser.objects.create_user(username=username, email=email, password=password)
    client.login(username=email, password=password)
    path = reverse("user-logout")
    response = client.get(path)
    assert response.status_code == 302
