# Maze Solver: My fifth(?) guided project from boot.dev

from classes import *

win = Window(800, 600)
# No more lines. Time for squares.
first_cell = Cell(0, 0, 50, 50, win)
first_cell.draw()

beeg_cell = Cell(75, 10, 175, 110, win)
beeg_cell.draw()

# Drawing a few cells without some walls wish me luck yippeeeeeeee
cell_no_left = Cell(200, 10, 250, 260, win)
cell_no_left.remove_walls("left")
cell_no_left.draw()

cell_no_right = Cell(300, 10, 350, 30, win)
cell_no_right.remove_walls("right")
cell_no_right.draw()

cell_but_parallel_lines = Cell(50, 300, 100, 350, win)
cell_but_parallel_lines.remove_walls("top", "bottom")
cell_but_parallel_lines.draw()

deadass_just_one_line = Cell(50, 400, 100, 450, win)
deadass_just_one_line.remove_walls("left", "right", "bottom")
deadass_just_one_line.draw()

# This one should raise an exception due to a malformed remove_walls() function
#bad_boy = Cell(75, 500, 125, 550, win)
#bad_boy.remove_walls("yes")
#bad_boy.draw()
# It worked
win.wait_for_close()