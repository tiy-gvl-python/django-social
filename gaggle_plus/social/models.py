from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Guser(models.Model):
    user = models.ForeignKey(User)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    gender = models.CharField(max_length=1, empty=True)
    birthday = models.DateField(null=True)
    creation = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Connection(models.Model):
    owner = models.ForeignKey(Guser)
    connection = models.ForeignKey(Guser)
    circle = models.CharField(max_length=50)
    creation = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} is in {}'s {} circle.".format(self.connection, self.owner, self.circle)


class Post(models.Model):
    guser = models.ForeignKey(Guser)
    data = models.CharField(max_length=1000)
    parent_post = models.ForeignKey("Post", null=True)
    public = models.BooleanField(default=True)
    creation = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "id: {}; poster: {}".format()


class Plus(models.Model):
    post = models.ForeignKey(Post)
    guser = models.ForeignKey(Guser)
    creation = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    post = models.ForeignKey(Post)
    tagger = models.ForeignKey(guser)
    guser = models.ForeignKey(guser)
    creation = models.DateTimeField(auto_now=True)


class PostCircle(models.Model):
    circle = models.ForeignKey(Connection)
    post = models.ForeignKey(Post)
