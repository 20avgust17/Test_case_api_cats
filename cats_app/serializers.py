from rest_framework import serializers
from cats_app.models import CatsModels


class CatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatsModels
        fields = '__all__'
