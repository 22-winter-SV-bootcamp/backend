from uuid import uuid4
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from backend.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME
from .serializers import *
from images.serializers import *
from .models import *
from rest_framework import status
from rest_framework.response import Response
import boto3
from images import views
import os
# Create your views here.

class ShowStyleView(APIView):
    def post(self,request):
        print("request",request)
        print("request.data: ",request.data)
        print("request.data의 타입: ",type(request.data))
        # link = request.data['img']
        # href = f'''
        # <html>
        # <body>
        #     <a href='img'>{link}</a>
        # </body>
        # </html>
        # '''
        # data = image.objects.filter(link=link)
        # serializer = imageSerializer(data)

        res = styleSerializer(data=request.data)
        if res.is_valid():
            res.save()
            
            data = request.FILES.get('img')
            file_type = os.path.splitext(data[1])   # 파일 확장자에 따라 url 생성
            uuid = str(uuid4())
            s3_client = boto3.client(
                's3',
                aws_access_key_id=AWS_ACCESS_KEY_ID,
                aws_secret_access_key=AWS_SECRET_ACCESS_KEY
            )
            s3_client.put_object(Body=data, Bucket=AWS_STORAGE_BUCKET_NAME, Key=uuid + file_type)
            url = "http://"+AWS_STORAGE_BUCKET_NAME+".s3.ap-northeast-2.amazonaws.com/" + \
                       uuid + file_type
            url = url.replace(" ", "/")
            img_link = image.objects.create(link=url)
            img_link.save()
            return JsonResponse({"url": url},status=200)
            
        else :
            return Response(res.errors,status=status.HTTP_400_BAD_REQUEST)
    
        