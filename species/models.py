from django.db import models
import datetime


from django.db import models


class Species(models.Model):
    id = models.AutoField(primary_key=True)  # or use UUID if needed
    scientific_name = models.CharField(max_length=200)
    common_names = models.JSONField(default=list, blank=True, null=True)
    taxonomy_family = models.CharField(max_length=100, blank=True, null=True)
    taxonomy_order = models.CharField(max_length=100, blank=True, null=True)
    taxonomy_genus = models.CharField(max_length=100, blank=True, null=True)
    is_cubes = models.BooleanField(default=False)
    edibility = models.CharField(max_length=100, blank=True, null=True)
    medicinal_properties = models.TextField(blank=True, null=True)
    substrate_preferences = models.TextField(blank=True, null=True)
    optimal_temperature = models.FloatField(blank=True, null=True)
    optimal_humidity = models.FloatField(blank=True, null=True)
    light_requirements = models.CharField(
        max_length=100, blank=True, null=True)
    co2_tolerance = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    photo_url = models.URLField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_custom = models.BooleanField(default=False)
