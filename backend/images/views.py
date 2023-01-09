from django.http import HttpResponse
from django.shortcuts import render
from .models import ResultImage

# Create your views here.
def index(request):
    list = ResultImage.objects.all()
  
    
    article = f'''
        <h1> 
            {ResultImage.objects.get(id='1').uuid}
            {ResultImage.objects.get(id='2').link}
        </h1>
        '''
    
    return HttpResponse(article) 