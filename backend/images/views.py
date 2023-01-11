from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import imageSerializer
class ImageCreateView(APIView):
    def post(self,request):
        print("request",request)
        print("request.data: ",request.data)
        print("request.data의 타입: ",type(request.data))
        res = imageSerializer(data=request.data)
        if res.is_valid():
            res.save()
            return Response(res.data,status=status.HTTP_200_OK)
        else :
            return Response(res.errors,status=status.HTTP_400_BAD_REQUEST)

