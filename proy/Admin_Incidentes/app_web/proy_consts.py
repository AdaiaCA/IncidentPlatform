"""
    Elaboró: Jesus Antonio Barradas Maldonado
    Fecha: 02 de Febrero del 2025    Usuario: JABM
    Descripción: Archivo que contiene las constantes que se utilizaran en todo el proyecto. 
    ¡¡¡IMPORTANTE!!! ESTE ARCHIVO NO SE SUBE A GIT
"""
class APP_CACHE:
    IS_LOGGING = 'i'
    TOKEN = 'k'
class APP_URLS:
    LOGIN = '/login/'
    LOGIN_NO_LOGGING = '/login?no_logging'
    LOGIN_VENCIDO = '/login?expired_token'