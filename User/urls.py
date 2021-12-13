from django.urls import path
from .views import index, signup, signin, logout_user, account
"""the url file is used to associate an url path to a view with path"""

urlpatterns = [
    path('', index, name="user-index"),
    path('signup', signup, name="user-signup"),
    path('signin', signin, name="user-signin"),
    path('logout', logout_user, name="user-logout"),
    path('account', account, name="user-account"),
]
