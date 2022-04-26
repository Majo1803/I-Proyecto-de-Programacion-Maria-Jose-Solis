
from time import sleep
from utils.utils import obtener_calve ,cifrar
from datetime import datetime

#_______Funcion que limpia la terminal_________
def limpiar_terminal():
    print (chr(27) + "[2J")

#____________OPCION PARA SALIR DEL PROGRAMA________________
def salir_programa():

        print("""

        **********      **********        ***** ***     **   ****   *******      ************
        **********   ***************      ***** ***     **   ****  ******      *************  
           ***      ******************    *****  ****  ***   **** *****       ******
           ***      *******    *******    *****   **** ***   *********         **************
           ***      *******    *******    *****   ********   **** *****           ************
           ***      *******    *******    *****    *******   ****  *****     ******   *********
           ***      *******    *******    *****     ******   ****    *****   ******    ********
           ***      ********   *******    ******      *****  ****     *****   ****************
               
                    """
                )
        print("\n\t¡Te agradecemos tu preferencia, hasta luego!")

        sleep(8)

#********************Funciones del menú interactivo*******************************************************

#_________________________ADMINISTRADORES_________________________________________________________________

#----------FUNCIÓN PARA LA OPCION DE NUEVO REGISTRO DE ADMINISTRADOR---------------------------------------
def agregar_registro_administrador (l_admin): 
    usuario= input("Escriba su usuario: ")
    l_admin[usuario] = {} 
    l_admin[usuario]['nombre'] = input("Escriba su nombre: ")
    l_admin[usuario]['nombre']=l_admin[usuario]['nombre']
    l_admin[usuario]['numero'] = int(input("Escriba su numero telefónico: "))
    l_admin[usuario]['password'] = cifrar(obtener_calve("Dijite una contraseña(solo caracteres numéricos): "))

    print ("""Registro creado:
     """)
    print(l_admin[usuario]) 
    print ("""
    Lista de administradores ahora::
     """)
    print(l_admin)
    print ("""
    Desea continuar
    
    """)
    print("1)si")
    print("2)no")
    opt_continuar=int(input("\n\n\tDijite la opcion: "))
    match opt_continuar:
                case 1:
                     print(autenticar_admin(l_admin))
#-----------------------------------------------------------------------------------------------------------------
   

#------------------FUNCIÓN PARA LA OPCION DE MOSTRAR EL REGISTRO DE LOS ADMINISTRADORES---------------------------
def mostrar_administrador(l_admin):
    print (l_admin)
    print ("""Desea usted realizar otra acción: 
    1) si
    2) no """)   
    opt_seguir=int(input("\n\n\tDijite la opcion: "))
    match opt_seguir:
        case 1:
            inicio_administrador_cc (l_admin,l_cursos,l_cursos_nuevo,carrera_valida_list,l_carreras)
        case 2:
            salir_programa()     
            sleep(10)
#------------------------------------------------------------------------------------------------------------------

#---------------------FUNCION DE LA OPCION DE AUTENTICACION DEL ADMINISTRADOR--------------------------------------
def autenticar_admin(l_admin):

    usuario = input("Escriba su usuario: ")
    contraseña = cifrar(obtener_calve("Escriba su contraseña: "))
    if usuario in l_admin and contraseña == l_admin[usuario]['password']:
            print("usuario valido, bienvenido")
            print (l_admin[usuario])
    else:
            print("usuario o contraseña invalida")
            print("desea usted registrarse: ")
            print ("1)si")
            print ("2)no")
            opt_registrarse=int(input("\n\n\tDijite la opcion: "))
            match opt_registrarse:
                case 1:
                      print(agregar_registro_administrador(l_admin))
                case 2:
                    print("gracias por usar el sistema") 
#---------------------------------------------------------------------------------------------------------------------

