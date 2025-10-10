"""Объявите класс EmailValidator для проверки корректности email-адреса. 
Необходимо запретить создание объектов этого класса: при создании 
экземпляров должно
возвращаться значение None, например:
em = EmailValidator() # None

В самом классе реализовать следующие методы класса (@classmethod):

get_random_email(cls) - для генерации случайного email-адреса по формату:
xxxxxxx...xxx@gmail.com, где x - любой допустимый символ в email
(латинский буквы, цифры, символ подчеркивания и точка);

check_email(cls, email) - возвращает True, если email записан верно
и False - в противном случае.
Корректность строки email определяется по следующим критериям:
+ допустимые символы: латинский алфавит, цифры, символы подчеркивания,
точки и собачка @ (одна);
+ длина email до символа @ не должна превышать 100 (сто включительно);
+ длина email после символа @ не должна быть больше 50 (включительно);
+ после символа @ обязательно должна идти хотя бы одна точка; 
+ не должно быть двух точек подряд.

Также в классе нужно реализовать приватный статический метод класса:

is_email_str(email) - для проверки типа переменной email, если строка,
то возвращается значение True, иначе - False.
Метод is_email_str() следует использовать в методе check_email() перед
проверкой корректности email.
Если параметр email не является строкой, то check_email() возвращает
False.

Пример использования класса EmailValidator (эти строчки в программе
писать не нужно):
res = EmailValidator.check_email("sc_lib@list.ru") # True
res = EmailValidator.check_email("sc_lib@list_ru") # False
P.S. В программе требуется объявить только класс. На экран ничего
выводить не нужно.
"""

from string import ascii_letters, digits
from random import randint, choices

class EmailValidator:
    CORRECT_CHARS = ascii_letters + digits + '_.'
    separator = '@' 
    min_length_mailbox_name = 8
    max_length_mailbox_name = 100
    length_domain = 50
    
    domains = {'gmail':"gmail.com"}
    
    def __new__(cls):
        return None
    
    @classmethod
    def get_random_email(cls):
        name_corporation = 'gmail'
        return (cls.__get_random_mailbox_name() 
                + cls.separator
                + cls.__get_domain(name_corporation))
    
    @classmethod
    def __get_random_mailbox_name(cls):
        length_mailbox_name = randint(cls.min_length_mailbox_name,
                                        cls.max_length_mailbox_name)
        mailbox_name = ''
        while (mailbox_name == ''
               or '..' in mailbox_name 
               or mailbox_name.startswith('.')):
            mailbox_name = ''.join(choices(cls.CORRECT_CHARS, k=length_mailbox_name))
        # while len(mailbox_name) != length_mailbox_name:
        #     if mailbox_name == '':
        #         mailbox_name = (mailbox_name
        #                         + choice(cls.CORRECT_CHARS.removesuffix('_.')))
        #     else:
        #         prev_char = mailbox_name[len(mailbox_name) - 1] 
        #         if prev_char == '.':
        #             mailbox_name = (mailbox_name 
        #                             + choice(cls.CORRECT_CHARS.removesuffix('.')))
        #         else:
        #             mailbox_name = (mailbox_name 
        #                             + choice(cls.CORRECT_CHARS))
        return mailbox_name
    
    @classmethod
    def __get_domain(cls, name_corporatiom):
        if (type(name_corporatiom) != str
            or name_corporatiom not in cls.domains):
            return ValueError
        return cls.domains[name_corporatiom]
    
    @classmethod
    def check_email(cls, email):
        if not cls.__is_email_str(email):
            return False
        elif (not set(email) < set(cls.CORRECT_CHARS + cls.separator)
              or email.count(cls.separator) != 1
              or email.find('..') != -1):
            return False

        return cls.__check_email(email)       

    @classmethod
    def __check_email(cls, email):
        mailbox_name, domain = email.split(cls.separator)
        if not (cls.__check_mailbox_name(mailbox_name)
                and cls.__check_domain(domain)):
            return False
        
        return True

    @classmethod
    def __check_mailbox_name(cls, mailbox_name):
        return len(mailbox_name) <= cls.max_length_mailbox_name
    
    @classmethod
    def __check_domain(cls, domain):
        if (len(domain) > cls.length_domain
            or domain.count('.') < 1):
            return False
        
        return True
    
    @staticmethod
    def __is_email_str(email):
        return isinstance(email, str)
        
    
email = EmailValidator.get_random_email()
print(email)  
print(EmailValidator.check_email(email))
