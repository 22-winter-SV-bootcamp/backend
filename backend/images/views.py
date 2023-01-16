from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .tasks import ai_task
from django.http import JsonResponse
from .utils import get_image_url
import json

class Images(APIView):
    def get(self, request):
        return 

    def post(self, request):
        json_text = '{"file": "'+get_image_url(request.FILES.get('file'))+'"}'
        task = ai_task.delay(json.loads(json_text))
        return JsonResponse({"task_id": task.id})


