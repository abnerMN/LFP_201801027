from tkinter import filedialog, Tk
from Pelicula import Pelicula

peliculas=[]

def leer_archivo():
    Tk().withdraw()
    archivo = filedialog.askopenfile(
        title= "Seleccione un archivo",
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
            tmp_nombre = None
            tmp_autores = None
            tmp_anio = None
            tmp_genero = None
            for j in i:
                if count == 1:
                    tmp_nombre = j
                elif count == 2:
                    j = j.split(",")
                    tmp_autores = j
                elif count == 3:
                    tmp_anio = j
                elif count == 4:
                    tmp_genero = j
                count += 1
            peli = Pelicula(contador,tmp_nombre, tmp_autores, tmp_anio, tmp_genero)
            contador+=1
            peliculas.append(peli)


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

def meu():
    pass

leer_archivo()
for peli in peliculas:
    peli.mostrar_informacion()