#----------------------FUNCION PARA AGREGAR CARRERAS MÁS DE UNA CARRERA A UN CURSO NUEVO------------------------------
def agregar_carreras_cursos(l_cursos_nuevo,carrera_valida_list):
   global l_cursos
   l_cursos=list(l_cursos)
   carrera=("Administración de empresas","Agronomía","Ing.Computación","Ing.Electrónica")
   print (carrera)
   carrera_ad=input("""Ingrese el nombre de las carreras que permite este curso:
     1- Escribalas tal y como aparecen en la lista anterior(no incluya las comillas):

      """  )

   if carrera_ad in carrera :
      if carrera_ad in carrera_valida_list:
         print ("la carrera ya se encuentra en el registro")
         print("Desea registrar otra carrera")
         print("1)Si")
         print("2)No")
         opt_otra_carrera=int(input("Digite la opcion: "))
         match opt_otra_carrera:
            case 1:
                return agregar_carreras_cursos(l_cursos_nuevo,carrera_valida_list)
            case 2:
                carrera_valida_list.append(carrera_ad)
                l_cursos_nuevo["carrera"]=carrera_valida_list
                l_cursos.append(l_cursos_nuevo)
                print (l_cursos)
                sleep(3)  
      else:   
            print("carrera valida")
            carrera_valida_list.append(carrera_ad)
            print("Desea registrar otra carrera")
            print("1)Si")
            print("2)No")
            opt_otra_carrera=int(input("Digite la opcion: "))
            match opt_otra_carrera:
               case 1:
                print(agregar_carreras_cursos(l_cursos_nuevo,carrera_valida_list))
               case 2:
                    carrera_valida_list.append(carrera_ad)
                    l_cursos_nuevo["carrera"]=carrera_valida_list
                    l_cursos.append(l_cursos_nuevo)
                    print (l_cursos)
                    sleep(3)   
   else:
            print("carrera invalida")

l_cursos_nuevo={}
carrera_valida_list=[]
#------------------------------------------------------------------------------------------------------------------------------

#-------------------------FUNCIÓN PARA QUE EL ADMINISTRADOR REGISTRE CURSOS NUEVOS --------------------------------------------
def agregar_cursos_admin(l_cursos,l_cursos_nuevo,carrera_valida_list):
   l_cursos=list(l_cursos)
   carrera_valida_list=[]
   print ("Por favor brinde los siguientes datos para el registro del curso")
   l_cursos_nuevo["nombre"] = input("Escriba el nombre: ")
   l_cursos_nuevo["creditos"] = int(input("Escriba los creditos: "))
   l_cursos_nuevo["fech.inicio"] =input("Escriba la fecha de inicio: ")
   l_cursos_nuevo["fech.finalización"] = input("Escriba la fecha de finalización: ")
   l_cursos_nuevo["horario"] =input("Escriba el horario: ")
   carrera=("Administración de empresas","Agronomía","Ing. Computación","Ing. Electrónica")
   print (carrera)
   carrera_ad=input("""Ingrese el nombre de las carreras que permite este curso:
   1- Escribalas tal y como aparecen en la lista anterior(no incluya las comillas):

   """)
   if carrera_ad in carrera :
               print("carrera valida")
               carrera_valida_list.append(carrera_ad)
               l_cursos_nuevo["carrera"]=carrera_valida_list
               print("Desea registrar otra carrera")
               print("1)Si")
               print("2)No")
               opt_otra_carrera=int(input("Digite la opcion: "))
               match opt_otra_carrera:
                 case 1:
                  print(agregar_carreras_cursos(l_cursos_nuevo,carrera_valida_list))
                 case 2:   
                    carrera_valida_list.append(carrera_ad)
                    l_cursos_nuevo["carrera"]=carrera_valida_list
                    l_cursos.append(l_cursos_nuevo)
                    print (l_cursos)
                    sleep(3)  
   else:
            print("carrera invalida")
#------------------------------------------------------------------------------------------------------------------------------------

#----------------------------FUNCIÓN PARA QUE EL ADMINISTRADOR REGISTRE CARRERAS------------------------------------------------------
l_carreras=()
def agregar_carreras(l_carreras):
   l_carreras=list(l_carreras)
   carrera_nueva=input("""Ingrese el nombre de la nueva carrera:
      """  )
   sleep(2)   
   l_carreras.append(carrera_nueva)
   l_carreras=tuple(l_carreras)
   sleep(2)
   print ("""Carrera agregada
   Esta es la nueva lista de carreras:
   
   """)
   print(l_carreras)
   opt_oc=int(input("Desea agragar otra carrera"))
   match opt_oc:
       case 1:
           return(agregar_carreras(l_carreras))
       case 2:
           menu_principal (l_admin,l_estudiante,l_cursos,l_carreras,dict_actividades) 
   sleep(5)
#-------------------------------------------------------------------------------------------------------------------------------------

#---------------------------FUNCIÓN PARA QUE EL ADMINISTRADOR MODIFIQUE LOS CURSOS----------------------------------------------------

def modificar_carreras_admin(l_carreras):
   l_carreras=list(l_carreras)
   print(l_carreras)
   opt_mod_carrera=int(input("\n\n\tDijite el numero correspondiente a la carrera que desea cambiar: "))
   opt=int(opt_mod_carrera-1)
   print(opt)
   for opt_mod_carrera in l_carreras:
      print ("valido")
      nombre_nuevo=input("\n\n\tDijite el nombre: ")
      l_carreras[opt]=nombre_nuevo
      print (l_carreras)  
#----------------------------------------------------------------------------------------------------------------------------------------

