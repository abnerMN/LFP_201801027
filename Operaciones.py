from tkinter import filedialog, Tk
from Pelicula import Pelicula

peliculas=[]
actores={}

#lee el archivo y almacena la informacion
def leer_archivo():
    global actores
    Tk().withdraw()
    archivo = filedialog.askopenfile(
        title= "sle un archivo",
        initialdir="./",
        filetypes= {
            ("archivos LFP", "*.lfp")
        }
    )
    if archivo is None:
        return None
    else:
        contador=1
        cont_act=1
        texto = archivo.readlines()
        for i in texto:
            i= i.split(";")
            count = 1
            t_nombre = None
            t_actores = None
            t_anhio = None
            t_genero = None
            for j in i:
                if count == 1:
                    t_nombre = j.strip()
                elif count == 2:
                    j = j.split(",")
                    at=[]
                    for s in j:
                        at.append(s.strip())
                    t_actores = at
                elif count == 3:
                    t_anhio = j.strip()
                elif count == 4:
                    t_genero = j.strip()
                count += 1
            if buscar_pelicula(t_nombre)== True:
                for p in peliculas:
                    if p.getNombre()==t_nombre:
                        p.setActores(t_actores)
                        p.setAnho(t_anhio)
                        p.setGenero(t_genero)
                    else:
                        pass
            else:
                peli = Pelicula(contador,t_nombre, t_actores, t_anhio, t_genero)
                for act in t_actores:
                    if act in actores:
                        pass
                    else:
                        actores.setdefault(act,cont_act)
                        cont_act+=1
                contador+=1
                peliculas.append(peli)

#metodo para validar la existencia de una pelicula en los registros
def buscar_pelicula(nombre_peli):
    global peliculas
    bandera= False
    for p in peliculas:
        if p.getNombre()==nombre_peli:
            bandera=True
    return bandera

#metodo para buscar actores 
def buscar_actor(nombre_actor):
    pass

def mostrar_actores():
    pass

#mostrar peliculas donde aparece un actor
def mostrar_pelixNombre (nombre_actor):
    global peliculas
    tmp_peli=[]
    for peli in peliculas:
        for act in peli.getActores():
            if nombre_actor == act:
                tmp_peli.append(peli)
            else:
                pass
    print(nombre_actor)
    for p in tmp_peli:
        p.mostrar_busquedaXator()
        print()



def filtrar_xActor():
    global peliculas, actores
    sla=-1
    while (sla!=0):
        print('********** Actores registrados **********')
        for act in actores:
            print(actores[act] ,'.- ',act)
        print('0.- Regresar')
        try:
            sla=int(input('*** Seleccione una opcion ***\n'))
            if sla>0 and sla <= len(actores):
                for act in actores:
                    if sla == actores[act]:
                        mostrar_pelixNombre(act)
                    else:
                         pass
            elif sla==0:
                break
            else:
                print('*** Opcion invalida ***')
            pausa_informacion()
        except:
            print('*** Por favor seleccione una opcion valida -Err: filtrar_xActor***')


def filtrar_xAnho():
    pass

def filtrar_xGenero():
    pass

def graficar():
    pass

#metodo para imprimir toda la informacion contenida de las peliculas
def mostrar_peliculas():
    global peliculas
    if validacion_arrVacio():
        for peli in peliculas:
            peli.mostrar_informacion()
    else:
        print('----- No hay elementos registrados -----')

#mostrar la informacion de las peliculas con el id para el menu 2
def mostrar_peliId():
    global peliculas
    if validacion_arrVacio():
        for peli in peliculas:
            peli.mostrar_peli()
    else:
        print('----- No hay elementos registrados -----')

#validacion si el arreglo esta vacio peliculas
def validacion_arrVacio():
    global peliculas
    if peliculas:
        bandera=True
    else:
        bandera=False
    return bandera

