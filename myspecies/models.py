from django.db import models
from species.models import Species


class MySpecies(models.Model):
    species = models.ForeignKey(
        Species, on_delete=models.CASCADE, related_name='my_species_entries')
    added_at = models.DateTimeField(auto_now_add=True)
    removed_at = models.DateTimeField(null=True, blank=True)

    def is_active(self):
        return self.removed_at is None

    def __str__(self):
        return f"MySpecies: {self.species.scientific_name} (removed: {self.removed_at})"
