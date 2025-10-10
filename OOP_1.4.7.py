'''Подвиг 7. Имеется следующий класс для считывания информации из входного потока:

import sys


class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res
Которым, затем, можно воспользоваться следующим образом:

sr = StreamReader()
data, result = sr.readlines()
Необходимо перед классом StreamReader объявить еще один класс StreamData с методом:

def create(self, fields, lst_values): ...

который бы на входе получал кортеж FIELDS из названий локальных атрибутов (передается в атрибут fields) и список строк lst_in
(передается в атрибут lst_values) и формировал бы в объекте класса StreamData локальные свойства с именами полей из fields
и соответствующими значениями из lst_values.

Если создание локальных свойств проходит успешно, то метод create() возвращает True, иначе - False. Если число полей и число строк 
не совпадает, то метод create() возвращает False и локальные атрибуты создавать не нужно.

P.S. В программе нужно дополнительно объявить только класс StreamData. Больше ничего делать не нужно.
'''


import sys

10
class StreamData:
    def create(self, tp_fields, lst_value):
        if len(tp_fields) != len(lst_value):
            return False
        for i, field in enumerate(tp_fields):
            setattr(self, field, lst_value[i])
        else:
            return True


class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res



sr = StreamReader()
data, result = sr.readlines()