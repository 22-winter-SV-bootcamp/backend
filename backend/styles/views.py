from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from .serializers import *
from styles.models import style
from rest_framework import status
from rest_framework.response import Response
# Create your views here.
class ResultView(APIView):
    def post(self,request):
        print("request",request)
        print("request.data: ",request.data)
        print("request.data의 타입: ",type(request.data))
        res = styleSerializer(data=request.data)
        if res.is_valid():
            return Response(res.data,status=status.HTTP_200_OK)
        else :
            return Response(res.errors,status=status.HTTP_400_BAD_REQUEST)