#-----------------------------FUNCION PARA QUE EL ADMINISTRADOR MODIFIQUE UN CURSO-------------------------------------------------------
def modificar_cursos(l_cursos,carrera_valida_list):
  
   print(l_cursos)
   opt_mod_cursos=int(input("\n\n\tDijite el numero correspondiente al curso que desea cambiar: "))
   opt=int(opt_mod_cursos-1)
   for opt_mod_cursos in l_cursos:
      print ("valido")
   
      if opt_mod_cursos in l_cursos: 
            l_cursos[opt]["nombre"] = input("Escriba el nombre: ")
            l_cursos[opt]["creditos"] = int(input("Escriba los creditos: "))
            l_cursos[opt]["fech.inicio"] =input("Escriba la fecha de inicio: ")
            l_cursos[opt]["fech.finalización"] = input("Escriba la fecha de finalización: ")
            l_cursos[opt]["horario"] =input("Escriba el horario: ")
            carrera=("Administración de empresas","Agronomía","Ing. Computación","Ing. Electrónica")
            print (carrera)
            carrera_ad=input("""Ingrese el nombre de las carreras que permite este curso:
         1- Escribalas tal y como aparecen en la lista anterior(no incluya las comillas):

         """)
            if carrera_ad in carrera :
                     print("carrera valida")
                     carrera_valida_list.append(carrera_ad)
                     print("Desea registrar otra carrera")
                     print("1)Si")
                     print("2)No")
                     opt_otra_carrera=int(input("Digite la opcion: "))
                     match opt_otra_carrera:
                        case 1:
                           print(agregar_carreras_cursos_modificado(l_cursos,carrera_valida_list,opt))
                           
                        case 2:
                           l_cursos[opt]["carreras"]=carrera_valida_list
                           print (l_cursos)  
            else:
                  print("carrera invalida")
#---------------------------------------------------------------------------------------------------------------------

#----------------------FUNCIÓN PARA AGREGAR MÁS DE UNA CARRERA A UN CURSO MODIFICADO----------------------------------
def agregar_carreras_cursos_modificado(l_cursos,carrera_valida_list,opt):
   carrera=("Administración de empresas","Agronomía","Ing.Computación","Ing.Electrónica")
   print (carrera)
   carrera_ad=input("""Ingrese el nombre de las carreras que permite este curso:
     1- Escribalas tal y como aparecen en la lista anterior(no incluya las comillas):

      """  )

   if carrera_ad in carrera :
      if carrera_ad in carrera_valida_list:
         print ("la carrera ya se encuentra en el registro")
         print("Desea registrar otra carrera")
         print("1)Si")
         print("2)No")
         opt_otra_carrera=int(input("Digite la opcion: "))
         match opt_otra_carrera:
            case 1:
               print(agregar_carreras_cursos_modificado(l_cursos,carrera_valida_list,opt))
            case 2:
                l_cursos[opt]["carreras"]=carrera_valida_list
                print (l_cursos)  
      else:   
            print("carrera valida")
            carrera_valida_list.append(carrera_ad)
            print("Desea registrar otra carrera")
            print("1)Si")
            print("2)No")
            opt_otra_carrera=int(input("Digite la opcion: "))
            match opt_otra_carrera:
               case 1:
                print(agregar_carreras_cursos_modificado(l_cursos,carrera_valida_list,opt))
               case 2:
                l_cursos[opt]["carreras"]=carrera_valida_list
                print (l_cursos) 
   else:
            print("carrera invalida")                    
#-------------------------------------------------------------------------------------------------------------------------------
               
#*******************************************************************************************************************************
#---------------------------------FUNCIÓN PARA EL INICIO DE UN ADMINISTRADOR CON CUENTA-----------------------------------------
def inicio_administrador_cc (l_admin,l_cursos,l_cursos_nuevo,carrera_valida_list,l_carreras):#la "cc" significa "con cuenta"
       print("""
       Bienvenido de nuevo, qué acción desea reaalizar:

          """)
       print ("1) Agregar o modificar un registro de administrador  ")
       print ("2) Ver su registro ")
       print ("3) Agregar un curso ")
       print ("4) Modificar un curso")
       print ("5) Agregar una carrera")
       print ("6) Modificar una carrera")

       opt_administrador=int (input("\n\n\tQué desea: "))
       match opt_administrador:
              case 1:
                   agregar_registro_administrador(l_admin)
              case 2:
                   mostrar_administrador(l_admin) 
                   sleep (10)  
              case 3:
                    agregar_cursos_admin(l_cursos,l_cursos_nuevo,carrera_valida_list)
              case 4:
                    modificar_cursos(l_cursos,carrera_valida_list)
              case 5:
                    agregar_carreras(l_carreras)      
              case 6:
                   modificar_carreras_admin(l_carreras)      
