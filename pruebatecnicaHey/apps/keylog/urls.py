from django.urls import path
from .views import keylog

urlpatterns = [
    path('keylog/',keylog),
]