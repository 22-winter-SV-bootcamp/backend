from django.http import JsonResponse
from rest_framework import status
from django.shortcuts import render
from requests import Response
from rest_framework.decorators import api_view
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from images.models import image 
from .serializers import imageSerializer

@api_view(['GET'])
def recentImage(request):
    if request.method == 'GET':

        pages = request.GET.get('page')
        recent_list = image.objects.all().order_by('-created_at')   #최근 이미지 별로 정렬
        link_list = recent_list.values('link')  # 모델에서 링크만 추출
        paginator = Paginator(link_list,5)  # 링크 5개씩 페이지네이션
        
        try:
            list = paginator.page(pages) # 보여줄 페이지는 쿼리스트링 값
            res = list.object_list
            serializer = imageSerializer(res, many=True)
            # if serializer.is_valid():
            return JsonResponse(serializer.data,status=status.HTTP_200_OK, safe=False)
        # 예외 처리
        except PageNotAnInteger:    
            return Response(status=status.HTTP_404_NOT_FOUND)
        except EmptyPage:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        
        
        
