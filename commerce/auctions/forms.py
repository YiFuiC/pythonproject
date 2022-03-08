from dataclasses import fields
from django import forms
from .models import AuctionListings, Bids, Comments, Watchlist

class ProductForm(forms.ModelForm):
    class Meta:
        model=AuctionListings
        fields=[
            'Product',
            'Description',
            'Price',
            'categories',
            'image',
        ]

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Comments
        fields=[
            'Review',
            'ratings',
        ]
class BidForm(forms.ModelForm):
    class Meta:
        model=Bids
        fields=[
            'bid',
        ]
