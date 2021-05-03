from django.shortcuts import render
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
