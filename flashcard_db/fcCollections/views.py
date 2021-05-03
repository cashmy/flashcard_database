from django.shortcuts import render
from .models import FcCollection
from .serializers import FcCollectionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class FcCollectionList(APIView):

    def get(self, request):
        fcCollection = FcCollection.objects.all()
        serializer = FcCollectionSerializer(fcCollection, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FcCollection(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)