from Color import Color
from FiguraGeometrica import FiguraGeometrica

class triangulo(Color,FiguraGeometrica):
    """
    Clase que crea objeto de tipo triangulo
    """
    def __init__(self, base=None, altura=None):
        FiguraGeometrica.__init__(self, ancho=base, alto=altura)

    def __str__(self):
        return f'triangulo: {self.__dict__}'

if __name__ == '__main__':
    t1 = triangulo(base=3, altura=4)
    print(t1)
    print(triangulo.mro())
    print(t1.area())