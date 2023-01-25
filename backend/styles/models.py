from django.db import models
from images.models import basemodel, image


class style(basemodel):
    id = models.AutoField(primary_key=True)  # pk
    image_id = models.ForeignKey(image, on_delete=models.CASCADE, db_column='image_id',default=1) # fk
    gender = models.CharField(max_length=36)
    top = models.CharField(max_length=36)
    top_color = models.CharField(max_length=36)
    bottom = models.CharField(max_length=36)
    bottom_color = models.CharField(max_length=36)

    class Meta:
        db_table = 'style'
