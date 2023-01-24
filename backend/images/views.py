from django.http import JsonResponse
from celery.result import AsyncResult
from rest_framework import status
from django.shortcuts import render
from rest_framework.decorators import api_view
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from images.models import image 
from .serializers import imageSerializer
from rest_framework.views import APIView
from .utils import get_image_url
from .tasks import ai_task
from .serializers import imageSerializer
from images.result import task_result
import json
from celery.exceptions import TimeoutError
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.parsers import MultiPartParser

from django.core.cache import cache
import redis


qs_page = [
	openapi.Parameter(
        "page",
        openapi.IN_QUERY,
        description="page",
        type=openapi.FORMAT_DATE,
        default=""
    )
]
qs_task = [
	openapi.Parameter(
        "task_id",
        openapi.IN_QUERY,
        description="task",
        type=openapi.TYPE_STRING,
        default=""
    )
]

class Images(APIView):
    @swagger_auto_schema(operation_id='recent image',manual_parameters=qs_page,responses={
                status.HTTP_200_OK: 'Success',
                status.HTTP_404_NOT_FOUND: "Error"
            })
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
    
    parser_classes = [MultiPartParser]
    @swagger_auto_schema(
            operation_id='task_id',
            manual_parameters=[
                openapi.Parameter('file', openapi.IN_FORM, type=openapi.TYPE_FILE, description='image to be uploaded'),
            ],
            responses={
                status.HTTP_200_OK: 'Success',
                status.HTTP_404_NOT_FOUND: "Error"
            }
        )
    def post(self, request):
        json_text = '{"file": "'+get_image_url(request.FILES.get('file'))+'"}'
        task = ai_task.delay(json.loads(json_text))
        print(task)
        return JsonResponse({"task_id": task.id})


@swagger_auto_schema(operation_id='task_result',method='get',manual_parameters=qs_task,responses={
                status.HTTP_200_OK: 'Success',
                status.HTTP_404_NOT_FOUND: "Error"
            })
@api_view(['GET'])
def get_task(request):
    
    if request.method == 'GET':
        try:
            r = redis.Redis(host='redis',port=6379,decode_responses=True)
            task_id = request.GET.get('task_id')
            task = AsyncResult(task_id)
            is_task = False
            
            for i in r.keys():                             # 있는 task인지 확인
                a = r.get(i).split('"task_id": "')         # r.get(i) 타입은 스트링
                print(r.get(i))
                print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
                if task_id == a[1][:-2]:
                    is_task = True
            if is_task == False:
                raise Exception()
            
            if task.ready():                          
                with open('images/sort/bottom.txt') as f:
                    bot = f.read().splitlines()
                    bot_def = bot[bot.index('slacks')]
                with open('images/sort/top.txt') as g:
                    top = g.read().splitlines()
                    top_def = top[top.index('t-shirts')]  
            
                to_list = list(task.result.values())       # dict -> list 
                to_str = ' '.join(to_list)                 # list -> string
                lists = to_str.split()                     # string -> list
                dict = {string:i for i, string in enumerate(lists)}     # confidence별로 dict의 value값 지정 (낮을수록 높은 confidence)
                bot_list = []
                top_list = []    

                try:
                    for key in dict:
                        if key in bot:
                            bot_list.append(key)
                        elif key in top:
                            top_list.append(key)
                
                    large_top = top_list[0]             # 항상 0번째 인덱스값이 가장 높은 컨피던스를 가짐
                    large_bot = bot_list[0]             # ""
                
                except:                                 # ai가 인식못했을때
                    if not top_list and bot_list: 
                        large_top = top_def
                        large_bot = bot_list[0]
                    
                    elif top_list and not bot_list:
                        large_top = top_list[0]
                        large_bot = bot_def
                    else:
                        large_top = top_def
                        large_bot = bot_def
                    
                finally:
                    res = task_result('done',{'top' : large_top, 'bottom' : large_bot})
                    return JsonResponse(res,status=200)
            else:                           # task가 안끝났을때
                res = task_result('Not yet')    
                return JsonResponse(res,status=404)
        except:                             # 없는 task_id일때
            res = task_result('task does not exist')    
            return JsonResponse(res,status=404)
            
