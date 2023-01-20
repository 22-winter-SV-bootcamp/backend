from uuid import uuid4
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from backend.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME
from .serializers import *
from images.serializers import *
from .models import *
from rest_framework import status
from images.utils import get_image_url
from drf_yasg.utils import swagger_auto_schema


# Create your views here.

class ShowStyleView(APIView):
    @swagger_auto_schema(operation_id='customizing',query_serializer=styleSerializer, responses={200:'SUCCESS',404:'Error'})
    def post(self,request):
        try:
            data = request.FILES.get('file')
            url = get_image_url(data)

            image.objects.create(link=url)
            style_info = style(gender = request.POST['gender'],top=request.POST['top'],top_color=request.POST['top_color'],bottom=request.POST['bottom'],bottom_color=request.POST['bottom_color']
            ,image_id=image.objects.get(link=url))
    
            style_info.save()
            return JsonResponse({"link": url},status=200)

        except:       
            return JsonResponse({"Error":"problem with received form-data"},status=status.HTTP_404_NOT_FOUND)
        