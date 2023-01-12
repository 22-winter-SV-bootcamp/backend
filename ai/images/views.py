from django.shortcuts import render
from rest_framework.decorators import api_view

from django.http import JsonResponse

import io, os, torch
from PIL import Image

@api_view(['POST'])
def get_ai_result(request):
    img = Image.open(io.BytesIO(request.FILES.get('file').read()))

    hubconfig = os.path.join(os.getcwd(), 'images', 'yolov5')
    weightfile = os.path.join(os.getcwd(), 'images', 'yolov5',
                              'runs', 'train', 'clothesClassification', 'weights', 'best.pt')
    model = torch.hub.load(hubconfig, 'custom', path=weightfile, source='local')

    results = model(img)
    results.render()
    results_dict = results.pandas().xyxy[0].to_dict(orient="records")
    if not results_dict:
        return JsonResponse({"ai_results":"0"})
    else:
        ai_results = []
        for result in results_dict:
            if result.get('name') not in ai_results:
                ai_results.append(result.get('name'))
    return JsonResponse({"ai_results": ' '.join(ai_results) })
