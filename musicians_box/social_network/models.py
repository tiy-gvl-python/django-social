from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class CommonUser(models.model):
    user = models.OneToOneField(User)
    location = models.CharField(max_length=100)
    age = models.IntegerField()
    sex = models.CharField(max_length=1)
    message = models.OneToOneField('Message')

    def __str__(self):
        return "{} is not a musician".format(self.user)


class Musician(CommonUser):
    video = models.CharField(max_length=300)
    genre = models.ManyToManyField('Genre')
    instrument = models.ManyToManyField('Instrument')

    def __str__(self):
        return "{} is a musician".format(self.user)


class Genre(models.model):
    genre = models.CharField(max_length=20)

    def __str__(self):
        return '{}'.format(self.genre)


class Instrument(models.model):
    instrument = models.CharField(max_length=20)

    def __str__(self):
        return '{}'.format(self.instrument)


class Video(models.model):
    musician = models.OneToOneField(Musician)
    genre = models.ManyToManyField(Genre)
    instrument = models.ManyToManyField(Instrument)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return 'Musician: {}, Date: {}'.format(self.musician, self.date_created)


class Forum(models.model):
    tags = models.ManyToManyField('Tags')
    topic = models.CharField(max_length=40)
    post = models.TextField

    def __str__(self):
        return 'Topic: {} Post: {}'.format(self.topic, self.post)


class Message(models.model):
    sender = models.OneToOneField(CommonUser)
    recipient = models.ManyToManyField(CommonUser)

    def __str__(self):
        return 'Sender: {} \n Recipient(s): {}'.format(self.sender, self.recipient)