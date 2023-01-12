from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
import requests
from django.http import JsonResponse


class Images(APIView):
    def get(self, request):
        return 

    def post(self, request):
        img = request.FILES.get('file')
        r = requests.post('http://ai:8081/api/v1/images', files = {"file": img})
        ret = r.json()
        return JsonResponse({"ai_results":ret['ai_results']})