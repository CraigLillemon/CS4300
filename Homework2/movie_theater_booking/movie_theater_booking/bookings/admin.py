from django.contrib import admin
from .models import Movie, Seat, Booking

# Register the models to make them available in the Django admin panel
admin.site.register(Movie)
admin.site.register(Seat)
admin.site.register(Booking)