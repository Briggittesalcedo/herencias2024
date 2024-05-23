from Color import Color
from FiguraGeometrica import FiguraGeometrica

class Rectangulo(Color,FiguraGeometrica):

    """
    Clase que crea objeto de tipo Rectangulo
    """
    def __init__(self, base=None, altura=None):
        FiguraGeometrica.__init__(self, ancho=base, alto=altura)

    def __str__(self):
        return f'rectangulo: {self.__dict__}'

if __name__ == '__main__':
    r1 = Rectangulo(base=5, altura=6,)
    print(r1)
    print(Rectangulo.mro())
    print(r1.area())
