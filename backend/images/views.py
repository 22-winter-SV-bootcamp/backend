from django.http import HttpResponse, JsonResponse
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
        except PageNotAnInteger:    
            list = paginator.page(1) # 예외값이 들어오면 첫페이지로
        except EmptyPage:
            list = paginator.page(paginator.num_pages) # 빈 페이지면 마지막 페이지로
        
        res = list.object_list
        serializer = imageSerializer(res, many=True)
        return JsonResponse(serializer.data, safe=False)
