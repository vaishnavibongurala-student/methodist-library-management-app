from django.contrib import admin

from .models import Library

class LibraryAdmin(admin.ModelAdmin):
    list_display = ['category', 'title', 'auther']
    search_fields = ['category', 'title', 'auther']
    list_filter = ['category', 'title', 'auther']


admin.site.register(Library,LibraryAdmin)