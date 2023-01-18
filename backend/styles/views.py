from uuid import uuid4
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from backend.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME
from .serializers import *
from images.serializers import *
from .models import *
from rest_framework import status
from rest_framework.response import Response
import boto3
import os
# Create your views here.

class ShowStyleView(APIView):
    def post(self,request):
        try:
            data = request.FILES.get('img')
            file_type = os.path.splitext(str(data))[1]   # 파일 확장자에 따라 url 생성
            uuid = str(uuid4())
            s3_client = boto3.client(
                's3',
                aws_access_key_id=AWS_ACCESS_KEY_ID,
                aws_secret_access_key=AWS_SECRET_ACCESS_KEY
            )
            s3_client.put_object(Body=data, Bucket=AWS_STORAGE_BUCKET_NAME, Key=uuid + file_type)    # 버킷에 이미지 저장
            url = "http://"+AWS_STORAGE_BUCKET_NAME+".s3.ap-northeast-2.amazonaws.com/" + \
                uuid + file_type
            url = url.replace(" ", "/")

            image.objects.create(link=url)
            style_info = style(gender = request.POST['gender'],top=request.POST['top'],top_color=request.POST['top_color'],bottom=request.POST['bottom'],bottom_color=request.POST['bottom_color']
            ,image_id=image.objects.get(link=url))
    
            style_info.save()
            return JsonResponse({"url": url},status=200)

        except:       
            return Response(style_info.errors,status=status.HTTP_404_NOT_FOUND)
        