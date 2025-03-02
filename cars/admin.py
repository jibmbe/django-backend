from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Car, Booking

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('make', 'model', 'year', 'available', 'price_per_day')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('car', 'customer_name', 'pickup_date', 'return_date', 'status')
    list_filter = ('status', 'pickup_date', 'return_date')
    search_fields = ('customer_name', 'customer_email')
    date_hierarchy = 'pickup_date'  # Enables date-based navigation in the admin

    class Media:
        js = ("admin/js/vendor/jquery/jquery.js", "admin/js/core.js", "admin/js/admin/RelatedObjectLookup.js")
        css = {
            "all": ("admin/css/widgets.css",),
        }
