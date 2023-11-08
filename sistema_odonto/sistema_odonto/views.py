from django.shortcuts import render
from django.http import HttpResponse

def saludar_con_html(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='base.html',
        context=contexto,
    )
    return http_response
