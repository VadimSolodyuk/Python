"""Подвиг 9 (на закрепление). Вам требуется сформировать класс PathLines для описания маршрутов,
состоящих из линейных сегментов. При этом каждый линейный сегмент предполагается задавать отдельным классом LineTo.
Объекты этого класса будут формироваться командой:
line = LineTo(x, y)
где x, y - следующая координата линейного участка (начало маршрута из точки 0, 0).

В каждом объекте класса LineTo должны формироваться локальные атрибуты:
x, y - для хранения координат конца линии (начало определяется по координатам предыдущего объекта).

Объекты класса PathLines должны создаваться командами:
p = PathLines()                   # начало маршрута из точки 0, 0
p = PathLines(line1, line2, ...)  # начало маршрута из точки 0, 0
где line1, line2, ... - объекты класса LineTo.

Сам же класс PathLines должен иметь следующие методы:
get_path() - возвращает список из объектов класса LineTo (если объектов нет, то пустой список);
get_length() - возвращает суммарную длину пути (сумма длин всех линейных сегментов);
add_line(self, line) - добавление нового линейного сегмента (объекта класса LineTo) в конец маршрута.

Пояснение:
суммарный маршрут - это сумма длин всех линейных сегментов, а длина каждого линейного сегмента определяется
как евклидовое расстояние по формуле:
L = sqrt((x1-x0)^2 + (y1-y0)^2)
где x0, y0 - предыдущая точка маршрута; x1, y1 - текущая точка маршрута.

Пример использования классов (эти строчки в программе писать не нужно):
p = PathLines(LineTo(10, 20), LineTo(10, 30))
p.add_line(LineTo(20, -10))
dist = p.get_length()
                  
P.S. В программе требуется объявить только классы. На экран ничего выводить не нужно. 
"""

from math import sqrt

class LineTo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, value):
        self.__y = value


class PathLines:

    def __init__(self, *lines):
        self.start_coords = LineTo(0, 0)
        self.lines = [*lines]

    def get_path(self):
        return self.lines
    
    def add_line(self, line):
        self.__is_valid_line(line)
        self.lines.append(line)

    @classmethod
    def __is_valid_line(cls, line):
        if not type(line) == cls:
            return TypeError
        
    def get_length(self):
        res_length = 0

        count_lines = len(self.lines)
        if count_lines:
            start_coords = self.start_coords
            for line in range(count_lines):
                end_coords = self.lines[line]
                length = sqrt((end_coords.x - start_coords.x)**2 + (end_coords.y - start_coords.y)**2)
                res_length += length
                start_coords = end_coords

        return res_length
    

p = PathLines(LineTo(10, 20), LineTo(10, 30))
p.add_line(LineTo(20, -10))
dist = p.get_length()

print(dist)