#----------------------------------------------------------------------------------------------------------------------------------

#**********************************************************************************************************************************

#_________________________________________________ESTUDIANTES______________________________________________________________________

#***********************************************************************************************************************************

#---------------------------- FUNCION PARA EL INICIO DEL MENU DE ESTUDIANTE CON CUENTA-----------------------------------------------

def inicio_estudiante_cc (l_estudiante,l_cursos):#la "cc" significa "con cuenta"
       print("""
       Bienvenido de nuevo, qué acción desea reaalizar:

          """)
       print ("1) Agregar carreras a mi registro ")
       print ("2) Ver mi registro ")
       print ("3) Ver lista de cursos disponibles y registrar cursos")
       print ("4) Agregar lista de posibles actividades")
       print ("5) Agregar actividades a mi registro")
       print ("6) Generar reporte de actividades")
       opt_estudiante=int (input("\n\n\tQué desea: "))
       match opt_estudiante:
              case 1:
                   agregar_carreras_estudiante(l_carreras,l_estudiante)
              case 2:
                   mostrar_estudiante(l_estudiante) 
              case 3:    
                  agregar_cursos_estudiante(l_cursos,l_estudiante)  
              case 4:
                  print ("""La actividad a registrar es una actividad
   1) recreativa 😎
   2) académica 🤓
   """)
                  opt_tipo_de_actividad=int(input("Dijite el número de la opción correcta: "))
                  match opt_tipo_de_actividad:
                   case 1:
                    agregar_registro_posibles_actividades_recreativas (l_actividades_recreativas)
                   case 2:
                    agregar_registro_posibles_actividades_académica (l_actividades_academicas,l_cursos,l_estudiante)
              case 5:
                    agregar_actividades_registro(l_estudiante,l_actividades)
              case 6:
                   reporte(l_estudiante)  
#----------------------------------------------------------------------------------------------------------------------------------------
#****************************************************************************************************************************************

#----------------------------FUNCION PARA QUE EL ESTUDIANTE MATRICULE UN CURSO-----------------------------------------------------------
def agregar_cursos_estudiante(l_cursos,l_estudiante):
   l_cursos_estu={}
   continuar=True
   while continuar:
      print("""
      Estos son los cursos disponibles por el momento:
      
      """)
      print(l_cursos)
      print("")
      item1 = int(input('Seleccione la posición en la que se encuentra el curso que desea añadir a su registro según la lista anterior(ejemplo:el primer curso que aparece en la lista es la posición 0): '))
      item1=int(item1)
      opt_registrar_cursos=int(input("Desea agregar este curso a su registro? digite 1 para Si o 2 para no: "))
      match opt_registrar_cursos:
         case 1:
                curso_escogido=l_cursos[item1]
                l_cursos_estu[item1] = curso_escogido
                print("")
                continuar = input('¿Quieres añadir otra carrera a tu registro (Si/No)? ') == "Si"
         case 2:
              opt_cursos_ya_llevados=int(input("Ya has llevado este curso? digite 1 para Si o 2 para no: "))
              opt_cursos_ya_llevados=int(opt_cursos_ya_llevados)
              match opt_cursos_ya_llevados:
                  case 1:
                   opt_registrar_cursos_tipo=int(input("Lo aprobaste o reprobaste? digite 1 para aprobado o 2 para reprobado: "))    
                   match opt_registrar_cursos_tipo:
                       case 1:
                           agregar_cursos_aprobados_estudiante(l_cursos,l_estudiante)
                       case 2:    
                            agregar_cursos_reprobados_estudiante(l_cursos,l_estudiante)
                  case 2:
                      print("✌️ recuerda llevarlo pronto ✌️")
   for item1 in l_cursos_estu.items():
      print("""
      esta es la lista de cursos que escogió agregar a su registro:
      
      """,l_cursos_estu, """
      
      """)

   usuario = input("Escriba su usuario: ")
   usuario=usuario
   print(l_estudiante[usuario])
   l_estudiante[usuario]["cursos actuales: "]=l_cursos_estu
   print("""
      Este es su nuevo registro:
      """)
   print(l_estudiante[usuario])
   sleep(2)
   print("""
   Volviendo al menu.........""")
   sleep(2)
   print(inicio_estudiante_cc (l_estudiante,l_cursos))
