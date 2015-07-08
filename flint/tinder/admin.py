from django.contrib import admin

from .models import Profile, Preference, Comment
# Register your models here.
admin.site.register(Profile)
admin.site.register(Preference)
admin.site.register(Comment)
