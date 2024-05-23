from Color import Color
from FiguraGeometrica import FiguraGeometrica

class Cuadrado(Color,FiguraGeometrica):
    """
    Clase que crea objeto de tipo Cuadrado
    """
    def __init__(self, lado=None, color=None):
        FiguraGeometrica.__init__(self, ancho=lado, alto=lado)
        Color.__init__(self, color=color)

    def __str__(self):
        return f'Cuadrado: {self.__dict__}'

if __name__ == '__main__':
    c1 = Cuadrado(lado=4, color='VERDE')
    print(c1)
    print(Cuadrado.mro())
    print(c1.area())