from django.contrib import admin
from mines_app.models import Post, Subscribe, User, Vote

# Register your models here.
admin.site.register(Post)
admin.site.register(Subscribe)
admin.site.register(User)
admin.site.register(Vote)
