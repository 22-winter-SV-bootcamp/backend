import boto3
from backend.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME
from uuid import uuid4
import redis

def get_image_url(image):
    s3_client = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY
    )
    image_type = "jpg"
    image_uuid = str(uuid4())
    s3_client.put_object(Body=image, Bucket=AWS_STORAGE_BUCKET_NAME, Key=image_uuid + "." + image_type)
    image_url = "http://"+AWS_STORAGE_BUCKET_NAME+".s3.ap-northeast-2.amazonaws.com/" + \
                image_uuid + "." + image_type
    image_url = image_url.replace(" ", "/")
    return image_url


def get_dict(task):
    to_list = list(task.result.values())                    # dict -> list 
    to_str = ' '.join(to_list)                              # list -> string
    lists = to_str.split()                                  # string -> list
    dict = {string:i for i, string in enumerate(lists)}     # confidence별로 dict의 value값 지정 (낮을수록 높은 confidence)    
    return dict


def is_task_exist(task_id):
    r = redis.Redis(host='redis',port=6379,decode_responses=True)

    for i in r.keys():                             # 있는 task인지 확인
        if i.startswith('celery'):
            a = r.get(i).split('"task_id": "')         # r.get(i) 타입은 스트링
            if task_id == a[1][:-2]:
                return True
    return False


def get_task_result(status,result=None):
    if result is not None:
        task_result = {
            'status' : status,
            'result' : result
        }
        return task_result
    else: 
        task_result = {
            'status' : status
        }
        return task_result

def classify(dict, top, bot):
    bot_list = []
    top_list = []
    for key in dict:
        if key in bot:
            bot_list.append(key)
        elif key in top:
            top_list.append(key)

    large_top = 't-shirts'     
    large_bot = 'slacks'

    if top_list:
        large_top = top_list[0]
    if bot_list:
        large_bot = bot_list[0]

    return large_top, large_bot


def get_sort_list(kind):
    with open('images/sort/'+kind+'.txt') as g:
        result = g.read().splitlines()
    return result