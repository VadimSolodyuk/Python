"""Объявите дескриптор данных FloatValue, который бы устанавливал
и возвращал вещественные значения. При записи вещественного числа должна
выполняться проверка на вещественный тип данных. Если проверка
не проходит, то генерировать исключение командой:
raise TypeError("Присваивать можно только вещественный тип данных.")
                  
Объявите класс Cell, в котором создается объект value дескриптора
FloatValue. А объекты класса Cell должны создаваться командой:
cell = Cell(начальное значение ячейки)
                  
Объявите класс TableSheet, с помощью которого создается таблица из N
строк и M столбцов следующим образом:
table = TableSheet(N, M)
                  
Каждая ячейка этой таблицы должна быть представлена объектом класса Cell,
работать с вещественными числами через объект value
(начальное значение должно быть 0.0).

В каждом объекте класса TableSheet должен формироваться локальный атрибут:
cells - список (вложенный) размером N x M, содержащий ячейки таблицы 
(объекты класса Cell).

Создайте объект table класса TableSheet с размером таблицы N = 5, M = 3.
Запишите в эту таблицу числа от 1.0 до 15.0 (по порядку, построчно).

P.S. На экран в программе выводить ничего не нужно.
"""


class FloatValue:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instant, owner):
        return getattr(instant, self.name)
    
    def __set__(self, instant, value):
        self.is_valid(value)
        setattr(instant, self.name, value)

    @staticmethod
    def is_valid(value):
        if type(value) != float:
            raise TypeError('Присваивать можно только вещественный тип данных.')


class Cell:
    value = FloatValue()
   
    def __init__(self, value):
        self.value = value


class TableSheet:
    def __init__(self, N, M):
        self.cells = [[Cell(0.0) for _ in range(M)] for _ in range(N)]



table = TableSheet(5, 3)

value = 1.0
for row in table.cells:
    for column in row:
        column.value = value
        value += 1

        print(column.value)