#metodo para pausar la ejecucion del programa
def pausa_informacion():
    print('        ******** presiona una tecla para continuar *****')
    ms_tp= input()




#-------------------------------------------- Menus -------------------------------------------------------
#menu filtrado
def menu_3():
    if validacion_arrVacio():
        sl_pel=-1
        while (sl_pel!=4):
            try:
                print(
'''
1. Filtrar por Actor
2. FIltrar por Año
3. Filtrar por genero
'''
                )
                sl_pel=int(input("*** Seleccione una opcion ***\n"))
                if sl_pel==1:
                    filtrar_xActor()
                    pausa_informacion()
                elif sl_pel==2:
                    pass
                elif sl_pel==3:
                    pass
                elif sl_pel==4:
                    sl_pel=4
                else:
                    print('*** Opcion Invalida ***')
            except:
                print('*** Por favor seleccione una opcion valida -Err: menu_3filtrado***')
    else:
        print('----- No hay elementos registrados -----')

#menu para mostrar los actores
def menu_2actores():
    global peliculas
    if validacion_arrVacio():
        seleccion_peli=-1
        while (seleccion_peli!=0):
            mostrar_peliId()
            print('0- Regresar')
            try:
                seleccion_peli=int(input("*** Seleccione una opcion ***\n"))
                if seleccion_peli>0 and seleccion_peli<=len(peliculas):
                    actores=peliculas[seleccion_peli-1].getActores()
                    print(peliculas[seleccion_peli-1].getNombre())
                    for act in actores:
                        print("     -"+act)
                    pausa_informacion()
                elif seleccion_peli==0:
                    seleccion_peli=0
                else:
                    print('*** Opcion Invalida ***')
            except:
                print('*** Por favor seleccione una opcion valida -Err: menu_2Actores***')
    else:
        print('----- No hay elementos registrados -----')

#menu gestionar peliculas
def menu_2():
    sel2=0
    while(sel2!=3):
        print('''
1. Mostrar Peliculas
2. Mostrar Actores
3. regresar
''')
        try:
            sel2=int(input("*** Seleccione una opcion ***\n"))
            if sel2 == 1:
                mostrar_peliculas()
                pausa_informacion()
            elif sel2 ==2:
                menu_2actores()
                pausa_informacion()
            elif sel2 == 3:
                print('regresando')
                sel2=3
            else:
                print ('*** Opcion no disponible ***')
        except:
            print('*** Por favor seleccione una opcion valida -Err: menu_2***')
        

#toda la informacion del menu
def menu():
    mensaje_inicio()
    pausa_informacion()
    sl= 0
    while (sl !=6):
        print(
            '''
**************************
        MENU
**************************
1. Cargar Archivo
2. Gestionar Peliculas
3. Filtrar Peliculas
4. Graficar
5. Mostrar informacion del estudiante
6. salir
**************************
            '''
        )
        try:
            sl = int(input('seleccione una opcion: \n'))
            if sl == 1:
                leer_archivo()
                mostrar_peliculas()
                pausa_informacion()
            elif sl ==2:
                menu_2()
            elif sl == 3:
                print('filtrar peliculas')
            elif sl == 4:
                print('')
            elif sl == 5:
                mensaje_inicio()
                pausa_informacion()
            elif sl == 6:
                print('bye')
                sl=6
            else:
                print ('*** Opcion no disponible ***')
        except:
            print('*** Por favor seleccione una opcion valida -Err: menu***')
            

#mensaje de informacion de la clase y estudiante
def mensaje_inicio():
    print(
        '''
        --------------------------------------------------
        |**** LENGUAJES FORMALES Y DE PROGRAMACION ****  |
        |     Seccion: B-                                |
        |     Carne: 201801027                           |
        |     Nombre: Abner Martín Noj Hernández         |
        -------------------------------------------------- 
        '''
        )


#main
if __name__== "__main__":
  #  menu()
  leer_archivo()
  menu_3()

                
