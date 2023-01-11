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
        
        # 커스텀 내용 db 저장 
        # reqData = request.data
        # gender = reqData['gender']
        # top = reqData['top']
        # top_color = reqData['top_color']
        # bottom
        res = styleSerializer(data=request.data)
        if res.is_valid():
            res.save()
            # return Response(이미지 링크)
             
        
            # return HttpResponse(href)
            # s3 bucket에 파일 보내서 이미지 반환받기
            # return Response(이미지 링크)
            data = request.FILES.get('img')
            uuid = str(uuid4())
            s3_client = boto3.client(
                's3',
                aws_access_key_id=AWS_ACCESS_KEY_ID,
                aws_secret_access_key=AWS_SECRET_ACCESS_KEY
            )
            s3_client.put_object(Body=data, Bucket=AWS_STORAGE_BUCKET_NAME, Key=uuid + ".jpg")
            url = "http://"+AWS_STORAGE_BUCKET_NAME+".s3.ap-northeast-2.amazonaws.com/" + \
                       uuid + ".jpg"
            url = url.replace(" ", "/")
            return JsonResponse({"url": url},status=200)
            
            # 임의 이미지 링크 반환
            
        else :
            return Response(res.errors,status=status.HTTP_400_BAD_REQUEST)
    
        