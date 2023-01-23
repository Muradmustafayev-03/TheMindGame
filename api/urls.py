from rest_framework import routers
from django.urls import path, include
from api.views import ProfileAPIViewSet, ReportAPIViewSet  # , UserAPIViewSet

router = routers.DefaultRouter()
# router.register(r'users', UserAPIViewSet)
router.register(r'profiles', ProfileAPIViewSet)
router.register(r'reports', ReportAPIViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
