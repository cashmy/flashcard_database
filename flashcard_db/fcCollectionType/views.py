from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
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
        serializer = FcCollectionTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class FcCollectionTypeDetail(APIView):

    def get_by_pk(self, pk):
        try:
            return FcCollectionType.objects.get(pk=pk)
        except:
            raise Http404

    def put(self, request, pk):
        fcCollectionType = self.get_by_pk(pk)
        serializer = FcCollectionTypeSerializer(fcCollectionType, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        fcCollection = self.get_by_pk(pk)
        fcCollection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
