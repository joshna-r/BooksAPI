from django.db.models.query import RawQuerySet
from API.serializers import BookSerializer, UserSerializer
from django.shortcuts import render
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

class Books(viewsets.ModelViewSet):
    queryset = book.objects.all()
    serializer_class = BookSerializer

class User(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

