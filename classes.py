# This document will hold all the classes that main.py will use

from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title = "Maze Solver" # TODO: Bugged. Figure out how to fix later
        self.__canvas = Canvas(self.__root, width=width, height=height)
        self.__canvas.pack()
        self.__is_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)
    
    def wait_for_close(self):
        self.__is_running = True
        while self.__is_running == True:
            self.redraw()
    
    def close(self):
        self.__is_running = False

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.__point1 = point1
        self.__point2 = point2
    
    def draw(self, canvas, fill_color): # DO NOT CALL THIS FUNCTION DIRECTLY. Call the Window class's draw_line() function instead, with the line itself as the first argument.
        canvas.create_line(
            self.__point1.x, self.__point1.y, self.__point2.x, self.__point2.y, fill=fill_color, width=2
        )

class Cell:
    def __init__(self, x1, y1, x2, y2, win):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__win = win
    
    def remove_walls(self, *args): # CALL THIS BEFORE THE draw() FUNCTION IF YOU WANNA REMOVE WALLS
        for arg in args:
            match arg:
                case "left":
                    self.has_left_wall = False
                case "right":
                    self.has_right_wall = False
                case "top":
                    self.has_top_wall = False
                case "bottom":
                    self.has_bottom_wall = False
                case _:
                    raise Exception("invalid input. which wall are you removing?")
    
    def draw(self):
        if self.has_left_wall == True:
            left_wall = Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
            self.__win.draw_line(left_wall, "black")
        if self.has_top_wall == True:
            left_wall = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
            self.__win.draw_line(left_wall, "black")
        if self.has_right_wall == True:
            left_wall = Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2))
            self.__win.draw_line(left_wall, "black")
        if self.has_bottom_wall == True:
            left_wall = Line(Point(self.__x2, self.__y2), Point(self.__x1, self.__y2))
            self.__win.draw_line(left_wall, "black")