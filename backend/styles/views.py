from uuid import uuid4
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from rest_framework import status
from images.utils import get_image_url
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.parsers import MultiPartParser
from django.core.cache import cache
from .ranking import get_ranking

# Create your views here.
responses = {status.HTTP_200_OK: 'Success', status.HTTP_404_NOT_FOUND: "Error"}

class ShowStyleView(APIView):
    qs_task = [openapi.Parameter("gender", openapi.IN_QUERY, description="gender 입력", type=openapi.TYPE_STRING)]
    @swagger_auto_schema(operation_id='ranking',manual_parameters=qs_task,responses=responses)
    
    def get(self, request):
        try:
            gender = request.GET.get('gender')
            res = cache.get(gender)
            if res == 'except':
                raise Exception
            return JsonResponse(res,status=status.HTTP_200_OK)
        except:
            return JsonResponse({'Error':'gender name is not in db'},status=status.HTTP_404_NOT_FOUND)
        
    qs_custom = [openapi.Parameter('file', openapi.IN_FORM, type=openapi.TYPE_FILE, description='image 입력'),
                 openapi.Parameter('gender', openapi.IN_FORM, type=openapi.TYPE_STRING),
                 openapi.Parameter('top', openapi.IN_FORM, type=openapi.TYPE_STRING),
                 openapi.Parameter('top_color', openapi.IN_FORM, type=openapi.TYPE_STRING),
                 openapi.Parameter('bottom', openapi.IN_FORM, type=openapi.TYPE_STRING),
                 openapi.Parameter('bottom_color', openapi.IN_FORM, type=openapi.TYPE_STRING)]
    parser_classes = [MultiPartParser]
    @swagger_auto_schema(operation_id='custom image 링크', manual_parameters=qs_custom,responses=responses)
    
    def post(self,request): 
        try:
            gender = request.POST['gender'] 
            data = request.FILES.get('file')
            url = get_image_url(data)

            style_info = style(gender = request.POST['gender'],top=request.POST['top'],
            top_color=request.POST['top_color'],bottom=request.POST['bottom'],
            bottom_color=request.POST['bottom_color'],image_id=image.objects.create(link=url))
            style_info.save()
            
            res = get_ranking(gender)
            if cache.get(gender) != res:                    # 이전 랭킹하고 다르면 업데이트
                cache.set(gender,res,60*60)       
            return JsonResponse({"link": url},status=status.HTTP_200_OK)

        except:       
            return JsonResponse({"Error":"problem with received form-data"},status=status.HTTP_404_NOT_FOUND)
        