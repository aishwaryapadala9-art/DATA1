from django.db import models

# Create your models here.
class UserDetails(models.Model):
    uname = models.CharField(max_length=50,unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    dob = models.DateField()

