#!/usr/bin/env python3

import random
from functools import reduce


class Minesweeper(object):
    """ Grid for minesweeper game.
    """
    def __init__(self, nrow=5, ncol=5, nmine=6):
        """ Initial a minesweeper grid with size being (nrow, ncol).
        """
        self.__grid = [[0]*ncol for _ in range(nrow)]
        self.placeMines(nrow, ncol, nmine)
        self.getCounts(nrow, ncol)
        self.__gridview = [['H']*ncol for _ in range(nrow)]
        self.active = True
        self.win = False

    def placeMines(self, nrow, ncol, nmine):
        """ Randomly place the mines on the grid.
        """
        mine_position = set([(random.randint(0,nrow-1), random.randint(0,ncol-1)) for j in range(nmine)])  #range(nrow+ncol)
        for pos in mine_position:
            self.__grid[pos[0]][pos[1]] = '*'
                   

    def getCounts(self, nrow, ncol):
        """ Get the counts for each non-mine cell on the grid.
        """
        for i,row in enumerate(self.__grid):
            for j,cell in enumerate(row):
                if cell != '*':
                    neighbor_index = [[k,l] for k in range(nrow) for l in range(ncol) if abs(k-i)<2 and abs(l-j)<2 and abs(k-i)+abs(l-j)>0]
                    for [n1,n2] in neighbor_index:
                        self.__grid[i][j] += int(self.__grid[n1][n2]=='*')
                    
    def __str__(self):
        """ Make print() function to display the grid.
        """
        return reduce(str.__add__, list("{0:s}\n".format(' '.join(map(str, row))) for row in self.__gridview))

    def explore(self, row, col):
        """ Player explore the grid on (row, col) cell.
        """
        nrow = len(self.__grid)
        ncol = len(self.__grid[0])
        self.__gridview[row][col] = self.__grid[row][col]
        if self.__grid[row][col] == '*': # hit mines, game over
            self.active = False
        elif self.__grid[row][col] == 0: # hit blank, show ripple effect
            ripple(self.__gridview, row, col, nrow, ncol, self.__grid)
        if sum(self.__gridview, []).count('H') == sum(self.__grid, []).count('*'):
            self.win = True
            self.active = False
        

def ripple(display_grid, row, col, nrow, ncol, actual_grid):
    """ When hitting blank, ripple effect appears.
        grid is the grid from player view, actual_grid is the solution grid.
    """
    neighbor_index = [[k,l] for k in range(nrow) for l in range(ncol) if abs(k-row)<2 and abs(l-col)<2 and abs(k-row)+abs(l-col)>0]
    for [n1,n2] in neighbor_index:
        if (actual_grid[n1][n2] != '*') & (display_grid[n1][n2] == 'H'):
            display_grid[n1][n2] = actual_grid[n1][n2]
            if actual_grid[n1][n2] == 0:
                ripple(display_grid, n1, n2, nrow, ncol, actual_grid)
        
            

def main():
    print("Let us play Minesweeper game!")
    while True:
        level = int(input("Choose difficuties (0 - easy; 1 - medium; 2 - hard):"))
        grid_size = [(5,5), (10,15), (20,30)]
        num_mine = [6,12,20]
        m1 = Minesweeper(grid_size[level][0], grid_size[level][1], num_mine[level])
        print(m1)
        while m1.active == True:
            pos_str = str(input("Choose the position you want to explore:"))
            row = int(pos_str.strip().split(',')[0].strip())
            col = int(pos_str.strip().split(',')[1].strip())
            m1.explore(row-1,col-1)
            print(m1)
            print('---------------------------------------------------------------------\n')
        if m1.win:
            print("Congratulations! You win!")
        else:
            print("Oops, you hit the mine! Game over...")
        if (input("Play again (y or n)?").lower() == 'n'):
            print()
            break

if __name__ == "__main__":
    main()

