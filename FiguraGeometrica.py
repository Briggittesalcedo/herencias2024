class FiguraGeometrica:
    """
    Clase que permite crear objetos de tipo Figura Geometrica
    """
    def __init__(self, ancho=None, alto=None):
        self._ancho = ancho
        self._alto = alto

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        self._ancho = ancho

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        self._alto = alto

    def area(self):
        return self._alto * self._ancho

    def __str__(self):
        return f'Figura Geometrica: {self.__dict__}'


if __name__ == '__main__':
    fg1 = FiguraGeometrica(ancho=5, alto=6)
    fg2 = FiguraGeometrica(ancho=3, alto=5)
    print(fg1)
    print(fg2)