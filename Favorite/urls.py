from django.urls import path
from .views import index
"""the url file is used to associate an url path to a view with path"""

urlpatterns = [
    path("", index, name="favorite-index"),
]
