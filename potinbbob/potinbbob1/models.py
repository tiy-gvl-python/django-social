from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User)

    def __str__(self):
        return 'username: {}'.format(self.user)


class Collection(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=25)
    comment = models.CharField(max_length=60)

    def __str__(self):
       return "Title: {} | Comment: {} | User: {}".format(self.title, self.comment, self.user)


class Genre(models.Model):
    genre = models.TextField(max_length=20)

    def __str__(self):
        return "{}".format(self.genre)


class Pic(models.Model):
    user = models.ForeignKey(User)
    link_to_origin = models.URLField()
    comment = models.CharField(max_length=150)
    time_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    category = models.ForeignKey(Collection)
    origin_info = models.CharField(max_length=35)
    tag = models.ManyToManyField(Genre)

    def __str__(self):
        return "Comment/Description: {} | Category: {} | User: {}".format(self.comment, self.category, self.user)
