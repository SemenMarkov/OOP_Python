from typing import List
from random import randint

class Cell:
    def __init__(self, around_mines:int = 0, mine:bool = False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = True

class GamePole:
    def __init__(self, N:int, M:int):
        self.N = N
        self.M = M
        self.pole = [[Cell() for i in range(N)] for j in range(N)]
        self.init()
        
    def init(self):
        m = 0
        while m < self.M:
            i = randint(0, self.N - 1)
            j = randint(0, self.N - 1)
            if self.pole[i][j].mine:
                continue
            self.pole[i][j].mine = True
            m += 1
        
        indices = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
        for x in range(self.N):
            for y in range(self.N):
                if not self.pole[x][y].mine:
                    mines = sum((self.pole[x + i][y + j].mine for i, j in indices if 0 <= x + i < self.N and 0 <= y + j < self.N))
                    self.pole[x][y].around_mines = mines
    
    def show(self):
        for i in range(self.N):
            print(' '.join(map(lambda x: self._show_sign(x), self.pole[i])))
    
    def _show_sign(self, cell: Cell):
        if cell.fl_open == False:
            return '#'
        else:
            if cell.mine:
                return '*'
            else:
                return f'{cell.around_mines}'

gamepole = GamePole(10, 12)
gamepole.show()