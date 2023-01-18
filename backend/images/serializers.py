from rest_framework.serializers import ModelSerializer
from .models import image

class imageSerializer(ModelSerializer):
    class Meta:
        model = image
        fields = '__all__'
