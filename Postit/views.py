from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import ListView


from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from .models import *


from django.views.generic.edit import DeleteView
# Create your views here.



# Home
def home(request):
    return render(request, 'Postit/home.html')


@login_required
def opinionForm(request):
    opForm = OpinionForm(request.POST)
    if request.method == 'POST':
       
       
       
        if opForm.is_valid():
           
            
            info = opForm.cleaned_data
       
            book = Opinion(
               text = info['text'], 
                sign = info['sign']
                )

            book.save()
            return render(request, 'Postit/opinionList.html')
    
        else:
            opForm = OpinionForm()
       
   
    return render(request, 'Postit/opinionForm.html', {'opForm': opForm})





def opinionList(request):

    opinions = Opinion.objects.all()
    context = {'opinions': opinions}

    return render(request, 'Postit/opinionList.html', context)



# About
def aboutMe(request):
    return render(request, 'Postit/aboutMe.html')

# Users

def signup(request):

    if request.method == 'POST':


        form = SignupForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()

            return render(request,'Postit/home.html', )
        

    else:
        form = SignupForm()

    return render(request, 'Postit/signup.html', {'formulario' : form} )



def logIn(request):

    if request.method == 'POST':

        form = AuthenticationForm(request, data = request.POST)   # reads form POST

        if form.is_valid():

            usuario = form.cleaned_data.get('username')
            passw = form.cleaned_data.get('password')

            user = authenticate(username = usuario, password = passw)

            if user:
                login(request,user)

                return render(request, 'Postit/home.html', {'message': f"We love to see you again!"})
        
        else:
            return render(request, 'Postit/home.html',  {'message': f'Oops! Try again!'})
    
    else:
        
        form = AuthenticationForm()

    return render(request, 'Postit/login.html', {'formulario' : form})


@login_required
def editProfile(request):

    user = request.user

    if request.method == 'POST':
        editForm = UserEditForm(request.POST)

        if editForm.is_valid():
            info = editForm.cleaned_data

            user.email = info['email']
            user.set_password(info['password1'])
            user.first_name = info['first_name']
            user.last_name = info['last_name']
                     

            user.save()

            return render(request, 'Postit/home.html')
        
    else:
        editForm = UserEditForm(initial = {
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            })
        
    return render(request, 'Postit/editProfile.html', {'editForm': editForm, 'user': user})





# Posts
@login_required
def postsForm(request):
    if request.method == 'POST':

        form1 = PostsForm(request.POST)

        if form1.is_valid():

            info = form1.cleaned_data

            post = Posts( heading = info['heading'], author = info['author'], subtite = info['subtite'], body = info['body'])

      
            post.save()
            return render(request, 'Postit/postsRead.html')
        
    else:
        form1 = PostsForm()

    
    return render(request, 'Postit/postsForm.html', {'form1': form1})

@login_required
def postsSearch(request):
    return render(request, 'Postit/home.html')

@login_required
def postsResults(request):
    if request.GET['postHeading']:

        postHeading = request.GET['postHeading']

        posts = Posts.objects.filter(heading__icontains = postHeading)

        return render(request, 'Postit/postsResults.html', {'postHeading': postHeading, 'posts': posts})
    

@login_required
def deletePost(request, subtite):

    post = Posts.objects.get(subtite = subtite)
    post.delete()

    posts = Posts.objects.all()

    contexto = {'posteos' : posts}

    return render(request, 'Postit/postsRead.html', contexto)


@login_required
def editPost(request, subtite):

    post = Posts.objects.get(subtite = subtite)

    if request.method == 'POST':

        myForm = PostsForm(request.POST)

        if myForm.is_valid(): 
            info = myForm.cleaned_data

            post.heading = info['heading']
            post.author = info['author']
            post.subtite = info['subtite']
            post.body = info['body']

            post.save()

            return render(request, 'Postit/postsRead.html')
        
    else:
        myForm= PostsForm(initial = {'heading': post.heading, 'author': post.author, 'subtite': post.subtite, 'body': post.body})

    return render(request, 'Postit/editPost.html', {'myForm': myForm, 'subtite': subtite})





