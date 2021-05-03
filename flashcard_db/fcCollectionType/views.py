from django.shortcuts import render
from .models import FcCollectionType
from .serializers import FcCollectionTypeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class FcCollectionTypeList(APIView):

    def get(self, request):
        fcCollectionType = FcCollectionType.objects.all()
        serializer = FcCollectionTypeSerializer(fcCollectionType, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FcCollectionType(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
