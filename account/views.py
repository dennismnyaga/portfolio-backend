from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework import status

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


class email_sender(APIView):
    def post(self, request):
        # Get data from request
        print('data ', request.data)
        serializer = EmailMessageSerializer(data=request.data)

        # Validate and save if valid
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Email saved successfully!"}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)