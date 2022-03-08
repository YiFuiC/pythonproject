from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("createlisting", views.createlisting, name="createlisting"),
    path("<int:AuctionListings_id>",views.product,name="product"),
    path("categories", views.categories, name="categories"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("clothing", views.clothing, name="clothing"),
    path("electronic_items", views.electronic_items, name="electronic_items"),
    path("household_items", views.household_items,name="household_items"),
    path("furniture", views.furniture, name="furniture"),
    path("toys",views.toy, name="toys"),
    path("product/add_watchlist", views.add_watchlist, name="add_watchlist")
]
