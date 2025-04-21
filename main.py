# Maze Solver: My fifth(?) guided project from boot.dev

from classes import *

win = Window(800, 600)
# Hope the maze actually works
maze = Maze(10, 10, 5, 5, 50, 50, win)
win.wait_for_close()