from django.contrib import admin

from .models import Post, Comment, File

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(File)