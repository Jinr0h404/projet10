from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestSearch(StaticLiveServerTestCase):
    def test_search_navbar(self):
        """tests the user's navigation when searching through the search bar in the navigation menu"""
        self.s = Service("Product/tests/functional_tests/chromedriver")
        self.browser = webdriver.Chrome(service=self.s)
        self.browser.set_window_position(0, 0)
        self.browser.set_window_size(1024, 768)
        self.browser.get(self.live_server_url + reverse("index"))
        search_input = self.browser.find_element(By.ID, "search_form_navbar")
        search_input.send_keys("pizza")
        search_input.send_keys(Keys.RETURN)
        self.assertEqual(self.browser.find_element(By.TAG_NAME, "h2").text, "Pour quel aliment voulez-vous un substitut ?")
        self.assertEqual(
            self.browser.current_url, self.live_server_url + reverse("product-search") + "?query=pizza"
        )
        self.browser.close()

    def test_search_index_return(self):
        """tests the user's navigation when doing a search using the search tool on the index page
        with return keys"""
        self.s = Service("Product/tests/functional_tests/chromedriver")
        self.browser = webdriver.Chrome(service=self.s)
        self.browser.get(self.live_server_url + reverse("index"))
        search_input = self.browser.find_element(By.ID, "searchForm")
        search_input.send_keys("pizza")
        search_input.send_keys(Keys.RETURN)
        self.assertEqual(self.browser.find_element(By.TAG_NAME, "h2").text, "Pour quel aliment voulez-vous un substitut ?")
        self.assertEqual(
            self.browser.current_url, self.live_server_url + reverse("product-search") + "?query=pizza" + "&search_input=chercher"
        )
        self.browser.close()

    def test_search_index_submit(self):
        """tests the user's navigation when doing a search using the search tool on the index page
        with submit button"""
        self.s = Service("Product/tests/functional_tests/chromedriver")
        self.browser = webdriver.Chrome(service=self.s)
        self.browser.get(self.live_server_url + reverse("index"))
        search_input = self.browser.find_element(By.ID, "searchForm")
        search_input.send_keys("pizza")
        search_submit = self.browser.find_element(By.NAME, "search_input")
        search_submit.submit()
        self.assertEqual(self.browser.find_element(By.TAG_NAME, "h2").text, "Pour quel aliment voulez-vous un substitut ?")
        self.assertEqual(
            self.browser.current_url, self.live_server_url + reverse("product-search") + "?query=pizza"
        )
        self.browser.close()
