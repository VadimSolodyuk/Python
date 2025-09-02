'''Большой подвиг 10. Объявите два класса: 

Cell - для представления клетки игрового поля;
GamePole - для управления игровым полем, размером N x N клеток.

С помощью класса Cell предполагается создавать отдельные клетки командой:

c1 = Cell(around_mines, mine)
Здесь around_mines - число мин вокруг данной клетки поля; mine - булева величина (True/False), означающая наличие мины в текущей клетке. При этом, в каждом объекте класса Cell должны создаваться локальные свойства:

around_mines - число мин вокруг клетки (начальное значение 0);
mine - наличие/отсутствие мины в текущей клетке (True/False);
fl_open - открыта/закрыта клетка - булево значение (True/False). Изначально все клетки закрыты (False).

С помощью класса GamePole должна быть возможность создавать квадратное игровое поле с числом клеток N x N:

pole_game = GamePole(N, M)
Здесь N - размер поля; M - общее число мин на поле. При этом, каждая клетка представляется объектом класса Cell и все объекты хранятся в двумерном списке N x N элементов - локальном свойстве pole объекта класса GamePole. 

В классе GamePole должны быть также реализованы следующие методы:

init() - инициализация поля с новой расстановкой M мин (случайным образом по игровому полю, разумеется каждая мина должна находиться в отдельной клетке).
show() - отображение поля в консоли в виде таблицы чисел открытых клеток (если клетка не открыта, то отображается символ #; мина отображается символом *; между клетками при отображении ставить пробел).

При создании экземпляра класса GamePole в его инициализаторе следует вызывать метод init() для первоначальной инициализации игрового поля.

В классе GamePole могут быть и другие вспомогательные методы.

Создайте экземпляр pole_game класса GamePole с размером поля N = 10 и числом мин M = 12. 

P.S. На экран в программе ничего выводить не нужно.
'''

from random import randint


from random import randint


class Cell:
    def __init__(self, row, column, around_mines=0, fl_mine=False):
        self.coords = (row, column)
        self.around_mines = around_mines
        self.mine = fl_mine
        self.fl_open = False
        
    
class GamePole:
    DRAW_CLOSED_CELL = '#'
    DRAW_MINE_CELL = '*'
    
    def __init__(self, N, M):
        self.pole_size = N
        self.total_mines = M
        self.init()

    def init(self):
        self.pole = [[Cell(i, j) for j in range(self.pole_size)] 
                                 for i in range(self.pole_size)]
                
        self.__init_pole_for_show()
        self.__place_mines()
    
    def __init_pole_for_show(self):
        self.pole_for_show = [[self.DRAW_CLOSED_CELL
                              for _ in range(self.pole_size)]
                                for _ in range(self.pole_size)]
    
    # Случайная расстановка по полю total_mines мин
    def __place_mines(self):
        mines = 0
        while mines < self.total_mines:
            mine_coords = (randint(0, self.pole_size - 1) for _ in range(2))
            cell = self.__get_cell(mine_coords)
            if cell.mine:
                continue
            cell.mine = True
            self.__update_cells_around_mine(cell.coords)
            # self.click_cell(cell)  # For testing
            mines += 1
                
    # Updating cells around the mine  
    def __update_cells_around_mine(self, coords_mine):
        i, j = coords_mine 
        for row in self.pole[max(0, i - 1):min(i + 2, self.pole_size)]:
            for cell in row[max(0, j - 1):min(j + 2, self.pole_size)]:
                if cell.mine:
                    continue
                cell.around_mines += 1
                # self.click_cell(cell)  # For testing
                        
    def show(self):
        for row in self.pole_for_show:
            print(*row)
            
    def click_cell(self, cell):
        if not cell.fl_open:
            cell.fl_open = True
        self.__update_pole_for_show(cell)
        
    def __get_cell(self, cell_coords):
        i, j = cell_coords
        return self.pole[i][j]
        
    def click_all_cells(self):
        for row in self.pole:
            for cell in row:
                self.click_cell(cell)

    def __update_pole_for_show(self, cell):
        i, j = cell.coords
        if cell.mine:
            self.pole_for_show[i][j] = self.DRAW_MINE_CELL
        else:
            self.pole_for_show[i][j] = str(cell.around_mines)
            
            
pole_game = GamePole(10, 12)   
                    

pole_game.show()