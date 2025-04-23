from django.urls import path  # import path from django
from .views import SpeciesListView  # import class from .views
from .views import SpeciesDetailView

urlpatterns = [
    path('', SpeciesListView.as_view()),
    path('<str:id>/', SpeciesDetailView.as_view(), name='species-detail'),
]
