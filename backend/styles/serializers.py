from rest_framework.serializers import ModelSerializer
from .models import style

class styleSerializer(ModelSerializer):
    class Meta:
        model = style
        fields = '__all__'