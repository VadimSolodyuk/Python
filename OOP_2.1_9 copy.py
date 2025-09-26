"""Большой подвиг 9. Необходимо реализовать связный список (не список языка Python и не хранить объекты в списке Python),
когда объекты класса ObjList связаны с соседними через приватные свойства __next и __prev.

Для этого объявите класс LinkedList, который будет представлять связный список в целом и иметь набор следующих методов:
add_obj(self, obj) - добавление нового объекта obj класса ObjList в конец связного списка;
remove_obj(self) - удаление последнего объекта из связного списка;
get_data(self) - получение списка из строк локального свойства __data всех объектов связного списка.

И в каждом объекте этого класса должны создаваться локальные публичные атрибуты:
head - ссылка на первый объект связного списка (если список пустой, то head = None);
tail - ссылка на последний объект связного списка (если список пустой, то tail = None).

Объекты класса ObjList должны иметь следующий набор приватных локальных свойств:
__next - ссылка на следующий объект связного списка (если следующего объекта нет, то __next = None);
__prev - ссылка на предыдущий объект связного списка (если предыдущего объекта нет, то __prev = None);
__data - строка с данными.

Также в классе ObjList должны быть реализованы следующие сеттеры и геттеры:
set_next(self, obj) - изменение приватного свойства __next на значение obj;
set_prev(self, obj) - изменение приватного свойства __prev на значение obj;
get_next(self) - получение значения приватного свойства __next;
get_prev(self) - получение значения приватного свойства __prev;
set_data(self, data) - изменение приватного свойства __data на значение data;
get_data(self) - получение значения приватного свойства __data.

Создавать объекты класса ObjList предполагается командой:
ob = ObjList("данные 1")
А использовать класс LinkedList следующим образом (пример, эти строчки писать в программе не нужно):
lst = LinkedList()
lst.add_obj(ObjList("данные 1"))
lst.add_obj(ObjList("данные 2"))
lst.add_obj(ObjList("данные 3"))
res = lst.get_data()    # ['данные 1', 'данные 2', 'данные 3']

Объявите в программе классы LinkedList и ObjList в соответствии с заданием.
P.S. На экран ничего выводить не нужно.
"""

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Добавление нового объекта obj класса ObjList в конец связного списка
    def add_obj(self, obj):
        if self.__is_empty_List():
            self.head = self.tail = obj
        else:
            self.tail.set_next(obj)
            obj.set_prev = self.tail
            self.tail = obj

    def __is_empty_List(self):
        return self.head == None
        
    # Удаление последнего объекта из связного списка;
    def remove_obj(self):
        if not self.__is_empty_List():
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.tail = self.tail.get_prev()
                self.tail.set_next(None)

    # Получение списка из строк локального свойства __data всех объектов связного списка
    def get_data(self):
        res_data = []
        if not self.__is_empty_List():
            obj = self.head
            while obj:
                res_data.append(obj.get_data())
                obj = obj.get_next()

        return res_data 

class ObjList:
    def __init__(self, data):
        self.set_data(data)
        self.__next = None
        self.__prev = None

# Изменение приватного свойства __next на значение obj
def set_next(self, obj):
    if self.__check_object(obj):
        self.__next = obj

# Изменение приватного свойства __prev на значение obj
def set_prev(self, obj):
    if self.__check_object(obj):
        self.__prev = obj

@staticmethod
def __check_object(obj):
    if not isinstance(obj, (ObjList, None)):
        raise ValueError('Type "obj" should be "ObjList" or "None"')
    else:
        True

# Получение значения приватного свойства __next
def get_next(self):
    return self.__next

# Получение значения приватного свойства __prev
def get_prev(self):
    return self.__prev

# Изменение приватного свойства __data на значение data
def set_data(self, data):
    if self.__check_data(data):
        self.__data = data

@classmethod
def __check_data(cls, data):
    if not isinstance(data, str):
        raise ValueError('Type "data" should be "str"')
    else:
        True

# Получение значения приватного свойства __data
def get_data(self):
    return self.__data


lst = LinkedList()
lst.add_obj(ObjList("данные 1"))
lst.add_obj(ObjList("данные 2"))
lst.add_obj(ObjList("данные 3"))
res = lst.get_data()    # ['данные 1', 'данные 2', 'данные 3']