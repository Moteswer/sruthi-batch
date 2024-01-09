# models.py
from django.db import models



 
from unicodedata import name
from django.db import models

# Create your models here.
class movie(models.Model):
    name = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    desc = models.TextField
    url= models.URLField
    rating = models.FloatField()
    image1 = models.CharField( max_length=500)
    image2 = models.CharField( max_length=500)
    image3 = models.CharField( max_length=500)
    image4 = models.CharField( max_length=500)

class series(models.Model):
    name = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    desc = models.CharField(max_length=500)
    url= models.CharField(max_length=500)
    rating = models.FloatField()
    image1 = models.CharField( max_length=500)
    image2 = models.CharField( max_length=500)
    image3 = models.CharField( max_length=500)
    image4 = models.CharField( max_length=500)

class upcoming(models.Model):
    name = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    desc = models.CharField(max_length=500)
    url= models.CharField(max_length=500)
    rating = models.FloatField()
    image1 = models.CharField( max_length=500)
    image2 = models.CharField( max_length=500)
    image3 = models.CharField( max_length=500)
    image4 = models.CharField( max_length=500)

class chromovies(models.Model):
    name = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    desc = models.CharField(max_length=500)
    url= models.CharField(max_length=500)
    rating = models.FloatField()
    image1 = models.CharField( max_length=500)
    image2 = models.CharField( max_length=500)
    image3 = models.CharField( max_length=500)
    image4 = models.CharField( max_length=500)


class newlatest(models.Model):
    name = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    directer = models.CharField(max_length=50)
    long = models.CharField(max_length=500)
    genre = models.CharField(max_length=500)
    sdesc = models.CharField(max_length=500)
    ldesc = models.CharField(max_length=1000)
    url= models.CharField(max_length=1000)
    svedio =  models.CharField(max_length=1000)
    rating = models.FloatField()
    image1 = models.CharField( max_length=500)
    image2 = models.CharField( max_length=500)
    image3 = models.CharField( max_length=500)
    image4 = models.CharField( max_length=500)

class newmovie(models.Model):
    name = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    directer = models.CharField(max_length=50)
    long = models.CharField(max_length=500)
    genre = models.CharField(max_length=500)
    sdesc = models.CharField(max_length=500)
    ldesc = models.CharField(max_length=1000)
    url= models.CharField(max_length=1000)
    svedio =  models.CharField(max_length=1000)
    rating = models.FloatField()
    image1 = models.CharField( max_length=500)
    image2 = models.CharField( max_length=500)
    image3 = models.CharField( max_length=500)
    image4 = models.CharField( max_length=500)

class newseries(models.Model):
    name = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    directer = models.CharField(max_length=50)
    long = models.CharField(max_length=500)
    genre = models.CharField(max_length=500)
    sdesc = models.CharField(max_length=500)
    ldesc = models.CharField(max_length=1000)
    url= models.CharField(max_length=1000)
    svedio =  models.CharField(max_length=1000)
    rating = models.FloatField()
    image1 = models.CharField( max_length=500)
    image2 = models.CharField( max_length=500)
    image3 = models.CharField( max_length=500)
    image4 = models.CharField( max_length=500)

class newupcoming(models.Model):
    name = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    directer = models.CharField(max_length=50)
    long = models.CharField(max_length=500)
    genre = models.CharField(max_length=500)
    sdesc = models.CharField(max_length=500)
    ldesc = models.CharField(max_length=500)
    url= models.CharField(max_length=500)
    svedio =  models.CharField(max_length=500)
    rating = models.FloatField()
    image1 = models.CharField( max_length=500)
    image2 = models.CharField( max_length=500)
    image3 = models.CharField( max_length=500)
    image4 = models.CharField( max_length=500)

class newchromovies(models.Model):
    name = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    directer = models.CharField(max_length=50)
    long = models.CharField(max_length=500)
    genre = models.CharField(max_length=500)
    sdesc = models.CharField(max_length=500)
    ldesc = models.CharField(max_length=500)
    url= models.CharField(max_length=500)
    svedio =  models.CharField(max_length=500)
    rating = models.FloatField()
    image1 = models.CharField( max_length=500)
    image2 = models.CharField( max_length=500)
    image3 = models.CharField( max_length=500)
    image4 = models.CharField( max_length=500)




class Customer(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)  # You should use a more secure way to store passwords
    DoB = models.DateField()
    phonenumber = models.CharField(max_length=15)  # Adjust max_length as needed

class CustomerProfile(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='profile')
    profilename = models.CharField(max_length=50)
    pin = models.CharField(max_length=4)  
    avatar = models.ImageField(upload_to='avatars/')

class KidProfile(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='kid_profiles')
    profilename = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='avatars/')