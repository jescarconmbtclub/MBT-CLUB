from rest_framework import serializers
from .models import Vajilla, Medallas, Llaveros, Banderines, ObjetoMagico, Arrojadizos, Medallon

class VajillaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vajilla
        fields = '__all__'

class MedallasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medallas
        fields = '__all__'

class LlaverosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Llaveros
        fields = '__all__'

class BanderinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banderines
        fields = '__all__'

class ObjetoMagicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjetoMagico
        fields = '__all__'

class ArrojadizosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arrojadizos
        fields = '__all__'

class MedallonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medallon
        fields = '__all__'
