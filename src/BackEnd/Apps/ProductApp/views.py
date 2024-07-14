# views.py
from rest_framework import generics
from .models import Vajilla, Medallas, Llaveros, Banderines, ObjetoMagico, Arrojadizos, Medallon
from .serializers import VajillaSerializer, MedallasSerializer, LlaverosSerializer, BanderinesSerializer, ObjetoMagicoSerializer, ArrojadizosSerializer, MedallonSerializer

from django.core.exceptions import FieldError
from itertools import groupby
from operator import attrgetter
from rest_framework.response import Response
from rest_framework.views import APIView

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


class MaterialGroupedView(APIView):
    def get(self, request):
        material = request.query_params.get('material', None)
        if not material:
            return Response({'error': 'Debes proporcionar un parámetro "material".'}, status=400)

        models_and_serializers = [
            (Vajilla, VajillaSerializer),
            (Medallas, MedallasSerializer),
            (Llaveros, LlaverosSerializer),
            (Banderines, BanderinesSerializer),
            (ObjetoMagico, ObjetoMagicoSerializer),
            (Arrojadizos, ArrojadizosSerializer),
            (Medallon, MedallonSerializer),
        ]
        res=[]

        for model,serializer in models_and_serializers:
            filtered_objects = model.objects.filter(material=material)
            serializer = serializer(filtered_objects, many=True)
            res.append(serializer.data)
            
        return Response(res)    