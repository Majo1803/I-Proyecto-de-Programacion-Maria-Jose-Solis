
from utils.utils import cifrar

import menu.menu as menu

l_admin={
        "majo": {
            "nombre": "Maria José Solis",
            "numero": "83817491",
            "password": cifrar("123")
    },
        "asolisgo": {
            "nombre": "Allan Solis Gonzalez",
            "numero": "86453803",
            "password":cifrar("1095")
    }
 } 
l_estudiante={
        "majo": {
            "nombre": "Maria Solis",
            "password": cifrar("109"),
    }
 } 
l_cursos= (
    {"nombre":"Matemática General","creditos":"3","fech.inicio":"9/2/2022","fech.finalización":"16/6/2022", "horario":"Martes de 1 p.m a 3 p.m","carreras":"Ing.Computación, Agronomía"},
    {"nombre":"Inglés Básico","creditos":"","fech.inicio":"9/2/2022","fech.finalización":"16/6/2022", "horario":"Viernes de 9 a.m a 11:30 a.m","carreras":"Ing.Computación, Agronomía, Administración"},  
    {"nombre":"Natacion","creditos":"0","fech.inicio":"9/2/2022","fech.finalización":"16/6/2022", "horario":"Lunes de 1 p.m a 3 p.m","carreras":"Ing.Computación,Agronomía,Ing.Electrónica,Administración"},
    
 ) 
l_cursos_nuevo={}
carrera_valida_list=[] 
dict_actividades={}

l_actividades={


    
} 
l_carreras=("Administración de empresas","Agronomía","Ing.Computación","Ing.Electrónica") 


menu.menu_principal(l_admin,l_estudiante,l_cursos,l_carreras,dict_actividades)
