from enum import Flag
from unicodedata import category
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError, models
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.shortcuts import get_object_or_404

from .forms import BidForm, ProductForm, ReviewForm
from django.contrib.auth.decorators import login_required

from .models import User, AuctionListings, Comments, Bids, Watchlist


def index(request):
    products=AuctionListings.objects.filter(Active=True)

    return render(request, "auctions/index.html",{
        "products": products
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def createlisting(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            newlisting=form.save(commit=False)
            newlisting.seller=request.user
            newlisting.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        form = ProductForm()
    return render(request, 'auctions/createlisting.html', {
        "form" : form,
        "products": AuctionListings.objects.all()
        })

def product(request, AuctionListings_id):
    product=AuctionListings.objects.get(pk=AuctionListings_id)
    highestbid=Bids.objects.filter(listing=AuctionListings_id).order_by('-bid').first()
    if request.method=="POST":
        bidform=BidForm(request.POST)
        form=ReviewForm(request.POST)

        if bidform.is_valid():
            newbid=bidform.save(commit=False)
            newbid.listing=product
            newbid.user=request.user
            newbid.save()
            form=ReviewForm(request.POST)
        if form.is_valid():
            newcomment=form.save(commit=False)
            newcomment.post=product
            newcomment.save()
    else:
        bidform=BidForm
        form=ReviewForm
    return render (request, "auctions/product.html",{
        "products":AuctionListings.objects.all(),
        "product": product,
        "form": form,
        "bidform": bidform,
        "comments": Comments.objects.filter(post=AuctionListings_id),
        "highestbid":highestbid
        })

def categories(request):
    categories=["Clothing","Furniture","Household Items","Electronic Items","Toys"]
    return render(request, "auctions/categories.html",{
        "categories" : categories
    })

def category(request, category):
    listings=AuctionListings.objects.filter(categories=category)
    return render(request, "auctions/category.html",{
        "listings":listings,
        "category":category,
    })

@login_required(login_url="auctions/login.html")
def watchlist(request):
    user=request.user
    try:
        listings=Watchlist.objects.filter(user=user)
    except:
        listings=None
    return render(request, "auctions/watchlist.html",{
        "listings" : listings,
    })

@login_required(login_url="auctions/login.html")
def watchlist_add(request, AuctionListings_id):
    user=request.user
    watchlist_item=AuctionListings.objects.get(pk=AuctionListings_id)
    if Watchlist.objects.filter(user=user).filter(product=AuctionListings_id).exists():
        Watchlist.objects.filter(user=user).filter(product=AuctionListings_id).delete()
        return HttpResponseRedirect(reverse("product"), args=(AuctionListings.Product))  
    else :
        watchlist_user=user
        watchlist_user.product= watchlist_item
        watchlist_user.save
        message="Item added to watchlist"
    return render(request, "auctions/product.html",{
        "message":message
    })

@login_required(login_url="auctions/login.html")
def closelisting(request, AuctionListings_id):
    listing=AuctionListings.objects.get(pk=AuctionListings_id)
    if AuctionListings.objects.filter(pk=AuctionListings_id).filter(seller=request.user):
        listing.Active=False
        listing.save()
    return render(request,"auctions/closelisting.html", {
        "listing" : listing,
        "product":AuctionListings.objects.get(pk=AuctionListings_id),
        "highestbid":Bids.objects.filter(listing=AuctionListings_id).order_by('-bid').first(),
        "comments": Comments.objects.filter(post=AuctionListings_id),
    })

