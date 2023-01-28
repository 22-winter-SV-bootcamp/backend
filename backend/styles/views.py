
from uuid import uuid4
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from backend.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME
from .models import *
from rest_framework import status
from images.utils import get_image_url
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.parsers import MultiPartParser
from django.core.cache import cache
from .ranking import get_ranking

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
            res = cache.get(gender)
            if res is 'except':
                raise Exception
            return JsonResponse(res,status=status.HTTP_200_OK)
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
            gender = request.POST['gender'] 
            data = request.FILES.get('file')
            url = get_image_url(data)
            
            image.objects.create(link=url)
            style_info = style(gender = request.POST['gender'],top=request.POST['top'],top_color=request.POST['top_color'],bottom=request.POST['bottom'],bottom_color=request.POST['bottom_color']
            ,image_id=image.objects.get(link=url))
            style_info.save()
            
            res = get_ranking(gender)
            if cache.get(gender) != res:                    # 이전 랭킹하고 다르면 업데이트
                cache.set(gender,res,60*60)       
            return JsonResponse({"link": url},status=status.HTTP_200_OK)

        except:       
            return JsonResponse({"Error":"problem with received form-data"},status=status.HTTP_404_NOT_FOUND)
        