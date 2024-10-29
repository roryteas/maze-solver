import time
import random
from geometry import *

class Maze():
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            window= None,
            seed= None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._window = window
        self._cells: [[Cell]] = [] 
        self._create_cells()
        if seed != None:
            random.seed(seed)
        self._break_walls_r(0, 0)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            if j > 0 and not self._cells[i][j-1].visited:
                to_visit.append((i,j-1))
            if i > 0 and not self._cells[i-1][j].visited:
                to_visit.append((i-1,j))
            if j < self._num_rows-1  and not self._cells[i][j+1].visited:
                to_visit.append((i,j+1))
            if i < self._num_cols-1 and not self._cells[i+1][j].visited:
                to_visit.append((i+1,j))
            if len(to_visit)==0:
                self._draw_cell(i, j)
                return
            direction = random.randrange(0,len(to_visit))
            direction_index = to_visit[direction]
            if direction_index[1] == j-1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j-1].has_bottom_wall = False

            if direction_index[1] == j+1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j+1].has_top_wall = False
            
            if direction_index[0] == i-1:
                self._cells[i][j].has_left_wall = False
                self._cells[i-1][j].has_right_wall = False

            if direction_index[0] == i+1:
                self._cells[i][j].has_right_wall = False
                self._cells[i+1][j].has_left_wall = False
            self._break_walls_r(*direction_index)
            

    def _create_cells(self):
        x = self._x1
        y = self._y1
        for i in range(self._num_cols):
            cell_col = []
            for j in range(self._num_rows):
                x1 = j * self._cell_size_x + x
                y1 = i * self._cell_size_y + y 
                x2 = (j+1) * self._cell_size_x + x
                y2 = (i+1) * self._cell_size_y + y 
                cell = Cell(x1, y1, x2, y2, self._window)
                cell_col.append(cell)
            self._cells.append(cell_col)
        self._cells[0][0].has_top_wall = False
        self._cells[-1][-1].has_bottom_wall = False
        if not self._window:
            return
        self._draw_cell(0, 0)
        self._draw_cell(-1,-1)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)
    def _draw_cell(self, i, j):
        cell = self._cells[i][j]
        cell.draw()
        self._animate()
    def _animate(self):
        self._window.redraw()
        time.sleep(0.02)


