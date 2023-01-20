from django.contrib import admin
from django.urls import path, re_path, include

from rest_framework.authtoken import views

namespace = 'api'

urlpatterns = [
    re_path('v1/', include('predictions.api.v1.urls')),
    path('token-auth/', views.obtain_auth_token)
]
