"""
URL configuration for sistema_odonto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from sistema_odonto.views import saludar_con_html
from control_odonto.views import crear_paciente

urlpatterns = [
    path("admin/", admin.site.urls),
    # Aqui agregar mis URLS
    # path(RUTA, VIEW)
    # La RUTA de la URL puede ser diferente al nombre de la view
    path("", saludar_con_html, name="inicio"),
   
]