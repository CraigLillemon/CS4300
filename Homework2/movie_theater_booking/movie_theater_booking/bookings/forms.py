from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
class Movieform(ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'description', 'release_date', 'duration')

class SeatForm(ModelForm):
    class Meta:
        model = Seat
        fields = ('seat_status',)




class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']