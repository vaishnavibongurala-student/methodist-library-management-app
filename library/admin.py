from django.contrib import admin

from .models import Book_Hub,Patron

from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone
from datetime import timedelta


@admin.action(description="Request Book")
def request_book(modeladmin, request, queryset):
    try:
        for book in queryset:
            book.request = True
            book.save()

            # Create Patron record
            Patron.objects.create(
            patron=request.user.username,
            title=book.title,
            count="1",
            department=book.department,
            email=request.user.email,
            auther=book.auther,
            edition=book.edition,
            due_date=timezone.now()+timedelta(days=14)
            )
            
            send_mail(
                subject="Library Management - Book Request",
                message=f"""
Hi Methodist Management,

Please approve book request from Methodist Library
Book: {book.title}
Author: {book.auther}
Requested by: {request.user.username}
Email: {request.user.email}

Thanks & Regards,
{request.user.username}
                        """,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=["methodistlibrary123@gmail.com"],
                fail_silently=False,
            )
    except Exception as e:
        print(f"Exception {e}")

class Book_HubAdmin(admin.ModelAdmin):
    list_display = ['department', 'title', 'auther','count','request','edition','year','publisher']
    search_fields = ['department', 'title', 'auther','count','edition','year','publisher']
    list_filter = ['department', 'title', 'auther','count','edition','year','publisher']
    actions = [request_book]


class PatronAdmin(admin.ModelAdmin):
    list_display = ['patron', 'title', 'count','department','email','status','auther','edition','issued_date','due_date']
    search_fields = ['patron', 'title', 'count','department','email','status','auther','edition']
    list_filter = ['patron', 'title', 'count','department','email','status','auther','edition']


admin.site.register(Book_Hub,Book_HubAdmin)
admin.site.site_header = "Methodist Library Administration"
admin.site.site_title = "Methodist Library Management"
admin.site.index_title = "Welcome to Methodist Library"

admin.site.register(Patron,PatronAdmin)
