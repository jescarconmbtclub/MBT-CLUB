# views.py
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView


#------------------------Vajilla------------------------#
class VajillaListCreateView(generics.ListCreateAPIView): #Create
    queryset = Vajilla.objects.all()
    serializer_class = VajillaSerializer

#------------------------Medallas------------------------#
class MedallasListCreateView(generics.ListCreateAPIView): #Create
    queryset = Medallas.objects.all()
    serializer_class = MedallasSerializer


#------------------------Llaveros------------------------#
class LlaverosListCreateView(generics.ListCreateAPIView): #Create
    queryset = Llaveros.objects.all()
    serializer_class = LlaverosSerializer



#------------------------Banderines------------------------#
class BanderinesListCreateView(generics.ListCreateAPIView): #Create
    queryset = Banderines.objects.all()
    serializer_class = BanderinesSerializer


#------------------------ObjetoMagico------------------------#
class ObjetoMagicoListCreateView(generics.ListCreateAPIView): #Create
    queryset = ObjetoMagico.objects.all()
    serializer_class = ObjetoMagicoSerializer


#------------------------Arrojadizos------------------------#
class ArrojadizosListCreateView(generics.ListCreateAPIView): #Create
    queryset = Arrojadizos.objects.all()
    serializer_class = ArrojadizosSerializer


#------------------------Medallon------------------------#
class MedallonListCreateView(generics.ListCreateAPIView): #Create
    queryset = Medallon.objects.all()
    serializer_class = MedallonSerializer


#------------------------GetProductByMaterial------------------------#
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


#------------------------GetByCode------------------------#
class CodeGroupedView(APIView):
    def get(self, request):
        codigo = request.query_params.get('codigo', None)
        if not codigo:
            return Response({'error': 'Debes proporcionar un código.'}, status=400)

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
            filtered_objects = model.objects.filter(codigo=codigo)
            serializer = serializer(filtered_objects, many=True)
            res.append(serializer.data)
            
        return Response(res)    