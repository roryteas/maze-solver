import time
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
            window):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._window = window
        self._cells = []
        self._create_cells()

    
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

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)
    def _draw_cell(self, i, j):
        cell = self._cells[i][j]
        cell.draw()
        self._animate()
    def _animate(self):
        self._window.redraw()
        time.sleep(0.035)


