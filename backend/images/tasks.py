from __future__ import absolute_import, unicode_literals
from backend.celery import app
import requests
from django.core.cache import cache

@app.task
def ai_task(request):
    r = requests.post('http://ai:8081/api/v1/images', json=request)
    ret = r.json()
    return {"ai_results":ret["ai_results"]}
