from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse


@api_view(['GET'])
def hi(request):
    return JsonResponse({"hi": "hi"})
