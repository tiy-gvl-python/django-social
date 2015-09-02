from django.contrib import admin

# Register your models here.
from potinbbob1.models import Pic
from potinbbob1.models import UserProfile
from potinbbob1.models import Genre
from potinbbob1.models import Collection

admin.site.register(Pic)
admin.site.register(UserProfile)
admin.site.register(Genre)
admin.site.register(Collection)
