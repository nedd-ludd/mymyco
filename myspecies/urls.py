from django.urls import path
from .views import MySpeciesListView

urlpatterns = [
    path('', MySpeciesListView.as_view())
]
