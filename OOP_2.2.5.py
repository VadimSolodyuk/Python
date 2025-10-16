"""Подвиг 5. Объявите в программе класс WindowDlg, объекты которого
предполагается создавать командой:
wnd = WindowDlg(заголовок окна, ширина, высота)
                  
В каждом объекте класса WindowDlg должны создаваться приватные локальные
атрибуты:
__title - заголовок окна (строка);
__width, __height - ширина и высота окна (числа).

В классе WindowDlg необходимо реализовать метод:
show() - для отображения окна на экране (выводит в консоль строку
в формате:
"<Заголовок>: <ширина>, <высота>", например "Диалог 1: 100, 50").

Также в классе WindowDlg необходимо реализовать два объекта-свойства:
width - для изменения и считывания ширины окна;
height - для изменения и считывания высоты окна.

При изменении размеров окна необходимо выполнять проверку:
- переданное значение является целым числом в диапазоне [0; 10000].

Если хотя бы один размер изменился (высота или ширина), то следует 
выполнить автоматическую перерисовку окна (вызвать метод show()).
При начальной инициализации размеров width, height вызывать метод show()
не нужно.

P.S. В программе нужно объявить только класс с требуемой 
функциональностью.
"""

class WindowDlg:
    min_window_size = 0
    max_window_size = 10000
    
    def __init__(self, title, width, height):
        self.set_title(title)
        self.__width = width
        self.__height = height
        
    def set_title(self, title):
        self.__check_title(title)
        self.__title = title
    
    @classmethod        
    def __check_title(cls, title):
        if not isinstance(title, str):
            raise TypeError
    
    def show(self):
        print(f"{self.__title}: {self.width}, {self.height}")
        
    @property
    def width(self):
        return self.__width    
        
    @width.setter
    def width(self, width):
        self.__check_size(width)
        self.__width = width
        self.show()
        
    @property
    def height(self):
        return self.__height    
        
    @height.setter
    def height(self, height):
        self.__check_size(height)
        self.__height = height
        self.show()
    
    @classmethod    
    def __check_size(cls, value):
        if type(value) != int:
            raise TypeError
        if not (cls.min_window_size <= value <= cls.max_window_size):
            raise ValueError
    
wind = WindowDlg("Main", 0 , 30)        
    
wind.show()
wind.width = 10
wind.height = 20