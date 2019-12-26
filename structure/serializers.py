from django.contrib.auth.models import User, Group
from .models import Category, AccessCredential
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'url', 'name')


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class AccessCredentialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AccessCredential
        fields = ('id', 'name', 'url', 'email', 'username', 'password', 'pin', 'category')