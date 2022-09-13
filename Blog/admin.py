from django.contrib import admin

from .models import Blogs, Likes, Comments, Language,FrameWork,BlogCategory,RoadMap

admin.site.register(Blogs)
admin.site.register(BlogCategory)
admin.site.register(RoadMap)
admin.site.register(Language)
admin.site.register(FrameWork)
admin.site.register(Likes)
admin.site.register(Comments)