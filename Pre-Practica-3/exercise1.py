class Vehiculo:
    def __init__(self, marca: str, ruedas: int, color: str) -> None:
        # Constructor de la clase Vehiculo
        self.marca = marca
        self.ruedas = ruedas
        self.color = color
        self.enMarcha = False  # Inicialmente el vehículo NO está en marcha

    def arrancar(self):
        # Método para arrancar el vehículo
        if self.enMarcha == False:
            print("El vehículo está APAGADO")
        else:
            print("El vehículo está EN MARCHA")

    def tipoVehiculo(self):
        # Método para determinar el tipo de vehículo basado en el número de ruedas
        if self.ruedas == 4:
            print("El vehículo es un AUTOMOVIL")
        elif self.ruedas == 2:
            print("El vehículo es una MOTOCICLETA")

    def mostrar(self):
        # Método para mostrar la información del vehículo
        print("La marca del vehículo es:", self.marca)
        print("La cantidad de ruedas son:", self.ruedas)
        print("El color del vehículo es:", self.color)
        print("\n")


# Crear una instancia de la clase Vehiculo
c1 = Vehiculo('Lamborghini', 2, 'Rojo')

# Mostrar la información del vehículo
c1.mostrar()

# Arrancar el vehículo
c1.arrancar()

# Determinar el tipo de vehículo
c1.tipoVehiculo()



"""
--Datos de los estudiantes--
    Comisión : 107
    Grupo : 4
    Integrantes:
                -Legajo 51910,Luciano Melo Claps.
                -Legajo 51886,Ezequiel Espinoza.
                -Legajo 51641,Camilo Carabajal
""" 