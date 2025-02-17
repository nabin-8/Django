from django.db import models

class Artist(models.Model):
    GENDER_CHOICES =[
        ('m', 'Male'),
        ('f', 'female'),
        ('o', 'others')
    ]
    name = models.CharField(max_length=255)
    dob = models.DateTimeField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    address = models.CharField(max_length=255)
    first_release_year = models.CharField(max_length=4)
    no_of_albums_released = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'artist'
        verbose_name_plural = 'artists'

class Music(models.Model):
    GENRE_CHOICES = [
        ('r', 'Rock'),
        ('p', 'Pop'),
        ('j', 'Jazz'),
        ('h', 'Hip Hop'),
        ('c', 'Classical'),
        ('f', 'Folk'),
        ('c', 'Country')
    ]
    artist_id = models.ImageField()
    title = models.CharField(max_length=255)
    album_name = models.CharField(max_length=255)
    genre = models.CharField(max_length=1, choices=GENRE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)