from common import MySpeciesSerializer
from species.serializers import SpeciesSerializer


class PopulatedMySpeciesSerializer(MySpeciesSerializer):
  species = SpeciesSerializer(many=True)