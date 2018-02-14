from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from toggles.serializers import UserSerializer, FeatureToggleSerializer
from .models import FeatureFlag


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class FeatureToggleViewSet(viewsets.ModelViewSet):
    queryset = FeatureFlag.objects.all()
    serializer_class = FeatureToggleSerializer
