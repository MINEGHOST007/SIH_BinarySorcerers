from rest_framework import serializers
from .models import Dormamu

class DormamuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dormamu
        fields = '__all__'