from django.contrib import admin
from .models import Category

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'slug')
    list_filter = ('published',)
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}