from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile, Report
from datetime import datetime


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['username', 'password', 'is_active', 'is_staff', 'date_joined', 'last_login']
#         read_only_fields = ['is_active', 'is_staff', 'date_joined', 'last_login']


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Profile
        fields = '__all__'
        read_only_fields = ['games_played', 'games_won', 'rounds_played', 'rounds_won', 'score']


class ReportSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    report_datetime = serializers.DateTimeField(default=datetime.now(), style={'input_type': 'hidden'})

    class Meta:
        model = Report
        fields = '__all__'
