from django.http import JsonResponse
from rest_framework import status
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from images.models import image 
from .serializers import imageSerializer
from rest_framework.views import APIView

from .utils import get_image_url
from .tasks import ai_task
from .serializers import imageSerializer

import json


class Images(APIView):
    def get(self, request):
        if request.method == 'GET':
            pages = request.GET.get('page')
            recent_list = image.objects.all().order_by('-created_at')   #최근 이미지 별로 정렬
            link_list = recent_list.values('link')  # 모델에서 링크만 추출
            paginator = Paginator(link_list,5)  # 링크 5개씩 페이지네이션
        try:
            list = paginator.page(pages) # 보여줄 페이지는 쿼리스트링 값
            res = list.object_list
            serializer = imageSerializer(res, many=True)
            return JsonResponse(serializer.data,status=status.HTTP_200_OK, safe=False)
        # 예외 처리

        except PageNotAnInteger:    
            return JsonResponse({"Error":"Page must be Integer"},status=status.HTTP_404_NOT_FOUND)
        except EmptyPage:
            return JsonResponse({"Error":"Empty page"},status=status.HTTP_404_NOT_FOUND)
        


    def post(self, request):
        json_text = '{"file": "'+get_image_url(request.FILES.get('file'))+'"}'
        task = ai_task.delay(json.loads(json_text))
        return JsonResponse({"task_id": task.id})
