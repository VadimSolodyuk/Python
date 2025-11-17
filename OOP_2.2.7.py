"""
"""


class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, value):
        if not self.__check_coord_value(value):
            # if self.__x:
            #     return
            self.__x = 0
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, value):
        if not self.__check_coord_value(value):
            # if self.__y:
            #     return
            self.__y = 0
        else:
            self.__y = value

    @classmethod
    def __check_coord_value(cls, value):
        if not ((type(value) == int or type(value) == float)
                and cls.MIN_COORD <= value <= cls.MAX_COORD):
            return False
        else:
            return True
        
    @staticmethod
    def norm2(vector):
        return vector.x**2 + vector.y**2
    

r1 = RadiusVector2D()
print(r1.x, r1.y)
r2 = RadiusVector2D(1, -101)
print(r2.x, r2.y)
r2.x = '5'
print(r2.x, r2.y)
print(r2.__dict__)