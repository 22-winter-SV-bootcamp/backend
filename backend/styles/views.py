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
from drf_yasg import openapi
from rest_framework.parsers import MultiPartParser
# Create your views here.

class ShowStyleView(APIView):
    parser_classes = [MultiPartParser]
    @swagger_auto_schema(
            operation_id='task_id',
            manual_parameters=[
                openapi.Parameter('file', openapi.IN_FORM, type=openapi.TYPE_FILE, description='image to be uploaded'),
                openapi.Parameter('gender', openapi.IN_FORM, type=openapi.TYPE_STRING),
                openapi.Parameter('top', openapi.IN_FORM, type=openapi.TYPE_STRING),
                openapi.Parameter('top_color', openapi.IN_FORM, type=openapi.TYPE_STRING),
                openapi.Parameter('bottom', openapi.IN_FORM, type=openapi.TYPE_STRING),
                openapi.Parameter('bottom_color', openapi.IN_FORM, type=openapi.TYPE_STRING),
            ],
            responses={
                status.HTTP_200_OK: 'Success',
                status.HTTP_404_NOT_FOUND: "Error"}
                )
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
        