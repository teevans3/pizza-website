from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("menu", views.menu, name="menu"),
    path("orders", views.orders_view, name="orders"),
    path("account", views.account, name="account"),
    path("about", views.about, name="about"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("item_handler", views.item_handler, name="item_handler"),
    path("remove_items", views.remove_items, name="remove_items"),
    path("change-password.html", views.change_password, name="change_password")
]
