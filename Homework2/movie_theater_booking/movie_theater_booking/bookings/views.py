from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib import messages
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import *

class MovieList(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
class SeatList(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
class BookingList(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer



def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movie_list.html', {'movies': movies})

def create_movie(request):
    if request.method == 'POST':
        form = Movieform(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)  
            
            movie.save()  
            return redirect('movie_list')
    else:
        form = Movieform()  
    
    context = {'form': form}
    return render(request, 'create_movie.html', context)

def update_movie(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == 'POST':
        form = Movieform(request.POST, instance=movie)
        if form.is_valid():
            movie = form.save(commit=False)  
            movie.save()  
            return redirect('movie_list')
    else:
        form = Movieform(instance=movie)  
    context = {'form': form}
    return render(request, 'create_movie.html', context)

def delete_movie(request, pk):
   movie = Movie.objects.get(pk=pk)
   if request.method == 'POST':
      try:
         print("got id")
         
         
         movie.delete()
         return redirect('movie_list')
      except Movie.DoesNotExist:
            # Handle the case where the project does not exist
        print("does not exist")
        return redirect('movie_list')  # Redirect to an appropriate page
   return render(request, 'delete_movie.html', {'movie':movie})


def register(request):
    form = CreateUserForm(request.POST)
    if form.is_valid():
        user = form.save()
        username = form.cleaned_data.get('username')
        group = Group.objects.get(name='manager_role')
        user.groups.add(group)
        #user = User.objects.create(user=user)
        user.save()
        messages.success(request, 'Account was create for ' + username)
        return redirect('login')
    context={'form':form}
        
    return render(request, 'register.html', context)

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('logout')
    return render(request, 'logout.html')

def book_seats(request, pk):
    movie = Movie.objects.get(pk=pk)
    bookings = Booking.objects.filter(movie=movie)
    seats = []
    for i in range(1, 41):
        seat = Seat.objects.create(seat_number = i)
        
        for booking in bookings:
            if booking.seat.seat_number == i:
                seat.seat_status = True
        seats.append(seat)
    return render(request, 'seat_booking.html', {'seats':seats, 'movie':movie})

def book_seat(request, pk, pk2):
    
    movie = Movie.objects.get(pk=pk)
    if request.method == 'POST':
        form = SeatForm(request.POST)
        if form.is_valid():
            seat = form.save(commit=False)  
            seat.seat_number = pk2
            seat.save()
            booking = Booking.objects.create(movie = movie, seat = seat, user = request.user)  
            booking.save()
            return redirect('movie_list')
    else:
        form = SeatForm()  
    
    context = {'form': form}
    return render(request, 'create_movie.html', context)


def booking_history(request):
    bookings = Booking.objects.filter(user = request.user)
    return render(request, 'booking_history.html', {'bookings': bookings})
   

