
from django.urls import path
from perfiles.views import registro,login_view

urlpatterns = [
path('registro/', registro, name="registro"),
path('login/', login_view, name="login"),
]   