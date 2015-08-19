from django.contrib import admin

# Register your models here.
from facebookclone.models import Tag, Friend, Status, Like

admin.site.register(Tag),
admin.site.register(Friend),
admin.site.register(Status),
admin.site.register(Like),