import django_filters
from django_filters import rest_framework as filters
from .models import (
    Laminate, Grade, Thickness, Chamfer, WaterResistance,
    LaminatePattern, Tone, WoodType, Gloss, Width, Texture,
    Construction, ConnectionType, Underlay, SkirtingBoard
)
from tile.models import Country

class NumberInFilter(django_filters.BaseInFilter, django_filters.NumberFilter):
    pass

class LaminateFilter(django_filters.FilterSet):
    price_min = django_filters.NumberFilter(field_name="price", lookup_expr="gte")
    price_max = django_filters.NumberFilter(field_name="price", lookup_expr="lte")
    country = NumberInFilter(field_name='country__id', lookup_expr='in')
    grades = NumberInFilter(field_name='grade__id', lookup_expr='in')
    thickness = NumberInFilter(field_name='thickness__id', lookup_expr='in')
    chamfers = NumberInFilter(field_name='chamfer__id', lookup_expr='in')
    water_resistances = NumberInFilter(field_name='water_resistance__id', lookup_expr='in')
    laminate_patterns = NumberInFilter(field_name='laminate_pattern__id', lookup_expr='in')
    patterns = NumberInFilter(field_name='pattern__id', lookup_expr='in')
    tones = NumberInFilter(field_name='tone__id', lookup_expr='in')
    wood_types = NumberInFilter(field_name='wood_type__id', lookup_expr='in')
    gloss = NumberInFilter(field_name='gloss__id', lookup_expr='in')
    width = NumberInFilter(field_name='width__id', lookup_expr='in')
    textures = NumberInFilter(field_name='texture__id', lookup_expr='in')
    constructions = NumberInFilter(field_name='construction__id', lookup_expr='in')
    connection_type = NumberInFilter(field_name='connection_type__id', lookup_expr='in')

    is_sale = django_filters.BooleanFilter()
    name = django_filters.CharFilter(lookup_expr="icontains")
    description = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Laminate
        fields = []


class UnderlayFilter(django_filters.FilterSet):
    thickness = django_filters.NumberFilter()
    has_vapor_barrier = django_filters.BooleanFilter()
    floor_type = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Underlay
        fields = ['thickness', 'has_vapor_barrier', 'floor_type']

class CharInFilter(filters.BaseInFilter, filters.CharFilter):
    pass

class SkirtingBoardFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    type = CharInFilter(field_name='type', lookup_expr='in')
    moisture_resistance = django_filters.CharFilter(lookup_expr='iexact')
    tone = django_filters.CharFilter(lookup_expr='iexact')
    price_min = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    thickness_min = django_filters.NumberFilter(field_name='thickness', lookup_expr='gte')
    thickness_max = django_filters.NumberFilter(field_name='thickness', lookup_expr='lte')
    height_min = django_filters.NumberFilter(field_name='height', lookup_expr='gte')
    height_max = django_filters.NumberFilter(field_name='height', lookup_expr='lte')

    class Meta:
        model = SkirtingBoard
        fields = [
            'name', 'type', 'moisture_resistance', 'tone',
            'price_min', 'price_max',
            'thickness_min', 'thickness_max',
            'height_min', 'height_max',
        ]