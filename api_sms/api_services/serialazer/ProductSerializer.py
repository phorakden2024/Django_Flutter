from rest_framework import serializers 
from ..models import Product 
from ..models import Category
from api_services.serialazer.CategorySerializer import CategorySerializer

class ProductSerializer(serializers.ModelSerializer):
    category_id = serializers.StringRelatedField()
    class Meta:
        model = Product
        fields = '__all__'
        
   