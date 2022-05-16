from django.contrib import admin

from .models import Blogs, Likes, Comments

admin.site.register(Blogs)
admin.site.register(Likes)
admin.site.register(Comments)