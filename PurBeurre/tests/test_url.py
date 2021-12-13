from django.urls import resolve


def test_index_url():
    """Check if the name of the view is correct and that the URL matches the name of the view."""
    assert resolve("/").view_name == "index"


def test_legal_url():
    """Check if the name of the view is correct and that the URL matches the name of the view."""
    assert resolve("/legal").view_name == "home-legal"
