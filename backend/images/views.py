
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from .utils import get_image_url
from .tasks import ai_task
from .serializers import imageSerializer

import json

class Images(APIView):
    def get(self, request):
        return 

    def post(self, request):
        json_text = '{"file": "'+get_image_url(request.FILES.get('file'))+'"}'
        task = ai_task.delay(json.loads(json_text))
        return JsonResponse({"task_id": task.id})
