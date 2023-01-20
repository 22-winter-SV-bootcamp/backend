from django.shortcuts import render
from rest_framework.decorators import api_view

from django.http import JsonResponse

import os, torch, requests
from PIL import Image
from io import BytesIO

@api_view(['POST'])
def get_ai_result(request):
    res = requests.get(request.data.get("file"))
    img = Image.open(BytesIO(res.content))

    # img = Image.open(io.BytesIO(request.FILES.get('file').read()))
    hubconfig = os.path.join(os.getcwd(), 'images', 'yolov5')
    weightfile = os.path.join(os.getcwd(), 'images', 'yolov5',
                              'runs', 'train', 'clothesClassification', 'weights', 'best.pt')
    model = torch.hub.load(hubconfig, 'custom', path=weightfile, source='local')

    results = model(img)
    # print(results)
    results.render()
    # print(results)
    results_dict = results.pandas().xyxy[0].to_dict(orient="records")
    # print(results_dict)
    if not results_dict:
        return JsonResponse({"ai_results": "none"})
    else:
        ai_results = []
        for result in results_dict:
            if result.get('name') not in ai_results:
                print(result.get('class'))
                ai_results.append(result.get('name'))
    return JsonResponse({"ai_results":' '.join(ai_results)})
