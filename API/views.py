from typing import List
from django.db.models.query import QuerySet, RawQuerySet
from API.serializers import *
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .models import *
from rest_framework.generics import CreateAPIView, DestroyAPIView, UpdateAPIView 

class Books(viewsets.ModelViewSet):
    queryset = book.objects.all()
    serializer_class = BookSerializer

class User(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


