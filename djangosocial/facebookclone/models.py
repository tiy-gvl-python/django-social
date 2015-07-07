from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db.models import ForeignKey, TextField


class Tag(models.Model):
    user = ForeignKey(User, related_name="Tagger")
    pub_date = models.DateField(auto_now=True)
    tagged = ForeignKey(User, related_name="Tagged")
    status = ForeignKey("Status")

    def __str__(self):
        return "User: {} - Friend: {} - Tagged In: {}".format(self.user,self.tagged, self.status)


class Friend(models.Model):
    user = ForeignKey(User, related_name="CUser")
    pub_date = models.DateField(auto_now=True)
    friend = ForeignKey(User, related_name="friend")

    def __str__(self):
        return "User: {} - Friend: {}".format(self.user,self.friend)


class Status(models.Model):
    user = ForeignKey(User)
    parent = ForeignKey("Status", null=True)
    message = TextField()
    pub_date = models.DateField(auto_now=True)

    def __str__(self):
        return "User: {} - Status: {}".format(self.user,self.message)


class Like(models.Model):
    user = ForeignKey(User)
    status = ForeignKey(Status)
    pub_date = models.DateField(auto_now=True)

    def __str__(self):
        return "User: {} - Status Liked: {}".format(self.user, self.status)

