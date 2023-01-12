from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView



class Images(APIView):
    def get(self, request):
        return 

    def post(self, request):
        img = request.FILES.get('file')
        
        return