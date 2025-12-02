"""Подвиг 8. 
"""


class StringValue:
    def __init__(self, min_length=3, max_length=100):
        self.__min_length = min_length
        self.__max_length = max_length

    def __set_name__(self, owner, name):
        self.name = '__' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)
    
    def __set__(self, instance, value):
        if self.__validate(value):
            setattr(instance, self.name, value)

    def __validate(self, string):
        return (type(string) == str 
                and self.__min_length <= len(string) <= self.__max_length)


class PriceValue:
    def __init__(self, max_value):
        self.__max_value = max_value

    def __set_name__(self, owner, name):
        self.name = '__' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)
    
    def __set__(self, instance, value):
        if self.__validate(value):
            setattr(instance, self.name, value)

    def __validate(self, value):
        return (isinstance(value, (int, float)) 
                and 0 <= value <= self.__max_value)
    

class Product:
    price = PriceValue(10000)
    name = StringValue()

    def __init__(self, name, price):
        self.name = name
        self.price = price


class SuperShop:
    name = StringValue()

    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        if self.__is_product(product):
            self.goods.append(product)

    def remove_product(self, product):
        if self.__is_product(product) and product in self.goods:
            self.goods.remove(product)

    @staticmethod
    def __is_product(value):
        return type(value) is Product
    


shop = SuperShop("У Балакирева")
shop.add_product(Product("Курс по Python", 0))
shop.add_product(Product("Курс по Python ООП", 2000))
for p in shop.goods:
    print(f"{p.name}: {p.price}")
