from abc import ABC


class Color(ABC):
    """
    Clase Color permite crea objetos de tipo Color
    """

    def __init__(self, color=None):
        self._color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, new_color):
        self._color = new_color

    def __str__(self):
         return f'Color: {self.__dict__}'


if __name__ == '__main__':
    c1 = Color(color='verde')
    print(c1)