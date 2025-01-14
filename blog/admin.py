from django.contrib import admin
from .models import Blog, Like, Comment, Note


class Blogadmin(admin.ModelAdmin):
    list_display = ['id', "title", "image", "created_at"]
    list_filter = ["created_at"]
    search_fields = ["title", "content"]

admin.site.register(Blog, Blogadmin)


class Likeadmin(admin.ModelAdmin):
    list_display = ['id', 'like', 'blog', 'created_at']
    list_filter = ['created_at']

admin.site.register(Like, Likeadmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'blog', 'created_at']
    list_filter = ['created_at']
    search_fields = ['content']

admin.site.register(Comment, CommentAdmin)

class NoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title','content']

admin.site.register(Note, NoteAdmin)