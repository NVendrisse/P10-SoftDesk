from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from authentification.serializer import UserSerializer
from authentification.models import User
from django.contrib.auth import get_user_model

User = get_user_model()


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()
