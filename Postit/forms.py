from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from .models import *



# USERS
class SignupForm(UserCreationForm):
    
    email = forms.EmailField()
    password1 = forms.CharField(label = 'Password', widget = forms.PasswordInput)
    password2 = forms.CharField(label = 'Repeat your password', widget = forms.PasswordInput)

    class Meta:

        model = User
        fields = ['username',  'first_name', 'last_name','email', 'password1', 'password2']


class UserEditForm(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label = 'Password', widget = forms.PasswordInput)
    password2 = forms.CharField(label = 'Repeat your password', widget = forms.PasswordInput)

    class Meta:

        model = User
        fields = ['first_name', 'last_name','email', 'password1', 'password2']


class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['image']


# POSTS
class PostsForm(forms.Form):
    heading = forms.CharField(max_length= 30)
    author = forms.CharField(max_length= 30)
    subtite = forms.CharField(max_length= 50)
    body = forms.CharField(max_length= 1000)

# PHOTO
class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image', 'text']

class PhotoEditForm(forms.ModelForm):

    image = models.ImageField(upload_to='photos', null = True, blank = True, unique = True)
    text = models.CharField(max_length = 100, null = 'null')
   

    class Meta:

        model = Photo
        fields = ['image', 'text']



# BOOKS
class BooksForm(forms.Form):
    title = forms.CharField(max_length= 100)
    writer = forms.CharField(max_length= 100)
    genre = forms.CharField(max_length= 50)

class OpinionForm(forms.Form):
    text = forms.CharField(max_length = 100)
    sign = forms.CharField(max_length= 30)
