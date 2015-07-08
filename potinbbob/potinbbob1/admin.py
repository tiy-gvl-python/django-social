from django.contrib import admin

# Register your models here.
from potinbbob1.models import Pics
from potinbbob1.models import User
from potinbbob1.models import Category

admin.site.register(Pics)
admin.site.register(User)
admin.site.register(Category)
