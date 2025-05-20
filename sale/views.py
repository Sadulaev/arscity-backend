from django.shortcuts import render

from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, filters as df_filters
from .models import Tile, Laminate, Category
from .serializers import TileSerializer, LaminateSerializer, CategorySerializer

class TileFilter(FilterSet):
    purpose = df_filters.ModelMultipleChoiceFilter(
        field_name='purpose', queryset=Tile.purpose.rel.model.objects.all(), conjoined=False
    )
    features = df_filters.ModelMultipleChoiceFilter(
        field_name='features', queryset=Tile.features.rel.model.objects.all(), conjoined=False
    )

    class Meta:
        model = Tile
        fields = {
            'category': ['exact'],
            'material': ['exact'],
            'room': ['exact'],
            'size': ['exact'],
            'color': ['exact'],
            'pattern': ['exact'],
            'surface': ['exact'],
            'shape': ['exact'],
            'is_new': ['exact'],
            'is_promo': ['exact'],
            'style': ['exact'],
            'country': ['exact'],
            'collection': ['exact'],
        }

class LaminateFilter(FilterSet):
    class Meta:
        model = Laminate
        fields = {
            'category': ['exact'],
            'country': ['exact'],
            'grade': ['exact'],
            'thickness': ['exact'],
            'water_resistant': ['exact'],
            'chamfer': ['exact'],
            'pattern': ['exact'],
            'surface': ['exact'],
            'wood_type': ['exact'],
            'is_promo': ['exact'],
        }

class TileViewSet(viewsets.ModelViewSet):
    queryset = Tile.objects.all()
    serializer_class = TileSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = TileFilter
    search_fields = ['name', 'description']

class LaminateViewSet(viewsets.ModelViewSet):
    queryset = Laminate.objects.all()
    serializer_class = LaminateSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = LaminateFilter
    search_fields = ['name', 'description']

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer