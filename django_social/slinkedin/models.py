from django.db import models

#Contains user profile information
class User(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    employment = models.CharField(max_length=100)
    education = models.CharField(max_length=100)
    experience = models.TextField()
    skills = models.TextField()
    messages = models.TextField()
    posts = models.TextField()
    invitation = models.CharField(max_length=100)

class Connection(models.Model):
    #Users can have multiple connections to different people
    connection = models.ForeignKey(User)
    colleagues = models.CharField(max_length=100)

class Job(models.Model):
    #Possibly a many to many.
    # Users can see multiple jobs and jobs can have multiple users see that job
    jobs = models.ForeignKey(User)
    post_job = models.TextField()

class Company(models.Model):
    companies = models.ForeignKey(Job)

class Group(models.Model):
    # this might be a many to many as well
    # a group can have multiple companies, and a company could belong to multiple groups
    group = models.ForeignKey(Company)
    discussion = models.CharField(max_length=100)
    members = models.CharField(max_length=100)

class Pulse(models.Model):
    recommendation = models.ForeignKey(User)
    articles = models.TextField()
    like = models.BooleanField()
    comment = models.TextField()

class School(models.Model):
    education = models.ForeignKey(User)
    school_ranking = models.IntegerField()
    field_of_study = models.CharField(max_length=100)
    employment = models.CharField(max_length=100)


