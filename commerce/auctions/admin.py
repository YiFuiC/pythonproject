from django.contrib import admin
from .models import AuctionListings, Bids, Comments, User, Watchlist

# Register your models here.
admin.site.register(AuctionListings)
admin.site.register(User)
admin.site.register(Comments)
admin.site.register(Watchlist)
admin.site.register(Bids)