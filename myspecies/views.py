from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from serializers.populated import PopulatedMySpeciesSerializer
from .models import MySpecies

from .serializers import MySpeciesSerializer

from django.db import IntegrityError

class MySpeciesListView(APIView):
  def get(self, _request):
    myspecies = MySpecies.objects.all()
    serialized_myspecies = PopulatedMySpeciesSerializer(myspecies, many=True)
    return Response(serialized_myspecies.data, status=status.HTTP_200_OK)
  

  def post(self, request):
      myspecies_to_add = MySpeciesSerializer(data=request.data)
      try:
          myspecies_to_add.is_valid()
          myspecies_to_add.save()
          return Response(myspecies_to_add.data, status=status.HTTP_201_CREATED)

      except IntegrityError as e:
          print("IntegrityError:", str(e))  # add this line
          res = {"detail": str(e)}
          return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
      except AssertionError as e:
          return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
      except Exception as e:
          print("here")
          return Response({"detail": f"Unexpected error: {str(e)}"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
          
    # def delete(self, request):
    #   pass