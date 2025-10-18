"""Подвиг 6. Реализуйте односвязный список (не список Python,
не использовать список Python для хранения объектов), когда один объект
ссылается на следующий и так по цепочке до последнего:

Для этого объявите в программе два класса: 
StackObj - для описания объектов односвязного списка;
Stack - для управления односвязным списком.

Объекты класса StackObj предполагается создавать командой:
obj = StackObj(данные)

Здесь данные - это строка с некоторым содержимым. 
Каждый объект класса StackObj должен иметь следующие локальные
приватные атрибуты:
__data - ссылка на строку с данными, указанными при создании объекта;
__next - ссылка на следующий объект класса StackObj (при создании 
объекта принимает значение None).

Также в классе StackObj должны быть объявлены объекты-свойства:
next - для записи и считывания информации из локального приватного
свойства __next;
data - для записи и считывания информации из локального приватного 
свойства __data.

При записи необходимо реализовать проверку, что __next будет ссылаться
на объект класса StackObj или значение None. Если проверка не проходит, 
то __next остается без изменений.

Класс Stack предполагается использовать следующим образом:
st = Stack() # создание объекта односвязного списка
                  
В объектах класса Stack должен быть локальный публичный атрибут:
top - ссылка на первый добавленный объект односвязного списка 
(если список пуст, то top = None).

А в самом классе Stack следующие методы:
push(self, obj) - добавление объекта класса StackObj в конец 
односвязного списка;
pop(self) - извлечение последнего объекта с его удалением 
из односвязного списка;
get_data(self) - получение списка из объектов односвязного списка 
(список из строк локального атрибута __data каждого объекта в порядке 
их добавления, или пустой список, если объектов нет).

Пример использования классов Stack и StackObj (эти строчки в программе 
писать не нужно):

st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st.pop()
res = st.get_data()    # ['obj1', 'obj2']
                  
P.S. В программе требуется объявить только классы. На экран ничего 
выводить не нужно. 
"""


class StackObj():
    def __init__(self, data):
        self.data = data
        self.next = None
        
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data):
        if self.__check_data(data):
            self.__data = data
    
    @staticmethod
    def __check_data(data):
        if not isinstance(data, str):
            return False  # ValueError
        return True
        
    @property
    def next(self):
        return self.__next
    
    @next.setter
    def next(self, obj):
        if self.__check_obj(obj):
            self.__next = next
    
    @classmethod
    def __check_obj(cls, obj):
        if not isinstance(obj, (cls, None)):
            return False  # ValueError
        return True
        
        
class Stack:
    stack_item_type = (StackObj,)
    
    def __init__(self):
        self.top = None
        
    def push(self, obj):
        if self.__check_obj(obj):
            if not self.top:
                self.top = obj
            else:
                bottom_obj = self.__get_bottom_obj(self.top)
                bottom_obj.next = obj
                self.top = bottom_obj.next
            
    @classmethod
    def __check_obj(cls, obj):
        if type(obj) not in cls.stack_item_type:
            return ValueError
        return True
    
    @classmethod
    def __get_penult_obj(cls, top_obj):
        if top_obj.next and not top_obj.next.next:
            return top_obj
        cls.__get_penult_obj(top_obj.next)
        
    def pop(self):
        if self.top:
            bottom_obj = self.__get_bottom_obj(self.top)
            bottom_obj.next = obj
            self.top = bottom_obj.next
            
    