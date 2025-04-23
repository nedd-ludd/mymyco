from rest_framework import serializers
from .models import Species

class SpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species  # the model it should use
        fields = '__all__'  # which fields to serialize
