from rest_framework import serializers
from tile.models import Country
from .models import (
    Laminate, Grade, Thickness, Chamfer, WaterResistance,
    LaminatePattern, Tone, WoodType, Gloss, Width, Texture,
    Construction, ConnectionType, Underlay, SkirtingBoard
)

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name']

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ['id', 'name']

class ThicknessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thickness
        fields = ['id', 'name']

class ChamferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chamfer
        fields = ['id', 'name']

class WaterResistanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaterResistance
        fields = ['id', 'name']

class LaminatePatternSerializer(serializers.ModelSerializer):
    class Meta:
        model = LaminatePattern
        fields = ['id', 'name']

class ToneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tone
        fields = ['id', 'name']

class WoodTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WoodType
        fields = ['id', 'name']

class GlossSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gloss
        fields = ['id', 'name']

class WidthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Width
        fields = ['id', 'name']

class TextureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Texture
        fields = ['id', 'name']

# class SubstrateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Substrate
#         fields = ['id', 'name']

class ConstructionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Construction
        fields = ['id', 'name']

class ConnectionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConnectionType
        fields = ['id', 'name']


class LaminateSerializer(serializers.ModelSerializer):

    country = CountrySerializer()
    grade = GradeSerializer()
    thickness = ThicknessSerializer()
    chamfer = ChamferSerializer()
    water_resistance = WaterResistanceSerializer()
    laminate_pattern = LaminatePatternSerializer()
    tone = ToneSerializer()
    wood_type = WoodTypeSerializer()
    gloss = GlossSerializer()
    width = WidthSerializer()
    texture = TextureSerializer()
    #substrate = SubstrateSerializer()
    construction = ConstructionSerializer()
    connection_type = ConnectionTypeSerializer()

    class Meta:
        model = Laminate
        fields = '__all__'



class UnderlaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Underlay
        fields = '__all__'


class SkirtingBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkirtingBoard
        fields = '__all__'