#---------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------FUNCION PARA QUE EL ESTUDIANTE MATRICULE UN CURSO COMO APROBADO---------------------------------------------------
def agregar_cursos_aprobados_estudiante(l_cursos,l_estudiante):
   l_cursos_estu_aprobados={}
   continuar=True
   while continuar:
      print("""
      Estos son los cursos disponibles por el momento:
      
      """)
      print(l_cursos)
      print("")
      item2 = int(input('Por favor, seleccione de nuevo la posición en la que se encuentra el curso que desea añadir como aprobado a su registro según la lista anterior (ejemplo:el primer curso que aparece en la lista es la posición 0): '))
      item2=int(item2)
      curso_escogido_aprobado=l_cursos[item2]
      l_cursos_estu_aprobados[item2] = curso_escogido_aprobado
      print("")
      continuar = input('¿Quieres añadir otro curso aprobado a tu registro (Si/No)? ') == "Si"
   for item2 in l_cursos_estu_aprobados.items():
      print("""
      esta es la lista de cursos que escogió agregar a su registro como aprobado:
      
      """,l_cursos_estu_aprobados, """
      
      """)

   usuario = input("Escriba su usuario: ")
   usuario=usuario
   print(l_estudiante[usuario])
   l_estudiante[usuario]["cursos aprobados: "]=l_cursos_estu_aprobados
   print("""
      Este es su nuevo registro:
      """)
   print(l_estudiante[usuario])
   sleep(2)
   print("""
   Volviendo al menu.........""")
   sleep(2)
   print(inicio_estudiante_cc (l_estudiante,l_cursos))
#---------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------FUNCION PARA QUE EL ESTUDIANTE MATRICULE UN CURSO COMO REPROBADO---------------------------------------------------
def agregar_cursos_reprobados_estudiante(l_cursos,l_estudiante):
   l_cursos_estu_reprobados={}
   continuar=True
   while continuar:
      print("""
      Estos son los cursos disponibles por el momento:
      
      """)
      print(l_cursos)
      print("")
      item3 = int(input('Por favor, seleccione de nuevo la posición en la que se encuentra el curso que desea añadir como reprobado a su registro según la lista anterior (ejemplo:el primer curso que aparece en la lista es la posición 0): '))
      item3=int(item3)
      curso_escogido_reprobado=l_cursos[item3]
      l_cursos_estu_reprobados[item3] = curso_escogido_reprobado
      print("")
      continuar = input('¿Quieres añadir otro curso aprobado a tu registro (Si/No)? ') == "Si"
   for item3 in l_cursos_estu_reprobados.items():
      print("""
      esta es la lista de cursos que escogió agregar a su registro como reprobado:
      
      """,l_cursos_estu_reprobados, """
      
      """)

   usuario = input("Escriba su usuario: ")
   usuario=usuario
   print(l_estudiante[usuario])
   l_estudiante[usuario]["cursos reprobados: "]=l_cursos_estu_reprobados
   print("""
      Este es su nuevo registro:
      """)
   print(l_estudiante[usuario])
   sleep(2)
   print("""
   Volviendo al menu.........""")
   sleep(2)
   print(inicio_estudiante_cc (l_estudiante,l_cursos))
#---------------------------------FUNCION PARA QUE UN ESTUDIANTE SE REGISTRE------------------------------------------------------------------------
#NOTA: Esta función solo registrará el nombre de usuario,nombre completo y contraseña del estudiante, el registro de las carreras que desee matrícular se hará cuando el estudiante ya tenga una cuenta en el sistema

def agregar_registro_estudiante(l_estudiante): 
    usuario= input("Escriba su usuario: ")
    l_estudiante[usuario] = {} 
    l_estudiante[usuario]['nombre'] = input("Escriba su nombre: ")
    l_estudiante[usuario]['nombre']=l_estudiante[usuario]['nombre']
    l_estudiante[usuario]['password'] = cifrar(obtener_calve("Dijite una contraseña(solo caracteres numéricos): "))
    print(l_estudiante[usuario]) 
    print ("""
      Lista de estudiantes ahora:
        """)
    print(l_estudiante)
    print ("""
      Desea continuar
    
    """)
    print("1)si")
    print("2)no")
    opt_cont=int(input("\n\n\tDijite la opcion: "))
    match opt_cont:
                case 1:
                     print(menu_principal (l_admin,l_estudiante,l_cursos,l_carreras,dict_actividades))

