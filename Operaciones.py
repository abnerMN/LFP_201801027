from tkinter import filedialog, Tk
from Pelicula import Pelicula

peliculas=[]

#lee el archivo y almacena la informacion
def leer_archivo():
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

def mostrar_peliculas():
    pass

def mostrar_actores():
    pass

def filtrar_xActor():
    pass

def filtrar_xAnho():
    pass

def filtrar_xGenero():
    pass

def graficar():
    pass

def mostrar_peliculas():
    global peliculas
    for peli in peliculas:
        peli.mostrar_informacion()

def pausa_informacion():
    print('        ******** presiona una tecla para continuar *****')
    ms_tp= input()

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
                print('gestion de peliculas')
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
            print('*** Por favor seleccione una opcion valida ***')
            


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



if __name__== "__main__":
    menu()


   