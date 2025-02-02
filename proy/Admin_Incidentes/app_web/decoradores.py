"""
    Elaboró: Jesus Antonio Barradas Maldonado
    Fecha: 02 de Febrero del 2025    Usuario: JABM
    Descripción: Archivo que permite agregar shorcuts a las urls redirigiendo de acuerdo al caso que se le asigne
"""
from django.shortcuts import redirect
import datetime
from django.utils.decorators import method_decorator
from proy_consts.py import APP_CACHE, APP_URLS

def is_logging(vista):
    def func_int(request):
        #Se guarda si esta logueado el usuario
        if not request.session.get(APP_CACHE.IS_LOGGING, False):
            return redirect(APP_URLS.LOGIN_NO_LOGGING)
        #si esta logueado, se valida que el token sea valido
        if validar_token(request):
            return redirect(APP_URLS.LOGIN_VENCIDO)
    return vista
