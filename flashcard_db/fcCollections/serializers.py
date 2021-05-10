from rest_framework import serializers
from .models import FcCollection


class FcCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FcCollection
        fields = ['fcCollection_id', 'fcCollection_title', 'fcCollectionType_id', 'fcCollection_image']

