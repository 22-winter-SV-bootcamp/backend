from collections import Counter
from uuid import uuid4
from django.http import JsonResponse
from django.shortcuts import render
from requests import Response
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
import datetime
# Create your views here.
qs_task = [
	openapi.Parameter(
        "gender",
        openapi.IN_QUERY,
        description="gender",
        type=openapi.TYPE_STRING,
        default=""
    )
]
class ShowStyleView(APIView):
    @swagger_auto_schema(operation_id='ranking',manual_parameters=qs_task,responses={
                status.HTTP_200_OK: 'Success',
                status.HTTP_404_NOT_FOUND: "Error"
            })
    def get(self, request):
        try:
            gender = request.GET.get('gender')
            end_date = datetime.datetime.today()                  
            start_date = end_date + datetime.timedelta(days=-7) 
            style_list = [
                style for style in style.objects.filter(created_at__range=(
                start_date, end_date)) if style.gender == gender
            ]
            list_cnt = []
            for a in style_list:
                list_cnt.append(str(a.top+a.top_color+a.bottom+a.bottom_color))
            cnt = Counter(list_cnt)
            rank = str(cnt.most_common(1))
            
            strip = "[""]"")""("
            wow = rank.strip(strip)
            sp = wow.replace('\'','').split(',')
            
            for b in style_list:
                if str(b.top+b.top_color+b.bottom+b.bottom_color) == sp[0]:
                    res = {
                        'gender':b.gender,
                        'top':b.top,
                        'top_color':b.top_color,
                        'bottom':b.bottom,
                        'bottom_color':b.bottom_color,
                        'count': sp[1].replace(' ','')
                        }
                    return JsonResponse(res,status=status.HTTP_200_OK)
                else:
                    raise Exception
            
        except:
            return JsonResponse({'Error':'gender name is not in db'},status=status.HTTP_404_NOT_FOUND)
        

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
            return JsonResponse({"link": url},status=status.HTTP_200_OK)

        except:       
            return JsonResponse({"Error":"problem with received form-data"},status=status.HTTP_404_NOT_FOUND)
        