from django.utils import timezone
from tkinter import CASCADE
from django.db import models

# Create your models here.
class basemodel(models.Model):  # 수정시간, 생성시간 모델
    created_at = models.DateTimeField(default=timezone.now)  # 해당 레코드 생성시 현재 시간 자동저장
    updated_at = models.DateTimeField(auto_now=True)  # 해당 레코드 갱신시 현재 시간 자동저장

    class Meta:
        abstract = True  # 상속

class images(basemodel):
    id = models.AutoField(primary_key=True)  # pk
    uuid = models.CharField(null=False, max_length=36, default='')
    link = models.CharField(max_length=200)
    
    def __str__(self):
        result_id = str(self.id)
        return result_id

class style(basemodel):
    id = models.AutoField(primary_key=True)  # pk
    image_id = models.ForeignKey(ResultImage, on_delete=models.CASCADE) # fk
    gender = models.CharField(max_length=36)
    top = models.CharField(max_length=36)
    top_color = models.CharField(max_length=36)
    bottom = models.CharField(max_length=36)
    bottom_color = models.CharField(max_length=36)