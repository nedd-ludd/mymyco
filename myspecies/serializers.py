from rest_framework import serializers
from .models import MySpecies
from species.models import Species

class MySpeciesSerializer(serializers.ModelSerializer):
  species = serializers.PrimaryKeyRelatedField(queryset=Species.objects.all())

  class Meta:
    model = MySpecies
    fields = '__all__'