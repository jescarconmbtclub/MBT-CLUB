# views.py
from rest_framework import generics
from .models import Vajilla, Medallas, Llaveros, Banderines, ObjetoMagico, Arrojadizos, Medallon
from .serializers import VajillaSerializer, MedallasSerializer, LlaverosSerializer, BanderinesSerializer, ObjetoMagicoSerializer, ArrojadizosSerializer, MedallonSerializer

class VajillaListCreateView(generics.ListCreateAPIView):
    queryset = Vajilla.objects.all()
    serializer_class = VajillaSerializer

class MedallasListCreateView(generics.ListCreateAPIView):
    queryset = Medallas.objects.all()
    serializer_class = MedallasSerializer

class LlaverosListCreateView(generics.ListCreateAPIView):
    queryset = Llaveros.objects.all()
    serializer_class = LlaverosSerializer

class BanderinesListCreateView(generics.ListCreateAPIView):
    queryset = Banderines.objects.all()
    serializer_class = BanderinesSerializer

class ObjetoMagicoListCreateView(generics.ListCreateAPIView):
    queryset = ObjetoMagico.objects.all()
    serializer_class = ObjetoMagicoSerializer

class ArrojadizosListCreateView(generics.ListCreateAPIView):
    queryset = Arrojadizos.objects.all()
    serializer_class = ArrojadizosSerializer

class MedallonListCreateView(generics.ListCreateAPIView):
    queryset = Medallon.objects.all()
    serializer_class = MedallonSerializer
