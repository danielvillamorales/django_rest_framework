from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'category', 'published')
    list_filter = ('published', 'category', 'user')
    search_fields = ('title', 'user__username', 'category__title')
    date_hierarchy = 'created_at'
    ordering = ('published', 'created_at')