from django.urls import path
from . import views
 
urlpatterns = [ 
    path('', views.hello_world),
    path('hello-world', views.hello_world_json),
]
