from django.urls import path
from .views import domingos

urlpatterns = [
    path('domingos/',domingos),
]