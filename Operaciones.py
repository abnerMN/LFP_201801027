from tkinter import filedialog, Tk
from Pelicula import Pelicula
import os

peliculas=[]

#----------------------------ingreso de informacion -----------------------
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
                contador+=1
                peliculas.append(peli)
        archivo.close()

#---------------------------- manejo de la informacion -------------------
#metodo para validar la existencia de una pelicula en los registros
def buscar_pelicula(nombre_peli):
    global peliculas
    bandera= False
    for p in peliculas:
        if p.getNombre()==nombre_peli:
            bandera=True
    return bandera

#metodo para filtrar la inforacion por medio del genero de las peliculas
def mostrar_pelixGenero(genero):
    global peliculas
    tmp_peli=[]
    for peli in peliculas:
        if genero == peli.getGenero():
            tmp_peli.append(peli)
        else:
            pass
    print('\n',genero)
    for p in tmp_peli:
        p.mostrar_busquedaGenero()
        print()

#metodo para mostrar la informacion de peliculas por medio del año
def mostrar_pelixAnho(anho):
    global peliculas
    tmp_peli=[]
    for peli in peliculas:
        if anho == peli.getAnho():
            tmp_peli.append(peli)
        else:
            pass
    print('\n',anho)
    for p in tmp_peli:
        p.mostrar_busquedaAnho()
        print()

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
    print('\n',nombre_actor)
    for p in tmp_peli:
        p.mostrar_busquedaXator()
        print()

#metodo para filtrar la informacion por medio del nombre del actor
def filtrar_xActor():
    global peliculas
    actores={}
    contador=1
    for peli in peliculas:
        for ac in peli.getActores():
            if ac in actores:
                pass
            else:
                actores.setdefault(ac,contador)
                contador+=1
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

#metodo para filtrar la informacion por medio del año de publicacion
def filtrar_xAnho():
    global peliculas
    anhos={}
    contador=1
    for peli in peliculas:
        if peli.getAnho() in anhos:
            pass
        else:
            anhos.setdefault(peli.getAnho(),contador)
            contador+=1
    slan=-1
    while (slan!=0):   
        for a in anhos:
            print(anhos[a], '.- ',a)
        print('0 .-  Regresar')
        try:
            slan=int(input('*** Seleccione una opcion ***\n'))
            if slan>0 and slan<= len(anhos):
                for a in anhos:
                    if slan== anhos[a]:
                        mostrar_pelixAnho(a)
                    else:
                        pass
            elif slan==0:
                break
            else:
                print('*** Opcion invalida ***')
            pausa_informacion()
        except:
            print('*** Por favor seleccione una opcion valida -Err: filtrar_xAnho***')
 

#metodo para filtrar la informacion por medio del genero de la pelicula
def filtrar_xGenero():
    global peliculas
    generos={}
    contador=1
    for peli in peliculas:
        if peli.getGenero() in generos:
            pass
        else:
            generos.setdefault(peli.getGenero(),contador)
            contador+=1
    slan=-1
    while (slan!=0):   
        for a in generos:
            print(generos[a], '.- ',a)
        print('0 .-  Regresar')
        try:
            slan=int(input('*** Seleccione una opcion ***\n'))
            if slan>0 and slan<= len(generos):
                for g in generos:
                    if slan== generos[g]:
                        mostrar_pelixGenero(g)
                    else:
                        pass
            elif slan==0:
                break
            else:
                print('*** Opcion invalida ***')
            pausa_informacion()
        except:
            print('*** Por favor seleccione una opcion valida -Err: filtrar_xAnho***')


#--------------------------------grafica de la informacion ---------------------
def graficar():
    global peliculas
    actores={}
    cont=1
    if validacion_arrVacio():
        for peli in peliculas:
            for ac in peli.getActores():
                if ac in actores:
                    pass
                else:
                    actores.setdefault(ac,cont)
                    cont+=1           
        archivo_DOT= open("imagen.dot","w")
        txt='''digraph {
    rankdir = LR
    '''
        for peli in peliculas:
            txt+='''
    pelicula'''+str(peli.getId())+'''[
        shape="record", label="'''+peli.getNombre()+'''|{'''+peli.getAnho()+''' | '''+peli.getGenero()+'''}",
        color= blue
        ]
            '''
        
        for ac in actores:
            txt+='''
    actor'''+str(actores[ac])+'''[shape="box", color=green, style=filled
        label="'''+ac+'''"
        ]
'''
        for ac in actores:
            for peli in peliculas:
                for act in peli.getActores():
                    if ac == act:
                        txt+="pelicula"+str(peli.getId())+"->"+"actor"+str(actores[ac])+'\n'
                    else:
                        pass

        txt+="}"
        archivo_DOT.write(txt)
        archivo_DOT.close()
        os.system("dot.exe -Tpdf imagen.dot -o grafica.pdf")
    else:
        print('----- No se puede graficar, No hay elementos registrados Err: graficar-----')


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
4. Regresar
'''
                )
                sl_pel=int(input("*** Seleccione una opcion ***\n"))
                if sl_pel==1:
                    filtrar_xActor()
                    pausa_informacion()
                elif sl_pel==2:
                    filtrar_xAnho()
                    pausa_informacion()
                elif sl_pel==3:
                    filtrar_xGenero()
                    pausa_informacion()
                elif sl_pel==4:
                    break
                else:
                    print('*** Opcion Invalida ***')
                    pausa_informacion()
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
            try:
                mostrar_peliId()
                print('0- Regresar')
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
                    pausa_informacion()
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
                break
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
                pausa_informacion()
            elif sl == 3:
                menu_3()
                pausa_informacion()
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
                pausa_informacion()
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
   # menu()
   leer_archivo()
   graficar()
                
