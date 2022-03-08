from enum import Flag
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError, models
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


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
    return render(request, "auctions/category.html")

@login_required(login_url="auctions/login.html")
def watchlist(request):
   listings=Watchlist.objects.filter(user=request.user)
   return render (request, "auctions/watchlist.html")


@login_required(login_url="auctions/login.html")
def add_watchlist(request, AuctionListings_id):
    if request.method=="POST":
        item=AuctionListings.objects.get(pk=int(request.POST['addwatchlist']))
        user = Watchlist.objects.get(user=request.user)
        user.product.add(item)
        return HttpResponseRedirect(reverse("watchlist", args=(AuctionListings.id,)))

def toy(request):
    try:
        listings=AuctionListings.objects.filter(categories="T").filter(Active=True)
        message=""
    except:
        message="No listings available under this category."
    return render (request,"auctions/toy.html",{
        "listings":listings
    })

def furniture(request):
    try:
        listings=AuctionListings.objects.filter(categories="F").filter(Active=True)
        message=""
    except:
        message="No listings available under this category."
    return render (request,"auctions/furniture.html",{
        "listings":listings
    })

def electronic_items(request):
    try:
        listings=AuctionListings.objects.filter(categories="E").filter(Active=True)
        message=""
    except:
        message="No listings available under this category."
    return render (request,"auctions/electronic_items.html",{
        "listings":listings
    })

def household_items(request):
    try:
        listings=AuctionListings.objects.filter(categories="H").filter(Active=True)
        message=""
    except:
        message="No listings available under this category."
    return render (request,"auctions/household_items.html",{
        "listings":listings
    })

def clothing(request):
    try:
        listings=AuctionListings.objects.filter(categories="C").filter(Active=True)
        message=""
    except:
        message="No listings available under this category."
    return render (request,"auctions/clothing.html",{
        "listings":listings
    })




    


    


