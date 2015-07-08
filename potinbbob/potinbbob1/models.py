from django.db import models

# Create your models here.

class Pics(models.Model):
    comment = models.CharField(max_length=60)
    time_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    category = models.CharField(max_length=100)
    user = models.CharField(max_length=25)
    link_to_origin = models.CharField(max_length=150)
    origin_info = models.CharField(max_length=35)
    humor = models.BooleanField(default=False)
    instructional = models.BooleanField(default=False)
    sappy = models.BooleanField(default=False)
    sad = models.BooleanField(default=False)

    def __str__(self):
        return "Comment/Description: {} | Category: {} | User: {}".format(self.comment, self.category, self.user)


class User(models.Model):
    full_name = models.CharField(max_length=25)
    email = models.EmailField()
    user_name = models.CharField(max_length=25)
    website = models.CharField(max_length=150)
    location = models.CharField(max_length=30)

    def __str__(self):
       return str(self.user_name)


class Category(models.Model):
    title = models.CharField(max_length=25)
    comment = models.CharField(max_length=60)
    user = models.CharField(max_length=25)

    def __str__(self):
       return "Title: {} | Comment: {} | User: {}".format(self.title, self.comment, self.user)