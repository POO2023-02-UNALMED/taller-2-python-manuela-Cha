from dataclasses import dataclass
@dataclass
class Motor:
    numeroCilindros: int
    tipo: str
    registro: int

    def cambiarRegistro(self, registro):
        """asigna el nuevo registro"""
        self.registro = registro

    def asignarTipo(self, tipo):
        """asigna el nuevo tipo de motor si este es electrico o gasolina"""
        if tipo == "electrico" or tipo == "gasolina":
            self.tipo = tipo

@dataclass
class Asiento():
    color: str
    precio: int
    registro: int

    def cambiarColor(self, color):
        """por medio de un diccionario con los valores validos para el color del asiento se restringe el hecho de que este atributo tome otro color no valido """
        dictColor = {}
        dictColor['rojo'] = "valido"
        dictColor["verde"] = "valido"
        dictColor["amarillo"] = "valido"
        dictColor["negro"] = "valido"
        dictColor["blanco"] = "valido"
        if dictColor.get(color,"no valido")== "valido":
            self.color = color

@dataclass
class Auto():
    modelo: str
    precio: int
    asientos: list[Asiento]
    marca: str
    motor: Motor
    registro: int
    cantidadCreados: int=0

    def cantidadAsientos(self):
        """Devuelve la cantidad de asientos que son objetos Asiento en la lista del objeto Auto"""
        return len([asiento for asiento in self.asientos if isinstance(asiento, Asiento)])

    def verificarIntegridad(self):
        """Se encarga de revisar que el atributo registro de Motor, Auto y Cada Asiento sean el mismo"""
        registros_iguales = True
        registro_motor = self.motor.registro
        for asiento in self.asientos:
            if asiento.registro != registro_motor:
                registros_iguales = False
                break
        return "Auto original" if registros_iguales else "Las piezas no son originales"


