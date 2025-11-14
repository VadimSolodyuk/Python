"""
"""


class RadiusVector2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @property
    def coord_x(self):
        return self.__x
    
    @coord_x.setter
    def coord_x(self, value):
        if self.__check_coords_value(value): # TODO
            self.__x = value