#---------------------------Función para que el estudiante agregue carreras a su registro-----------------------------------
def agregar_carreras_estudiante(l_carreras,l_estudiante):
   l_carreras_estu={}
   continuar=True
   while continuar:
      print("""
      Estos son las carreras disponibles por el momento:
      
      """)
      print(l_carreras)
      print("")
      item = int(input('Seleccione la posición en la que se encuentra la carrera que desea añadir a su registro según la lista anterior(ejemplo:el primer curso que aparece en la lista es la posición 0): '))
      item=int(item)
      carrera_escogida=l_carreras[item]
      l_carreras_estu[item] = carrera_escogida
      print("")
      continuar = input('¿Quieres añadir otra carrera a tu registro (Si/No)? ') == "Si"
   for item in l_carreras_estu.items():
      print("""
      esta es la lista de carreras que escogió agregar a su registro:
      
      """,l_carreras_estu, """
      
      """)

   usuario = input("Escriba su usuario: ")
   usuario=usuario
   print(l_estudiante[usuario])
   #contraseña = input("Escriba su contraseña: ")
   #for usuario in l_estudiante and contraseña == l_estudiante[usuario]['password']:
      #print("""
      #usuario valido
      #""")
   l_estudiante[usuario]["carrera/as: "]=l_carreras_estu
   print("""
      Este es su nuevo registro:
      """)
   print(l_estudiante[usuario])
   sleep(2)
   print("""
   Volviendo al menu.........""")
   sleep(2)
   print(inicio_estudiante_cc (l_estudiante,l_cursos))
 
   
#-------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------FUNCION PARA LA OPCION DE MOSTRAR UN REGISTRO DEL ESTUDIANTE---------------------------------------------------
def mostrar_estudiante(l_estudiante):
    print (l_estudiante)
    print ("""Desea usted realizar otra acción: 
    1) si
    2) no """)   
    opt_seguir_estudiante=int(input("\n\n\tDijite la opcion: "))
    match opt_seguir_estudiante:
        case 1:
            inicio_estudiante_cc(l_estudiante,l_cursos)
        case 2:
            salir_programa()     
#-------------------------------------------------------------------------------------------------------------------------------------------------       

#---------------------------------FUNCION PARA LA AUTENTICACIÓN DEL ESTUDIANTE---------------------------------------------------------------------
def autenticacion_estudiante (l_estudiante):

    usuario = input("Escriba su usuario: ")
    contraseña = cifrar(obtener_calve("Escriba su contraseña: "))
    if usuario in l_estudiante and contraseña == l_estudiante[usuario]['password']:
            print("usuario valido, bienvenido")
            print (l_estudiante[usuario])
    else:
            print("usuario o contraseña invalida")
            print("desea usted registrarse: ")
            print ("1)si")
            print ("2)no")
            opt_registrarse=int(input("\n\n\tDijite la opcion: "))
            match opt_registrarse:
                case 1:
                      print(agregar_registro_estudiante(l_estudiante))
                case 2:
                    print("gracias por usar el sistema")          
#---------------------------------------------------------------------------------------------------------------------------------------------------   
# ------------------------------FUNCION PARA EL REGISTRO DE POSIBLES ACTIVIDADES-----------------------------------------------------------------------------
l_actividades=[]
l_actividades_recreativas={}
l_actividades_academicas={}
#----------------------------ACTIVIDADES RECREATIVAS-----------------------------------------------------
def agregar_registro_posibles_actividades_recreativas (l_actividades_recreativas): 
    print ("-------------🪅REGISTRO DE POSIBLE ACTIVIDAD RECREATIVA🪅-----------------")
    print ("""
            Para el registro de la actividad que desea realizar, por favor brindenos los siguientes datos 🖍: 
            """)
    l_actividades=[]
    actividad= input("Escriba una clave para la actividad (ejemplo: actividad1): ")
    l_actividades_recreativas[actividad] = {} 
    l_actividades_recreativas[actividad]['nombre'] = input("Escriba el nombre de la actividad: ")
    l_actividades_recreativas[actividad]['nombre']=l_actividades_recreativas[actividad]['nombre']
    l_actividades_recreativas[actividad]['fecha inicio'] = input("Escriba la fecha inicio en formato dd-mm-aaaa: ")
    l_actividades_recreativas[actividad]['fecha final'] = input("Escriba la fecha final en formato dd-mm-aaaa: ")
    l_actividades_recreativas[actividad]['horario'] = input("Escriba el horario: ")


    print ("""Registro creado:
     """)
    print(l_actividades_recreativas[actividad]) 
    print ("""
    Lista de actividades de su interes ahora:
     """)
    l_actividades.append(l_actividades_recreativas) 
    print(lista(l_actividades))

    print ("""
    Desea continuar
    
    """)
    print("1)si")
    print("2)no")
    opt_continuar=int(input("\n\n\tDijite la opcion: "))
    match opt_continuar:
                case 1:
                     inicio_estudiante_cc (l_estudiante,l_cursos)

