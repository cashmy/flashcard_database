from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import FlashCard
from .serializers import FlashCardSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class FlashCardList(APIView):
    def get(self, request):
        flashCard = FlashCard.objects.all()
        serializer = FlashCardSerializer(flashCard, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FlashCardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class FlashCardCollection(APIView):
    def get(self, request, collection_id):
        flashCard = FlashCard.objects.all().filter(fcCollection_id=collection_id)
        serializer = FlashCardSerializer(flashCard, many=True)
        return Response(serializer.data)


class FlashCardDetail(APIView):
    def get_by_pk(self, pk):
        try:
            return FlashCard.objects.get(pk=pk)
        except:
            raise Http404

    def put(self, request, pk):
        flashCard = self.get_by_pk(pk)
        serializer = FlashCardSerializer(flashCard, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        flashCard = self.get_by_pk(pk)
        flashCard.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