class PostsList(ListView):
    model = Posts


@login_required
def postsRead(request):

    posts = Posts.objects.all()

    contexto = {'posts': posts}

    return render(request, 'Postit/postsRead.html', contexto)


class DeletePost(DeleteView):
    model = Posts
    success_url = '/Postit/postsRead'




#PHOTOS
@login_required
def uploadPhoto(request):

    if request.method == 'POST':

        form = PhotoForm(request.POST, request.FILES)

        if form.is_valid():

            info = form.cleaned_data

            photo = Photo(image = info['image'] ,text = info['text'])
            photo.save()

            return render(request, 'Postit/photoRead.html' )
        
       
    else:
        form = PhotoForm()
    
    return render(request, 'Postit/uploadPhoto.html', {'form': form})

@login_required
def photoRead(request):

    photos = Photo.objects.all()
    
    context = {'photos': photos}

    return render(request, 'Postit/photoRead.html', context)

@login_required
def editPhotos(request, text):

    photo = Photo.objects.get(text = text)

    if request.method == 'POST':

        photoForm = PhotoForm(request.POST)

        if PhotoForm.is_valid(): 
            info = photoForm.cleaned_data

            photo.image = info['image']
            photo.text = info['text']
      
            photo.save()

            return render(request, 'Postit/photoRead.html')
        
    else:
        photoForm= PhotoForm(initial = {'image': photo.image, 'text': photo.text})

    return render(request, 'Postit/editPhotos.html', {'photoForm': photoForm, 'text': text})

@login_required
def deletePhoto(request, image):

    photo = Photo.objects.get(image = image)
    photo.delete()

    photo = Photo.objects.all()

    contexto = {'photos' : photo}

    return render(request, 'Postit/photoRead.html', contexto)


class DeletePhoto(DeleteView):
    model = Photo
    success_url = '/Postit/photoRead'













# Books
@login_required
def booksForm(request):
    if request.method == 'POST':
       
        form2 = BooksForm(request.POST)
       
        if form2.is_valid():
           
            
            info = form2.cleaned_data
       
            book = Books(
                title = info['title'],
                writer = info['writer'],
                genre = info['genre'],
                )
            
           
            book.save()
        
            
            return render(request, 'Postit/booksList.html')
    
    else:
       form2 = BooksForm()
       
   
    return render(request, 'Postit/booksForm.html', {'form2': form2})

@login_required
def booksList(request):

    books = Books.objects.all()
   
    context = {'books': books}

    return render(request, 'Postit/booksList.html', context)

@login_required
def editBooks(request, title):

    book = Books.objects.get(title = title)

    if request.method == 'POST':

        myForm = BooksForm(request.POST)

        if myForm.is_valid(): 
            info = myForm.cleaned_data

            book.title = info['title']
            book.writer = info['writer']
            book.genre = info['genre']

            book.save()

            return render(request, 'Postit/booksList.html')
        
    else:
        myForm= BooksForm(initial = {'title': book.title, 'writer': book.writer, 'genre': book.genre})

    return render(request, 'Postit/editBooks.html', {'myForm': myForm, 'title': title})





@login_required
def deleteBook(request, title):

    book = Books.objects.get(title = title)
    book.delete()

    book = Books.objects.all()

    contexto = {'books' : book}

    return render(request, 'Postit/booksList.html', contexto)


class DeleteBook(DeleteView):
    model = Books
    success_url = '/Postit/booksList'




# SELF
@login_required
def profile(request):
    return render(request, 'Postit/profile.html')


@login_required
def uploadAvatar(request):

    if request.method == 'POST':

        form = AvatarForm(request.POST, request.FILES)

        if form.is_valid():

            currentUser = User.objects.get(username = request.user)

            avatar = Avatar(user = currentUser, image = form.cleaned_data['image'])
            avatar.save()

            return render(request, 'Postit/home.html' )
        
       
    
    else:
        form = AvatarForm()
    
    return render(request, 'Postit/uploadAvatar.html', {'form': form})





