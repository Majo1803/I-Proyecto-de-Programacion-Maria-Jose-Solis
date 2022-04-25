from hashlib import md5
from getpass import getpass


def cifrar (entrada):
    entrada_binaria=entrada.encode('ascii')
    resultado = md5(entrada_binaria)
    return (resultado.hexdigest())

def obtener_calve(mensaje):
    pswd = getpass(mensaje+": ")
    return (pswd)