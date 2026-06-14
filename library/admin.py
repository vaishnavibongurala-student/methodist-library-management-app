from django.contrib import admin

from .models import Book_Hub

from django.conf import settings
from django.core.mail import send_mail


@admin.action(description="Request Book")
def request_book(modeladmin, request, queryset):
	try:
	    for book in queryset:
	        book.request = True
	        book.save()

	        send_mail(
	            subject="Library Management - Book Request",
	            message=f"""
Hi Methodist Management,

Please approve book request from Methodist Library
Book: {book.title}
Author: {book.auther}

Requested by: {request.user.username}
Email: {request.user.email}
						""",
	            from_email=settings.EMAIL_HOST_USER,
	            recipient_list=["srujanapadakanti62001@gmail.com"],
	            fail_silently=False,
	        )
	except Exception as e:
		print(f"Exception {e}")

class Book_HubAdmin(admin.ModelAdmin):
    list_display = ['category', 'title', 'auther','count','request','edition','year','publisher']
    search_fields = ['category', 'title', 'auther','count','edition','year','publisher']
    list_filter = ['category', 'title', 'auther','count','edition','year','publisher']
    actions = [request_book]


admin.site.register(Book_Hub,Book_HubAdmin)
admin.site.site_header = "Methodist Library Administration"
admin.site.site_title = "Methodist Library Management"
admin.site.index_title = "Welcome to Methodist Library"