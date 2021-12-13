"""PurBeurre URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.urls import path
from django.contrib import admin
from .views import legal_notice, index

urlpatterns = [
    path('content/', admin.site.urls),
    path('', index, name="index"),
    path('favoris/', include("Favorite.urls")),
    path('user/', include("User.urls")),
    path('product/', include("Product.urls")),
    path('legal', legal_notice, name="home-legal")
]
