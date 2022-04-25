from hashlib import md5
from getpass import getpass

lista=[1,2,3,4,5,6,7,8,9]

def cifrar (entrada):
    entrada_binaria=entrada.encode('ascii')
    resultado = md5(entrada_binaria)
    return (resultado.hexdigest())

def obtener_calve(mensaje):
    pswd = getpass(mensaje+": ")
    return (pswd)