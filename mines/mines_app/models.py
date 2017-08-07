from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=20)
    subscribers = models.ForeignKey('Subscribe')

    def __str__(self):
        return "{}-{}".format(self.name, self.subscribers.subscriptions)


class Vote(models.Model):
    bool = models.BooleanField()
    posts = models.ForeignKey('Post')

    def __str__(self):
        return "{}-{}".format(self.bool, self.posts.id)


class Post(models.Model):
    user = models.ForeignKey('User')
    content = models.CharField(max_length=50)

    def __str__(self):
        return "{}-{}".format(self.user.name, self.content)


class Group(models.Model):
    user = models.ForeignKey('User')
    content = models.TextField(max_length=50)
    related_comments = models.ForeignKey('Post')
    related_votes = models.ForeignKey('Vote')

    def __str__(self):
        return "{}-{}-{}-{}".format(self.user.name, self.content, self.related_comments.content, self.related_votes.bool)


class Subscribe(models.Model):
    subscriptions = models.TextField()

    def __str__(self):
        return "{}".format(self.subscriptions)
