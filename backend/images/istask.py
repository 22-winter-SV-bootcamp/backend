import redis

def task_exist(task_id):
    r = redis.Redis(host='redis',port=6379,decode_responses=True)
    is_task = False
    
    for i in r.keys():                             # 있는 task인지 확인
        if i.startswith('celery'):
            a = r.get(i).split('"task_id": "')         # r.get(i) 타입은 스트링
            if task_id == a[1][:-2]:
                is_task = True
    return is_task