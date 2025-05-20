from rest_framework import serializers
from .models import Tile, Laminate, Category, Purpose, Feature

class CategorySerializer(serializers.ModelSerializer):
    class Meta: model = Category
    fields = 'all'

class PurposeSerializer(serializers.ModelSerializer):
    class Meta: model = Purpose 
    fields = 'all'

class FeatureSerializer(serializers.ModelSerializer):
    class Meta: model = Feature 
    fields = 'all'

class TileSerializer(serializers.ModelSerializer):
    purpose = serializers.PrimaryKeyRelatedField(many=True, queryset=Purpose.objects.all())
    features = serializers.PrimaryKeyRelatedField(many=True, queryset=Feature.objects.all())

class Meta:
    model = Tile
    fields = [
        'id', 'name', 'description', 'price', 'discount', 'image', 'category', 'material',
        'room', 'purpose', 'size', 'color', 'pattern', 'surface', 'shape',
        'is_new', 'is_promo', 'style', 'features', 'country', 'collection'
    ]

class LaminateSerializer(serializers.ModelSerializer):
    class Meta: model = Laminate
    fields = [ 'id', 'name', 'description', 'price', 'discount', 'image', 'category', 'country', 'grade', 'thickness', 'water_resistant', 'chamfer', 'pattern', 'surface', 'wood_type', 'is_promo' ]