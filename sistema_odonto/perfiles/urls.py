
from django.urls import path
from perfiles.views import registro

urlpatterns = [
path('registro/', registro, name="registro"),
]   