import unittest

from maze import *




class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
                len(m1._cells),
                num_cols,)
        self.assertEqual(
                len(m1._cells[0]),
                num_rows,)
    
    # def test_maze_no_cells(self):
    #     num_cols = 0
    #     num_rows = 0
    #     m1= Maze(0,0,0,0,10,10)


    def test_start_and_end(self):
        num_cols = 5
        num_rows = 5
        x1 = 0
        y1 = 0
        cell_width = 5
        cell_height = 5
        maze = Maze(x1, y1, num_rows, num_cols, cell_width, cell_height)
        first_cell = maze._cells[0][0]
        last_cell = maze._cells[-1][-1]

        self.assertEqual(first_cell.has_top_wall, False)
        self.assertEqual(last_cell.has_bottom_wall, False)
if __name__ == "__main__:":
    unittest.main()
