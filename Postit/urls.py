from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [ 
   
    path('', home, name= 'home'),
    path('home/', home, name = 'inicio'),
  
   
    


    #Users 
   path('login/', logIn, name='login'),
   path('signup/', signup, name= 'signup'),
   path('logout/', LogoutView.as_view(template_name= 'Postit/logout.html'), name ='logout'),
   
   #path('usersForm/', usersForm, name = 'usersForm'),

    
    # Posts
    path('postsForm/', postsForm, name= 'postsForm' ),
    path('postsSearch/', postsSearch, name = 'postsSearch'),
    path('postsResults/', postsResults, name= 'postsResults'),
    path('postsRead/', postsRead, name = 'postsRead'),
   
    path('editPost/<subtite>', editPost, name = 'editPost'),
    path('deletePost/<int:pk>', DeletePost.as_view(), name = 'deletePost'),


    #Photo
    path('uploadPhoto/', uploadPhoto, name = 'uploadPhoto' ),
    path('photoRead/', photoRead, name = 'photoRead'),
    path('editPhotos/<text>', editPhotos, name = 'editPhotos'),
    path('deletePhoto/<int:pk>', DeletePhoto.as_view(), name = 'deletePhoto'),


    # books
    path('booksForm/', booksForm, name= 'booksForm'),
    path('booksList/', booksList, name = 'booksList'),
    path('editBooks/<title>', editBooks, name = 'editBooks'),
    path('deleteBook/<int:pk>', DeleteBook.as_view(), name = 'deleteBook'),

    #SELF
    path('profile/', profile, name = 'profile'),
    path('editProfile/', editProfile, name = 'editProfile'),
    path('uploadAvatar/', uploadAvatar, name = 'uploadAvatar'),
    path('opinionForm/', opinionForm, name = 'opinionForm'),
    path('opinionList/', opinionList, name = 'opinionList'),

    # ABAOUT ME
    path('aboutMe/', aboutMe, name = 'aboutMe'),
    
    


    #class views
    
    ]