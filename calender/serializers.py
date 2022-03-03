from .models import Calender
from rest_framework.serializers import ModelSerializer

class RelapseSerializer(ModelSerializer):
    class Meta:
        model = Calender
        fields = '__all__'