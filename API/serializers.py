from django.db.models import fields
from rest_framework import serializers
from .models import *

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = book
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
        # fields = ['first_name', 'last_name', 'email', 'password', 'book_title', 'wishlist']
        # depth=1

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['Total_wishlist'] = instance.wishlist.count()

        return representation 