#----------------------------ACTIVIDADES ACADEMICAS-----------------------------------------------------
def agregar_registro_posibles_actividades_académica (l_actividades_academicas,l_cursos,l_estudiante): 
    print ("-------------🤓REGISTRO DE POSIBLE ACTIVIDAD ACADEMICA🤓-----------------")
    print ("""
            Para el registro de la actividad que desea realizar, por favor brindenos los siguientes datos 🖍: 
            """)
    l_actividades=[]
    actividad= input("Escriba una clave para la actividad (ejemplo: actividad1): ")
    l_actividades_academicas[actividad] = {} 
    l_actividades_academicas[actividad]['nombre'] = input("Escriba el nombre de la actividad: ")
    l_actividades_academicas[actividad]['nombre']=l_actividades_academicas[actividad]['nombre']
    l_actividades_academicas[actividad]['fecha inicio'] = input("Escriba la fecha inicio en formato dd-mm-aaaa: ")
    l_actividades_academicas[actividad]['fecha final'] = input("Escriba la fecha final en formato dd-mm-aaaa: ")
    l_actividades_academicas[actividad]['horario'] = input("Escriba el horario: ")
    print("para registrar una actividad académica tiene que vincularla a un curso que lleve en el momento")
    print(l_cursos)
    item = int(input('Seleccione el curso,empezando en la posición 0: '))
    item=int(item)
    curso_escogido=l_cursos[item]
    curso_para_actividad=l_cursos[item]
    print(curso_escogido)
    usuario = input("Escriba su usuario: ")
  
    for  usuario in l_estudiante:
      for curso_escogido in l_estudiante[usuario]['cursos actuales: ']:
       print ("valido")  
       l_actividades_academicas[actividad]['curso'] = curso_para_actividad
      else:
         if curso_escogido not in l_estudiante[usuario]['cursos actuales: ']:
            print("la actividad no está asociada a un curso dentro de sus cursos actuales")

    print ("""Registro creado:
     """)
    print(l_actividades_academicas[actividad]) 
    print ("""
    Lista de actividades de su interes ahora:
     """)
    l_actividades.append(l_actividades_academicas) 
    print(lista(l_actividades))

    print ("""
    Desea continuar
    
    """)
    print("1)si")
    print("2)no")
    opt_continuar=int(input("\n\n\tDijite la opcion: "))
    match opt_continuar:
                case 1:
                     inicio_estudiante_cc (l_estudiante,l_cursos)
#----------UNION DE LAS DICCIONARIOS DE POSIBLES ACTIVIDADES EN UNA LISTA---------------------------------------------
def lista(l_actividades):
   l_actividades=[l_actividades_recreativas] +[l_actividades_academicas]
   print(l_actividades)

#--------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------AGREGAR ACTIVIDADES-----------------------------------------------------------------------
def agregar_actividades_registro(l_estudiante,l_actividades):
   print(l_actividades)
   continuar=True
   while continuar:
      print("""
      Estos son las actividades disponibles por el momento:
      
      """)
      
      print("")
      item = int(input('Seleccione la posición en la que se encuentra la carrera que desea añadir a su registro según la lista anterior: '))
      item=int(item)
      actividad_escogida=l_actividades[item]
      l_actividades_estu[item] = actividad_escogida
      print("")
      continuar = input('¿Quieres añadir otra carrera a tu registro (Si/No)? ') == "Si"
   for item in l_actividades_estu.items():
      print("""
      esta es la lista de carreras que escogió agregar a su registro:
      
      """,l_actividades_estu, """
      
      """)

   usuario = input("Escriba su usuario: ")
   for  usuario in l_estudiante:
      for l_actividades_estu in l_estudiante[usuario]['cursos actuales: ']["horario"]:
       print ("no valido")  
      else:
         if l_actividades_estu not in l_estudiante[usuario]['cursos actuales: ']:
            print("valida")
            l_estudiante[usuario]['actividades'] = l_actividades_estu
   print("""
   Volviendo al menu.........""")
   print(inicio_estudiante_cc (l_estudiante,l_cursos))             
#--------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------FUNCIÓN DE REPORTE DE ACTIVIDADES------------------------------------------------------------
def reporte(l_estudiante):
    print("""
    📋Bienvenido, haz seleccionado la opción para crear un reporte📋
    """)
    print ("""Por favor brindenos estos datos para acceder al registro de sus actividades: """)
    usuario = input("Escriba su usuario: ")
    contraseña =cifrar(obtener_calve("Escriba su contraseña: "))
    if usuario in l_estudiante and contraseña == l_estudiante[usuario]['password']:
        print("¡usuario y contraseña validas!")
        print("""
        Este es su registro:
        """)
        print(l_estudiante[usuario])
        print ("""
        Basados en su registro, estos son los cursos para el reporte:

        """)
        print(l_estudiante[usuario]["cursos actuales: "])
    
        print("""
        Estas son sus actividades registradas

        """)
        print(l_estudiante[usuario]['actividades'])
        





#____________________________________MENU INTERACTIVO CON EL USUARIO_______________________________________________________________________________
#-------Lista de administradores-------------------
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
#-------Lista de estudiantes----------------------------------------------------------------------------------- 
l_estudiante={
        "maj": {
            "nombre": "Maria Solis",
            "password": cifrar("109"),
            "carrera":"Agronomía"
    }
 } 
