from rest_framework import serializers # type: ignore
from ..models import  Category
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'