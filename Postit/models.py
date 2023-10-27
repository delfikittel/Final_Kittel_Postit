from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Users(models.Model):

    def __str__(self):
        return f'{self.name} -- {self.email}'

    name = models.CharField(max_length= 30)
    password = models.CharField(max_length= 30)
    email = models.EmailField()



class Posts(models.Model):

    def __str__(self):
        return f'{self.heading} -- {self.subtite}'

    heading = models.CharField(max_length= 30)
    author = models.CharField(max_length= 30)
    subtite = models.CharField(max_length= 50, unique = True)
    body = models.CharField(max_length= 1000)
    


class Books(models.Model):

    def __str__(self):
            return f'{self.title} by {self.writer}'

    title = models.CharField(max_length= 100, null = 'null', unique = True)
    writer = models.CharField(max_length= 100)
    genre = models.CharField(max_length= 50)
    


class Avatar(models.Model):
     user = models.ForeignKey(User, on_delete = models.CASCADE)
     image = models.ImageField(upload_to='avatares', null = True, blank = True)


class Opinion(models.Model):

      def __str__(self):
            return f'{self.text} by {self.sign}'
      
      sign = models.CharField(max_length= 30, null = 'null', unique = True)
      text = models.CharField(max_length = 100, null = 'null')

class Photo(models.Model):
    def __str__(self):
        return f'{self.text}'
    image = models.ImageField(upload_to='photos', null = True, blank = True, unique = True)
    text = models.CharField(max_length = 100, null = 'null')



