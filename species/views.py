from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Species
from .serializers import SpeciesSerializer

from django.db import IntegrityError

class SpeciesListView(APIView):
    def get(self, _request):
      species = Species.objects.all()
      serialized_species = SpeciesSerializer(species, many=True)
      return Response(serialized_species.data, status=status.HTTP_200_OK)
    
    def post(self, request):
      species_to_add = SpeciesSerializer(data=request.data)
      try:
          species_to_add.is_valid()
          species_to_add.save()
          return Response(species_to_add.data, status=status.HTTP_201_CREATED)
      except IntegrityError as e:
          res = {                "detail": str(e)            }
          return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

      except AssertionError as e:
            return Response({ "detail": str(e) }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

      except:
            return Response({ "detail": "Unprocessable Entity" }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
      
class SpeciesDetailView(APIView):
    def get_species(self, id):
        try:
            return Species.objects.get(id=id)
        except Species.DoesNotExist:
            raise NotFound(detail="Sorry! Can't find that species.")
    

    def get(self, _request, id):
        species = self.get_species(id=id) 
        serialized_species = SpeciesSerializer(species)
        return Response(serialized_species.data, status=status.HTTP_200_OK)
    
    def put(self, request, id):
        species_to_edit = self.get_species(id=id)
        updated_species = SpeciesSerializer(species_to_edit, data=request.data)
        try:
            updated_species.is_valid()
            updated_species.save()
            return Response(updated_species.data, status=status.HTTP_202_ACCEPTED)
        except AssertionError as e:
            return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        except:
            res = {
                "detail": "Unprocessable Entity"
            }
            return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def delete(self, _request, id):
        species_to_delete = self.get_species(id=id)
        species_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    