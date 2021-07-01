from django.contrib import admin
from .models import Listing
from .models import OrderBooking

# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    list_display = ('title','license_number','contact_person','price_per_km','price_per_day','is_booked','is_published')
    list_display_links = ('title',)
    list_filter = ('contact_person','vehicle_type','category','is_booked')
    list_editable = ('is_booked','is_published')
    search_fields = ['title','license_number']
    list_per_page = 10

admin.site.register(Listing,ListingAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('listing','username','pickup_date','return_date','price','phone','order_date','is_confirm')
    list_display_links = ('listing',)

admin.site.register(OrderBooking,OrderAdmin)