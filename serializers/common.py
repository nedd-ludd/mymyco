from rest_framework import serializers
from species.models import  Species
from myspecies.models import MySpecies


class SpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = '__all__'


class MySpeciesSerializer(serializers.ModelSerializer):
    species = SpeciesSerializer()  # ✅ Nested serializer!

    class Meta:
        model = MySpecies
        fields = ['id', 'added_at', 'removed_at', 'species']
