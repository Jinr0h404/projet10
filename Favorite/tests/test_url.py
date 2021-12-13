from django.urls import resolve


def test_index_url():
    """Check if the name of the view is correct and that the URL matches the name of the view."""
    assert resolve("/favoris/").view_name == "favorite-index"
