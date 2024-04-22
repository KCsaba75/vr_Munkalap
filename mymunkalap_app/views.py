# views.py


from rest_framework.response import Response
from rest_framework.views import APIView


from .serializers import MunkalapSerializer
from rest_framework import generics
from .models import Megrendelo, Hibatipusok, Munkalap
from .serializers import MegrendeloSerializer, HibatipusokSerializer, MunkalapSerializer, MunkalapListSerializer

class MegrendeloListCreate(generics.ListCreateAPIView):
    queryset = Megrendelo.objects.all()
    serializer_class = MegrendeloSerializer

class MegrendeloRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Megrendelo.objects.all()
    serializer_class = MegrendeloSerializer



class HibatipusokListCreate(generics.ListCreateAPIView):
    queryset = Hibatipusok.objects.all()
    serializer_class = HibatipusokSerializer

class HibatipusokRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hibatipusok.objects.all()
    serializer_class = HibatipusokSerializer



class MunkalapListCreate(generics.ListCreateAPIView):
    queryset = Munkalap.objects.all()
    serializer_class = MunkalapSerializer
    
class MunkalapRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Munkalap.objects.all()
    serializer_class = MunkalapSerializer

class AktivMunkalapokJsonView(APIView):
    def get(self, request, *args, **kwargs):
        aktiv_munkalapok = Munkalap.objects.filter(munkalapstatus='enum_value_1')
        serializer = MunkalapListSerializer(aktiv_munkalapok, many=True)
        return Response(serializer.data)
    
class InAktivMunkalapokJsonView(APIView):
    def get(self, request, *args, **kwargs):
        inaktiv_munkalapok = Munkalap.objects.filter(munkalapstatus='enum_value_2')
        serializer = MunkalapListSerializer(inaktiv_munkalapok, many=True)
        return Response(serializer.data)



class OsszesMunkalapokJsonView(APIView):
    def get(self, request, *args, **kwargs):
        munkalapok = Munkalap.objects.all()
        serializer = MunkalapListSerializer(munkalapok, many=True)
        return Response(serializer.data)