from rest_framework import serializers
from .models import Book_Hub

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book_Hub
        fields = "__all__"