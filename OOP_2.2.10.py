"""Подвиг 10 (на закрепление). Вы создаете телефонную записную книжку.
Она определяется классом PhoneBook. Объекты этого класса создаются командой:
p = PhoneBook()
                  
А сам класс должен иметь следующий набор методов:
add_phone(phone) - добавление нового номера телефона (в список);
remove_phone(indx) - удаление номера телефона по индексу списка;
get_phone_list() - получение списка из объектов всех телефонных номеров.

Каждый номер телефона должен быть представлен классом PhoneNumber. Объекты этого класса должны создаваться командой:
note = PhoneNumber(number, fio)
где number - номер телефона (число) в формате XXXXXXXXXXX (одиннадцати цифр, X - цифра); fio - Ф.И.О. владельца номера (строка).

В каждом объекте класса PhoneNumber должны формироваться локальные атрибуты:
number - номер телефона (число);
fio - ФИО владельца номера телефона.

Необходимо объявить два класса PhoneBook и PhoneNumber в соответствии с заданием.

Пример использования классов (эти строчки в программе писать не нужно):
p = PhoneBook()
p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
p.add_phone(PhoneNumber(21345678901, "Панда"))
phones = p.get_phone_list()
                  
P.S. В программе требуется объявить только классы. На экран ничего выводить не нужно. 
"""


class PhoneBook:
    def __init__(self):
        self.phone_numbers = []

    def add_phone(self, phone):
        self.__is_valid_phone(phone)
        self.phone_numbers.append(phone)

    @staticmethod
    def __is_valid_phone(phone):
        if type(phone) != PhoneNumber:
            raise TypeError    

    def remove_phone(self, index):
        self.phone_numbers.pop(index)

    def get_phone_list(self):
        return self.phone_numbers
    

class PhoneNumber:
    LENGTH_NUMBER = 11

    def __init__(self, number, fio):
        self.number = number
        self.fio = fio

    @property
    def number(self):
        return self.__number
    
    @number.setter
    def number(self, number):
        self.__is_valid_number(number)
        self.__number = number

    @classmethod
    def __is_valid_number(cls, number):
        if not (len(str(number)) != cls.LENGTH_NUMBER or str(number).isdigit()):
            raise ValueError
        
    @property
    def fio(self):
        return self.__fio
    
    @fio.setter
    def fio(self, fio):
        self.__is_valid_fio(fio)
        self.__fio = fio

    @staticmethod
    def __is_valid_fio(fio):
        if not type(fio) == str:
            raise ValueError




p = PhoneBook()
p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
p.add_phone(PhoneNumber(21345678901, "Панда"))
phones = p.get_phone_list()