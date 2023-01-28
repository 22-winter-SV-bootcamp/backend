import boto3
from backend.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME
from uuid import uuid4


def get_image_url(image):
    s3_client = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY
    )
    image_type = "jpg"
    image_uuid = str(uuid4())
    # s3_client.put_object(Body=image, Bucket=AWS_STORAGE_BUCKET_NAME, Key=image_uuid + "." + image_type)
    image_url = "http://"+AWS_STORAGE_BUCKET_NAME+".s3.ap-northeast-2.amazonaws.com/" + \
                image_uuid + "." + image_type
    image_url = image_url.replace(" ", "/")
    return image_url