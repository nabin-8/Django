from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=1)
    address = models.CharField(max_length=255)
    first_release_year 
    
