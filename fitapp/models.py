

from django.db import models


class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    date_of_joining = models.DateField()
    age = models.IntegerField()
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    PROGRAM_CHOICES = [
        ('Program 1', 'THE RIDE'),
        ('Program 2', 'THE SPIRIT'),
        ('Program 3', 'THE SOUL'),
    ]
    program = models.CharField(max_length=20, choices=PROGRAM_CHOICES)



#checkout


class cheackout(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    email = models.EmailField()
    pincode = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    date = models.DateField()
    time_slot = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
#login


class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
    
    
class Registration(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date_of_joining = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    program = models.CharField(max_length=20)
