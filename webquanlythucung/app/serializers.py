from rest_framework import serializers
from .models import ThuCung
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ThuCungSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThuCung
        fields = '__all__'
