from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import FeatureFlag


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username')


class FeatureToggleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FeatureFlag
        fields = ('feature_key', 'feature_value')
