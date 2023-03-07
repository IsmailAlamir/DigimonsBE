from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import DigimonsSerializer
from .models import Digimon
import requests


class allDigimons(APIView):
    serializer_class = DigimonsSerializer

    def get(self,request):
        url='https://digimon-api.vercel.app/api/digimon'
        req = requests.get(url).json()
        return Response(req)


class digimonsListView(ListCreateAPIView):
    queryset=Digimon.objects.all()
    serializer_class= DigimonsSerializer

class digimonsDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Digimon.objects.all()
    serializer_class= DigimonsSerializer

