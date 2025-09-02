'''Подвиг 9. Вам необходимо реализовать односвязный список (не список 
языка Python, объекты в списке не хранить, а формировать связанную
структуру, показанную на рисунке) из объектов класса ListObject:

Для этого объявите в программе класс ListObject, объекты которого
создаются командой:
obj = ListObject(data)
                  
Каждый объект класса ListObject должен содержать локальные свойства:
next_obj - ссылка на следующий присоединенный объект (если следующего
объекта нет, то next_obj = None);
data - данные объекта в виде строки.

В самом классе ListObject должен быть объявлен метод:

link(self, obj) - для присоединения объекта obj такого же класса
к текущему объекту self (то есть, атрибут next_obj объекта self должен
ссылаться на obj).

Прочитайте список строк из входного потока командой:

lst_in = list(map(str.strip, sys.stdin.readlines()))
                 
Затем сформируйте односвязный список, в объектах которых (в атрибуте
data) хранятся строки из списка lst_in (первая строка в первом объекте,
вторая - во втором и  т.д.). На первый добавленный объект класса 
ListObject должна ссылаться переменная head_obj.

P.S. В программе что-либо выводить на экран не нужно.
'''


class ListObject:
    def __init__(self, data):
        self.next_obj = None
        self.data = data

    # Присоединения объекта obj такого же класса
    def link(self, obj):
        self.next_obj = obj


lst_in = ['var_' + str(x) for x in range(20)]

head_obj = ListObject(lst_in[0])

# Var 1
obj = head_obj
for x in range(1, len(lst_in)):
    new_obj = ListObject(lst_in[x])
    obj.link(new_obj)
    obj = new_obj
    

# Var 2
def insert(list_object, data):
    if list_object.next_obj is None:
        list_object.link(ListObject(data))
    else:
        insert(list_object.next_obj, data)
    
        
for i in range(1, len(lst_in)):
    insert(head_obj, lst_in[i])      