#---------Lista cursos--------------------------------------------------------------------------------------
l_cursos= (
    {"nombre":"Matemática General","creditos":"3","fech.inicio":"9/2/2022","fech.finalización":"16/6/2022", "horario":"Martes de 1 p.m a 3 p.m","carreras":"Ing.Computación, Agronomía"},
    {"nombre":"Inglés Básico","creditos":"","fech.inicio":"9/2/2022","fech.finalización":"16/6/2022", "horario":"Viernes de 9 a.m a 11:30 a.m","carreras":"Ing.Computación, Agronomía, Administración"},  
    {"nombre":"Natacion","creditos":"0","fech.inicio":"9/2/2022","fech.finalización":"16/6/2022", "horario":"Lunes de 1 p.m a 3 p.m","carreras":"Ing.Computación,Agronomía,Ing.Electrónica,Administración"},
    
 ) 
#------------Listas y diccionarios necesarias para que el admin pueda registrar un cursos---------------------------------- 
l_cursos_nuevo={}
carrera_valida_list=[] 
dict_actividades={}

#-------------Diccionario de actividades-------------------------------------------------------------------------------
l_actividades={


    
} 

#---------------Tupla de carreras------------------------------------------------------------------------------------------------------------

l_carreras=("Administración de empresas","Agronomía","Ing.Computación","Ing.Electrónica") 

# ------------------------------------------FUNCIÓN DEL MENÚ----------------------------------------------------------------------------------
def menu_principal (l_admin,l_estudiante,l_cursos,l_carreras,dict_actividades):
    while True:
        limpiar_terminal()
        print("""
                  *********************************************
                  ⏳Bienvenido a su administrador del tiempo⏳
                  *********************************************  
        
        Cuenta usted con algún registro previo?:

        """)
        print("1) Si")
        print("2) No")
        opt_si_tiene_cuenta=int (input("\n\n\tDijite la opcion: "))
        match opt_si_tiene_cuenta:
          case 1:
                print ("""

                 🕰  Hola, bienvenido de nuevo a tu sistema de administración del tiempo  🕰  
               
                Escoja su tipo de usuario:

                """ )
                print ("1) Administrador ")
                print ("2) Estudiante ")
                print ("3) Salir")

                opt=int (input("\n\n\tDijite el numero correspondiente:  "))

                match opt:
                    case 1:
                        autenticar_admin(l_admin)
                        print("""

                        💼 Es usted un administrador, por favor indique la acción que quiere realizar 💼
                        
                        """)
                        print (inicio_administrador_cc(l_admin,l_cursos,l_cursos_nuevo,carrera_valida_list,l_carreras))
                    case 2:
                        autenticacion_estudiante(l_estudiante)
                        print("""

                        🎒 Es usted un estudiante, por favor indique la acción que quiere realizar 🎒
                        
                        """)
                        inicio_estudiante_cc (l_estudiante,l_cursos) 
                    
                        
                    case 3:
                        salir_programa()
                    
                        break
                    

                    case _:
                        print("\n\t!No es una opción válida¡")
             
          case 2:
             print (""" Desea usted registrarse?🤔
             
             """)
             print("1) Si ")
             print("2) No")
             opt_decide_registrar=int (input("\n\n\tQué desea: "))
             match opt_decide_registrar:
                 case 1:
                     print("""Cuál es su tipo de usuario:

                       1) administrador 💼
                       2) estudiante 🎒
                       
                        """)
                     opt_que_es=int(input("\n\n\tDigite su respuesta:  "))
                     match opt_que_es:
                        
                        case 1:    
                             print("""

                                💼 Es usted un administrador, por favor indique la acción que quiere realizar 💼

                                """)  
                             print ("1) Agregar un registro ")
                             print ("2) Salir ")
                             opt_administrador=int (input("\n\n\tQué desea: "))
                             match opt_administrador:
                                    case 1:
                                        agregar_registro_administrador(l_admin)
                                    case 2:
                                        salir_programa()  

                        case 2:    
                             print("""

                                🎒 Es usted un estudiante, por favor indique la acción que quiere realizar 🎒

                                """)
                             print ("1) Agregar un registro ")
                             print ("2) Salir")
                             opt_estudiante=int (input("\n\n\tQué desea: "))
                             match opt_estudiante:
                                case 1: 
                                    agregar_registro_estudiante(l_estudiante)
                                case 2:
                                    salir_programa()
                 case 2:
                     print (""" 🤗 Ha decidido usted la opción de no registrarse, esperamos poder ayudarle luego 🤗""")
                     salir_programa()