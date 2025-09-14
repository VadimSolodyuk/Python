# inp = '''1 0 0 0 0
# 0 0 1 0 0
# 0 0 0 0 0
# 0 1 0 1 0
# 0 0 0 0 0'''

# import sys

# # здесь объявляйте функцию
# def verify(matrix):
#     def is_isolate(i, j, matr2D=matrix) :

#     for i, row in enumerate(matrix) :
#         for j, x  in enumerate(row) :
#             if x == 0 or (x == 1 and is_isolate(i, j)) :
#                 continue
#             else :
#                 return False
#     return True


# lines = inp.split(sep='\n') # lines = sys.stdin.readlines() # чтение строк из входного потока (переменную lines не менять)

# # здесь продолжайте программу по формированию двумерного списка lst2D
# lst2D = [[int(x) for x in row if x.isdigit()] for row in lines]
# print(lst2D)

# line_eng = 'house river tree car'
# line_rus = 'дом река дерево машина'


# def show_dict(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args)
#         dic = { x : res[1][i] for i, x in enumerate(res[0])}
#         return dic
#     return wrapper

# @show_dict
# def get_tuple(*args):
#     tp = tuple([w for w in line.split()] for line in args)
#     return tp


# d = get_tuple(line_eng, line_rus)
# print(*sorted(d.items()))


##########################################################
# from string import ascii_lowercase

# gen = (x + y for x in ascii_lowercase for y in ascii_lowercase)

# for x in range(50):
#     print(next(gen), end=' ')


# ##########################################################
# cities = ["Москва", "Ульяновск", "Самара", "Уфа", "Омск", "Тула"]

# gen = (cities[x] if x <= (len(cities) - 1) else cities[x % len(cities)] for x in range(1000000))

# for x in range(20):
#     print(next(gen), end=' ')


# ##########################################################
# a, b = 0, 10 #map(int, input().split())

# # gen = (x for x in )
# gen_res = (0.5 * pow(x / 100, 2) - 2.0 for x in range(100 * a, 100 * b + 1))

# for x in range(20):
#     print(round(next(gen_res), 2), end=' ')


# ##########################################################
# def gen_numbers():
#     number = 1
#     while True:
#         number += 1
#         for x in range(2, number + 1):
#             if (x != number) and (number % x == 0):
#                 break
#             elif number % x == 0:
#                 yield number


# gen = gen_numbers()
# for _ in range(20):
#     print(next(gen), end=' ')

# # ##########################################################
# # import sys

# in_ = '''зонт=1000
# палатка=10000
# спички=22
# котелок=543'''
# # # считывание списка из входного потока
# # lst_in = list(map(str.strip, sys.stdin.readlines()))
# lst_in = list(map(str.strip, in_.split(sep='\n')))


# # здесь продолжайте программу (используйте список lst_in)
# tuple_in = tuple(map(lambda line: tuple(line.split(sep='=')), lst_in))
# out_ = filter(lambda x: int(x[1]) >= 500 , tuple_in)

# for x in out_:
#     print(x[0], end=' ')
    
    
# ##########################################################
# import sys

# input_ = '''6 10 3 2 1 5
# 7 10 5 3 6'''

# # put your python code here
# tuple_in = tuple(map(str.strip, input_.split(sep='\n')))
# monets1 = set(map(int, tuple_in[0].split()))
# monets2 = set(map(int, tuple_in[1].split()))
# monets = sorted(list(monets1 & monets2))
# # monets.sort()
# print(monets)
# for x in filter(lambda y: y % 2 == 0, monets):
#     print(x, end=' ')

# ##########################################################
# def get_sort(d):
#     tp_pair_sorted = sorted(d.items())
#     list_value = [pair[1] for pair in tp_pair_sorted]
#     return list_value


# d = {'cat': 'кот', 'horse': 'лошадь', 'tree': 'дерево', 'dog': 'собака', 'book': 'книга'}
# print(get_sort(d))


##########################################################
# new_order = 'Имя;Зачет;Оценка;Номер'
# new_order = tuple(new_order.split(sep=';'))

# input_ = '''Номер;Имя;Оценка;Зачет
# 1;Портос;5;Да
# 2;Арамис;3;Да
# 3;Атос;4;Да
# 4;д'Артаньян;2;Нет
# 5;Балакирев;1;Нет'''

# lst_in = list(map(str.strip, input_.splitlines()))

# t_table = tuple(tuple(map(lambda x: int(x) if x.isdigit() else x, row.split(';'))) \
#     for row in lst_in)

# t_table = tuple(zip(*t_table))
# t_table = sorted(t_table, key=lambda tuple_: new_order.index(tuple_[0]))
# t_table = tuple(zip(*t_table))

# print(t_table)


''' OOP_1.7.10

class AppStore:
    def __init__(self):
        self.applications = {}
    
    # Добавление нового приложения app в магазин
    def add_application(self, app):
        self.applications[id(app)] = app
    
    # Удаление приложения app из магазина
    def remove_application(self, app):
        if self.__in_appStore(app):
            del self.applications[id(app)]
        
    # Блокировка приложения app (устанавливает локальное свойство blocked
    # объекта app в значение True)
    def block_application(self, app):
        if self.__in_appStore(app):
            self.applications[id(app)].blocked = True
    
    # Возвращает общее число приложений в магазине
    def total_apps(self):
        return len(self.applications)
    
    def __in_appStore(self, app):
        return id(app) in self.applications
    
    
class Application:
    def __init__(self, name):
        self.name = name
        self.blocked = False
        
        
store = AppStore()
app_youtube = Application("Youtube")
store.add_application(app_youtube)
store.remove_application(app_youtube)
'''

''' OOP_1.7.11

class Message:
    def __init__(self, text):
        self.text = text
        self.fl_like = False
        
        
class Viber:
    messages = {}
    
    # Добавление нового сообщения в список сообщений
    @classmethod
    def add_message(cls, message):
        cls.messages[id(message)] = message
    
    # Удаление сообщения из списка
    @classmethod
    def remove_message(cls, message):
        if cls.__in_viber(message):
            del cls.messages[id(message)]
    
    # Поставить/убрать лайк для сообщения msg (т.е. изменить атрибут fl_like
    # объекта msg: если лайка нет то он ставится, если уже есть, то убирается)
    @classmethod
    def set_like(cls, message):
        if cls.__in_viber(message):
            cls.messages[id(message)].fl_like = \
                not cls.messages[id(message)].fl_like
                
    # Отображение последних сообщений
    def show_last_message(number):
        pass
            
    # Возвращает общее число сообщений
    @classmethod
    def total_messages(cls):
        return len(cls.messages)
    
    @classmethod
    def __in_viber(cls, message):
        return id(message) in cls.messages 
'''


