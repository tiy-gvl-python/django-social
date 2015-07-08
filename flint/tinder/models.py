from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=200, blank=True)
    distance = models.IntegerField(default=1)  # turn this into location (0,0)
    age = models.IntegerField(default=18)
    sex = models.BooleanField()  # True = male
    preferred_sex = models.BooleanField()

    def __str__(self):
        return self.name


class Preference(models.Model):
    primary_id = models.ForeignKey(Profile, related_name='swiper')
    preferred_id = models.ForeignKey(Profile, related_name='swiped')
    preferrence = models.BooleanField()

    class Meta:
        ordering = ['primary_id']

    def __str__(self):
        if preferrence:
            return "I want to make friends"
        else:
            return "Bleh"


class Comment(models.Model):
    profile = models.ForeignKey(Profile)
    text = models.CharField(max_length=300)
    moment = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
