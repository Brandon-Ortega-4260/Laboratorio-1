# Poner estaciones en civil 3D
class PonerEstaciones():
    def __init__(self):
        self.Nombre = input("Ingrese nombre de la estacion: ")
        self.Tamaño = float(input("Ingrese La distancia de la estacion: "))
        self.Grados = input("Ingrese los Grados de la estacion: ")
        self.Altura= float(input("Ingrese la Altura de la estacion: "))
    def Imprimir(self):
        print(" ")
        print("Nombre:", self.Nombre)
        print("Tamaño:", self.Tamaño)
        print("Grados:", self.Grados)
        print("Altura", self.Altura)
        print("")

    def FinEstacion(self):
        if int(self.Grados) <90:
            print("La Estacion estara a la derecha")
        elif int(self.Grados) == 90:
            print("La estacion estara en el centro")
        else:
            print("la Estacion estara a la izquierda")


# Programa principal
Estacion1 = PonerEstaciones()
Estacion2 = PonerEstaciones()
Estacion3 = PonerEstaciones()
Estacion4 = PonerEstaciones()

Estacion1.Imprimir()
Estacion1.FinEstacion()
Estacion2.Imprimir()
Estacion2.FinEstacion()
Estacion3.Imprimir()
Estacion3.FinEstacion()
Estacion4.Imprimir()
Estacion4.FinEstacion()


