from random import choices
from time import timezone
from unicodedata import category
from urllib import request
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class AuctionListings(models.Model):
    Product = models.CharField(max_length=99)
    Description = models.CharField(max_length=10000000)
    Price = models.DecimalField(max_digits=50, decimal_places=2)
    Active = models.BooleanField(default=True)
    CATEGORY = (("Clothing", "Clothing"), ("Furniture", "Furniture"),
                ("Household Items", "Household Items"),
                ("Electronic Items", "Electronic Items"), ("Toys", "Toys"))
    categories = models.CharField(max_length=16, choices=CATEGORY)
    seller = models.ForeignKey(User, on_delete=models.PROTECT)
    image = models.URLField(blank=True)

    def __str__(self):
        return f"{self.Product}"


class Comments(models.Model):
    post = models.ForeignKey(AuctionListings, on_delete=models.CASCADE)
    Review = models.CharField(max_length=10000000000, blank=True)
    RATINGS = (
        ("1", "Terrible"),
        ("2", "Bad"),
        ("3", "Average"),
        ("4", "Good"),
        ("5", "Excellent"),
    )
    ratings = models.CharField(max_length=1, choices=RATINGS, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.post} : {self.Review}"


class Bids(models.Model):
    listing = models.ForeignKey(AuctionListings, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    bid = models.DecimalField(max_digits=99, decimal_places=2, blank=True)
    date = models.DateTimeField(auto_now_add=True)


class Watchlist(models.Model):
    product = models.ManyToManyField(AuctionListings,
                                blank=True,
                                related_name="watchlist_item")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self) :
        return f"{self.user} has added an item to watchlist"
