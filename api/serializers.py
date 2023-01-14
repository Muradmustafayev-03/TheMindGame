from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile, Report


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'is_active', 'is_staff']
        read_only_fields = ['is_active', 'is_staff']


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Profile
        fields = '__all__'
        read_only_fields = ['games_played', 'games_won', 'rounds_played', 'rounds_won', 'score']
