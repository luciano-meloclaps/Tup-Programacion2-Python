"""Variables de Clase y Métodos de Clase."""


class Article:
    iva: float = 0.21
    """Todos los artículos tienen un nombre y un costo, opcionalmente algunos
    tienen un porcentaje de descuento.

    El IVA es un impuesto que se aplica a todos los productos por igual,
    actualmente es de 21% pero puede cambiar en el futuro.

    Para calcular el precio de un artículo, hay que sumar el IVA y luego restar
    los descuentos si hubiera. Redondear a 2 decimales.

    Restricciones:
        - Utilizar 3 variables de instancia
        - Utilizar 1 método de instancia
        - Utilizar 1 variable de clase
        - Utilizar 1 método de clase
        - No utilizar Dataclasses
        - No utilizar Properties
        - Utilizar Type Hints en todos los métodos y variables
    """

    def __init__(self, auto: str, costo: float, descuento: float = 0.0) -> None:
        # Inicialización de las variables de instancia
        self.auto: str = auto
        self.costo: float = costo
        self.descuento: float = descuento

    def calcular_precio(self) -> float:
        # Cálculo del precio teniendo en cuenta el IVA y el descuento
        precio_sin_descuento: float = self.costo + (self.costo * self.iva)  # Precio sin descuento
        precio_con_descuento: float = precio_sin_descuento - (precio_sin_descuento * self.descuento)  # Precio con descuento
        return round(precio_con_descuento, 2)  # Devuelve el precio final redondeado a 2 decimales

    @classmethod
    def actualizar_iva(cls, nuevo_iva: float) -> None:
        # Actualización del valor del IVA
        cls.iva = nuevo_iva

# NO MODIFICAR - INICIO
# Test parámetro obligatorio
try:
    article = Article()
    assert False, "No se puede instanciar sin nombre ni costo"
except TypeError:
    assert True

try:
    article = Article("Auto")
    assert False, "No se puede instanciar sin costo"
except TypeError:
    assert True

try:
    article = Article(auto="Auto", costo=1)
    assert True
except TypeError:
    assert False, "El descuento es opcional"

# Test básico
article = Article("Auto", 1)
assert article.auto == "Auto"
assert article.calcular_precio() == 1.21


article = Article("Auto", 1, 0.21)
assert article.auto == "Auto"
assert article.calcular_precio() == 0.96


# Test palabra clave
article = Article(costo=1, auto="Auto")
assert article.auto == "Auto"
assert article.calcular_precio() == 1.21

article = Article(costo=1, auto="Auto", descuento=0.21)
assert article.auto == "Auto"
assert article.calcular_precio() == 0.96


# Test de método de clase
Article.actualizar_iva(0.25)

article = Article(costo=1, auto="Auto")
assert article.auto == "Auto"
assert article.calcular_precio() == 1.25
# NO MODIFICAR - FIN