from django.urls import path, include
from rest_framework import routers
from .views import CaseViewSet

namespace = 'v1'

router = routers.DefaultRouter()
router.register(r'case', CaseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
