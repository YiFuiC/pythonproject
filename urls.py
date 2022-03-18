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
    path("category/<str:category>", views.category, name="category"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("<int:AuctionListings_id>/watchlist_add", views.watchlist_add, name="watchlist_add"),
    path("closelisting/<int:AuctionListings_id>", views.closelisting, name="closelisting")
]
    