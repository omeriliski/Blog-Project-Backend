from django.contrib import admin
from .models import Category,Post,Like,Comment,PostView

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(PostView)
