from django.contrib import admin
from django.urls import path, re_path, include

from .views import CaseViewSet

namespace = 'v1'

urlpatterns = [
    re_path('case', CaseViewSet.as_view({'post':'create'}))
]
