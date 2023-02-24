class Pelicula:
    def __init__(self,id,nombre, actores,anho, genero):
        self.id=id
        self.nombre=nombre
        self.actores=actores
        self.anho=anho
        self.genero=genero
    
    def getNombre(self):
        return self.nombre
    
    def getActores(self):
        return self.actores
    
    def getAnho(self):
        return self.anho
    
    def getGenero(self):
        return self.genero
    
    def setNombre(self, nombre):
        self.nombre=nombre
    
    def setActores(self,actores):
        self.actores=actores

    def setAnho(self,anho):
        self.anho=anho

    def setGenero(self, genero):
        self.genero=genero
    
    def mostrar_informacion(self):
        print ('Nombre: ',self.nombre ,'\n   Actores: ' ,self.actores ,'\n   Año: ' , str(self.anho) , '\n   Genero: ',self.genero +'\n' )

    def mostrar_peli(self):
        print (str(self.id)+ '- Nombre: ',self.nombre)
    
    def mostrar_busquedaXator(self):
        print (
            '   Nombre: ', self.nombre,'\n',
            '   Anho: ', self.genero,'\n',
            '   Genero: ', self.genero
        )

    def mostrar_busquedaAnho(self):
        print(
            '   Nombre: ',self.nombre,'\n'
            '   Genero: ',self.genero
        )

    def mostrar_busquedaGenero(self):
        print(
            '   Nombre: ',self.nombre,'\n'
            '   Año: ',self.anho
        )
    