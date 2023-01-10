from django.shortcuts import render
import boto3
from backend.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME
from uuid import uuid4
from django.http import JsonResponse
from rest_framework.decorators import api_view


@api_view(['POST'])
def get_link(request):
    data = request.FILES.get('file')
    uuid = str(uuid4())
    s3_client = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY
    )
    s3_client.put_object(Body=data, Bucket=AWS_STORAGE_BUCKET_NAME, Key=uuid + ".jpg")
    url = "http://"+AWS_STORAGE_BUCKET_NAME+".s3.ap-northeast-2.amazonaws.com/" + \
                uuid + ".jpg"
    url = url.replace(" ", "/")
    return JsonResponse({"url": url})