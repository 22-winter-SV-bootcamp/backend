from __future__ import absolute_import, unicode_literals
from backend.celery import app
import requests
import redis
from django.core.cache import cache

@app.task
def ai_task(request):
    r = requests.post('http://ai:8081/api/v1/images', json=request)
    ret = r.json()
    return {"ai_results":ret["ai_results"]}

def task_exist(task_id):
    r = redis.Redis(host='redis',port=6379,decode_responses=True)
    is_task = False
    
    for i in r.keys():                             # 있는 task인지 확인
        if i.startswith('celery'):
            a = r.get(i).split('"task_id": "')         # r.get(i) 타입은 스트링
            if task_id == a[1][:-2]:
                is_task = True
    return is_task

def get_dict(task):
    to_list = list(task.result.values())                    # dict -> list 
    to_str = ' '.join(to_list)                              # list -> string
    lists = to_str.split()                                  # string -> list
    dict = {string:i for i, string in enumerate(lists)}     # confidence별로 dict의 value값 지정 (낮을수록 높은 confidence)    
    return dict

