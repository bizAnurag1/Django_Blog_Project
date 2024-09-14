from django.contrib import admin
from django.http import HttpRequest
from .models import Blog, Author, Comment

class BlogInLines(admin.TabularInline):
    model = Blog
    extra = 0
    fields = ['title']
    readonly_fields = [field.name for field in Blog._meta.get_fields()]

    def has_delete_permission(self, request, obj = None):
        return False

class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['name', 'email']
    inlines = [BlogInLines,]


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    list_filter = ('author', 'date')
    list_per_page = (5)
    search_fields = ['title', 'author__name', 'author__email']
    autocomplete_fields = ['author']
    search_help_text = "Search the blog by Title and Author name."
    fields = ('title', 'author', 'blog_text')
    #readonly_fields = ['title']

# Register your models here.
admin.site.register(Blog, BlogAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Comment)