from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'body')
    search_fields = ('title',)


class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'post')


admin.site.register(Post, PostAdmin)
admin.site.register(Like, LikeAdmin)
