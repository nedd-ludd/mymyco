from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from serializers.populated import PopulatedMySpeciesSerializer
from .models import MySpecies

class MySpeciesListView(APIView):
  def get(self, _request):
    myspecies = MySpecies.objects.all()
    serialized_myspecies = PopulatedMySpeciesSerializer(myspecies, many=True)
    return Response(serialized_myspecies.data, status=status.HTTP_200_OK)