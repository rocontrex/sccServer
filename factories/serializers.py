from rest_framework import serializers
from .models import Factories

class FactorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Factories
        fields = '__all__'