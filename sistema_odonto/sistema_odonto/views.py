from django.shortcuts import render


def saludar_con_html(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='inicio.html',
        context=contexto,
    )
    return http_response
def inicio(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='base.html',
        context=contexto,
    )
    return http_response