# Unit tests for the maze classes

import unittest
from classes import *

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_2(self):
        num_cols = 4
        num_rows = 9
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    
    def test_maze_entrance_exit_breaking(self):
        num_cols = 5
        num_rows = 5
        entrance_walls = 4
        exit_walls = 4
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._break_entrance_and_exit()
        if m1._cells[0][0].has_left_wall == False or m1._cells[0][0].has_top_wall == False:
            entrance_walls -= 1
        if m1._cells[-1][-1].has_right_wall == False or m1._cells[-1][-1].has_bottom_wall == False:
            exit_walls -= 1
        self.assertEqual(entrance_walls, 3)
        self.assertEqual(exit_walls, 3)

if __name__ == "__main__":
    unittest.main()