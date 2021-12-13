import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from selenium.webdriver.common.by import By
from User.models import CustomUser


class TestAuthentification(StaticLiveServerTestCase):
    """class containing methods to check the authentication part of the application"""
    def test_signup(self):
        """functional test with selenium to verify the user account creation scenario."""
        self.s = Service("User/tests/functional_tests/chromedriver")
        self.browser = webdriver.Chrome(service=self.s)
        self.browser.get(self.live_server_url + reverse("user-signup"))
        username = self.browser.find_element(By.ID, "id_username")
        username.send_keys("ewen_test")
        email = self.browser.find_element(By.ID, "id_email")
        email.send_keys("ewen_test@test.com")
        password1 = self.browser.find_element(By.ID, "id_password1")
        password1.send_keys("ewen12345")
        password2 = self.browser.find_element(By.ID, "id_password2")
        password2.send_keys("ewen12345")
        signup = self.browser.find_element(By.NAME, "signup")
        signup.submit()
        self.assertEqual(self.browser.find_element(By.TAG_NAME, "h2").text, "ewen_test")
        self.assertEqual(
            self.browser.current_url, self.live_server_url + reverse("user-account")
        )
        self.browser.close()

    def test_signin_not_account(self):
        """functional test with selenium to verify the user signin wihtout account."""
        self.s = Service("User/tests/functional_tests/chromedriver")
        self.browser = webdriver.Chrome(service=self.s)
        self.browser.get(self.live_server_url + reverse("user-signin"))
        email = self.browser.find_element(By.ID, "id_email")
        email.send_keys("ewen_test@test.com")
        password = self.browser.find_element(By.ID, "id_password")
        password.send_keys("ewen12345")
        signin = self.browser.find_element(By.NAME, "signin")
        signin.submit()
        self.assertEqual(
            self.browser.find_element(By.TAG_NAME, "p").text, "Identifiants incorrects"
        )
        self.assertEqual(
            self.browser.current_url, self.live_server_url + reverse("user-signin")
        )
        self.browser.close()

    @pytest.mark.django_db
    def test_signin(self):
        """functional test with selenium to verify the user signin scenario."""
        username = "toto"
        email = "toto@gmail.com"
        password = "ewen12345"
        CustomUser.objects.create_user(username=username, email=email, password=password)
        self.s = Service("User/tests/functional_tests/chromedriver")
        self.browser = webdriver.Chrome(service=self.s)
        self.browser.get(self.live_server_url + reverse("user-signin"))
        email = self.browser.find_element(By.ID, "id_email")
        email.send_keys("toto@gmail.com")
        password = self.browser.find_element(By.ID, "id_password")
        password.send_keys("ewen12345")
        signin = self.browser.find_element(By.NAME, "signin")
        signin.submit()
        self.assertEqual(
            self.browser.current_url, self.live_server_url + reverse("user-account")
        )
        self.assertEqual(self.browser.find_element(By.TAG_NAME, "h2").text, "toto")
        self.browser.close()
