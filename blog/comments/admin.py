from django.contrib import admin
from .models import Comment

# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'content', 'created_at')
    list_filter = ('user', 'post', 'created_at')
    search_fields = ('user', 'post', 'content')
    date_hierarchy = 'created_at'
    ordering = ('created_at',)