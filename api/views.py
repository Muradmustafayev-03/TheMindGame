from django.db import IntegrityError
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer


class ProfileAPIViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def create(self, request, *args, **kwargs):
        try:
            super().create(request, args, kwargs)
        except IntegrityError as e:
            if 'UNIQUE constraint failed: api_profile.user_id' in e.args:
                return Response({'error': 'current user already has the profile'})
            else:
                return Response({'error': e.args})
