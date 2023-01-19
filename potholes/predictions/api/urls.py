from django.contrib import admin
from django.urls import path, re_path, include

namespace = 'api'

urlpatterns = [
    re_path('v1/', include('predictions.api.v1.urls'))
]
