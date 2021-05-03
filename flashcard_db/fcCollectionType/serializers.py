from rest_framework import serializers
from .models import FcCollectionType


class FcCollectionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FcCollectionType
        fields = ['fcCollectionType_id', 'fcCollectionType_name', 'fcCollectionType_desc']
