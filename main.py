# Maze Solver: My fifth(?) guided project from boot.dev

from classes import *

win = Window(800, 600)
# Hope the maze actually works
maze = Maze(10, 10, 10, 10, 50, 50, win)
maze._break_entrance_and_exit()
maze._break_walls_r(0, 0)
maze._reset_cells_visited()
maze.solve()
win.wait_for_close()