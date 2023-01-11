from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view

@api_view(['GET'])
def hello_world(request):
    if request.method == 'GET':
        return HttpResponse("Hello World!")


@api_view(['GET'])
def hello_world_json(request):
    if request.method == 'GET':
        return JsonResponse({"baraa says": "hello world!"})