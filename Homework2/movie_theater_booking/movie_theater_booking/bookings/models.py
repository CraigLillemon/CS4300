from django.db import models
from django.urls import reverse
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

class Movie(models.Model):
    movie_id = models.BigAutoField(primary_key=True)
    title = models.TextField()
    description = models.TextField()
    release_date = models.DateField()
    duration = models.PositiveIntegerField()
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('movie-detail', args=[str(self.movie_id)])

class Seat(models.Model):
    seat_id = models.BigAutoField(primary_key=True)
    seat_number = models.PositiveIntegerField()
    seat_status = models.BooleanField(default=False)
    def __str__(self):
        return f"Seat {self.seat_number}"
    def get_absolute_url(self):
        return reverse('steat-detail', args=[str(self.seat_id)])

class Booking(models.Model):
    booking_id = models.BigAutoField(primary_key=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE) 
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE) 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_date = models.DateField(auto_now_add=True)




