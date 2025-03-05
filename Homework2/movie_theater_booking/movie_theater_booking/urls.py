"""
URL configuration for movie_theater_booking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from .bookings import views
from django.contrib.auth.decorators import login_required
from rest_framework import routers, serializers, viewsets



router = routers.DefaultRouter()
router.register(r'movies', views.MovieList)
router.register(r'seats', views.SeatList)
router.register(r'bookings', views.BookingList)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

    



    path('', views.movie_list, name = 'movie_list'),
    path('', views.movie_list, name = 'login'),
    path('bookings', views.booking_history, name = 'booking_history'),
    
    path('movie/create_movie', views.create_movie, name = 'movie_form'),
    path('movie/update/<int:pk>/', views.update_movie, name='update_movie'),
    path('movie/<int:pk>/delete/', views.delete_movie, name='delete_movie'),
    
    path('movie/<int:pk>/book_seats/', views.book_seats, name='book_seats'),
    path('movie/<int:pk>/book_seats/<int:pk2>', views.book_seat, name='book_seat'),

    

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register', views.register, name = 'register_page'),
    path('accounts/logout/', views.logout_view, name='logout'),
]





