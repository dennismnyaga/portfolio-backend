from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from .models import *
from rest_framework.response import Response

# Create your views here.


class PorfolioViews(APIView):
    def get(self, request):
        dat = Porfolio.objects.all().order_by('-date_added')
        serialize = PotfolioSerializer(dat, many = True)
        
        return Response(serialize.data)


class PorfolioDetailsViews(APIView):
    def get(self, request, pk):
        dat = Porfolio.objects.filter(pk=pk)

        serialize = PotfolioSerializer(dat, many=True)
        
        return Response(serialize.data)
