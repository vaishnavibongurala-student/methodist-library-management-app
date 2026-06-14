from django.shortcuts import render


from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Book_Hub
from .serializers import BookSerializer

@api_view(['GET'])
def books(request):
    books = Book_Hub.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)
