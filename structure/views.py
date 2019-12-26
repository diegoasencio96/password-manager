from django.shortcuts import render
from django.contrib.auth.models import User, Group
from .models import AccessCredential, Category
from .serializers import AccessCredentialSerializer, CategorySerializer
from rest_framework import viewsets
from structure.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class AccessCredentialViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = AccessCredential.objects.all()
    serializer_class = AccessCredentialSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
