from django.http import JsonResponse
from celery.result import AsyncResult
from rest_framework import status
from rest_framework.decorators import api_view
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from images.models import image 
from .serializers import imageSerializer
from rest_framework.views import APIView
import json
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.parsers import MultiPartParser
from django.core.cache import cache
from .utils import get_image_url, is_task_exist, get_task_result, get_sort_list, classify, get_dict
from .tasks import ai_task

responses={status.HTTP_200_OK: 'Success', status.HTTP_404_NOT_FOUND: "Error"}

class Images(APIView):
    qs_page = [openapi.Parameter("page", openapi.IN_QUERY, description="최근이미지 링크 반환", type=openapi.FORMAT_DATE)]
    @swagger_auto_schema(operation_id='recent image',manual_parameters=qs_page,responses=responses)
    
    def get(self, request):
        pages = request.GET.get('page')
        recent_list = image.objects.all().order_by('-created_at')   #최근 이미지 별로 정렬
        link_list = recent_list.values('link')                      # 모델에서 링크만 추출
        paginator = Paginator(link_list,5)                          # 링크 5개씩 페이지네이션
        try:
            list = paginator.page(pages)                            # 보여줄 페이지는 쿼리스트링 값
            res = list.object_list
            serializer = imageSerializer(res, many=True)
            return JsonResponse(serializer.data,status=status.HTTP_200_OK, safe=False)
        except PageNotAnInteger:    
            return JsonResponse({"Error":"Page must be Integer"},status=status.HTTP_404_NOT_FOUND)
        except EmptyPage:
            return JsonResponse({"Error":"Empty page"},status=status.HTTP_404_NOT_FOUND)
    
    parser_classes = [MultiPartParser]
    qs_img = [openapi.Parameter('file', openapi.IN_FORM, type=openapi.TYPE_FILE, description='task_id 반환')]
    @swagger_auto_schema(operation_id='task_id', manual_parameters=qs_img, responses=responses)
    
    def post(self, request):
        file = request.FILES.get('file')
        
        if not cache.get(file):
            json_text = '{"file": "'+get_image_url(file)+'"}'
            task = ai_task.delay(json.loads(json_text))
            cache.set(file, task.id)

        return JsonResponse({"task_id": cache.get(file)})


qs_task = [openapi.Parameter("task_id", openapi.IN_QUERY, description="ai 처리 결과 반환", type=openapi.TYPE_STRING)]
@swagger_auto_schema(operation_id='task_result',method='get',manual_parameters=qs_task,responses=responses)
@api_view(['GET'])

def get_task(request,task_id):
    try:
        task = AsyncResult(task_id)
        is_task = is_task_exist(task_id)
        if is_task == False:
            raise Exception()
        
        if task.ready():            
            dict = get_dict(task)
            large_top,large_bot = classify(dict, get_sort_list('top'), get_sort_list('bottom'))
            res = get_task_result('done',{'top' : large_top, 'bottom' : large_bot})
            return JsonResponse(res,status=200)
        elif not task.ready():                           # task가 안끝났을때
            res = get_task_result('Not yet')    
            return JsonResponse(res,status=404)
    except:                                            # 없는 task_id일때
        res = get_task_result('task does not exist')    
        return JsonResponse(res,status=404)