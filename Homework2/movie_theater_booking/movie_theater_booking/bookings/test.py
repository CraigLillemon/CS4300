from django.test import TestCase
from .models import *
from rest_framework.test import APIClient
from rest_framework import status

class UnitTest(TestCase):
    def testMovieCreate(self):
        movie = Movie.objects.create(title="Diehard", description="Christmas", release_date="2025-3-4", duration = 2)
        self.assertEqual(movie.title, "Diehard")
        self.assertEqual(movie.description, "Christmas")
        self.assertEqual(movie.release_date, "2025-3-4")
        self.assertEqual(movie.duration, 2)
    def testSeat(self):
        seat =Seat.objects.create(seat_number=50, seat_status=True)
        self.assertEqual(seat.seat_number, 50)
        self.assertEqual(seat.seat_status, True)

    def testBooking(self):
        movie = Movie.objects.create(title="Diehard", description="Christmas", release_date="2025-3-4", duration = 2)
        seat = Seat.objects.create(seat_number=50, seat_status=True)
        booking = Booking.objects.create(movie = movie, seat = seat, user = 1)
        self.assertEqual(booking.movie, movie)
        self.assertEqual(booking.seat, seat)
        



