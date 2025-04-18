# Maze Solver: My fifth(?) guided project from boot.dev

from tkinter import Tk, BOTH, Canvas

# Remember to move these classes to another file soon otherwise the main file is gonna be BLOATED AS HELL

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title = "Maze Solver"
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
    
    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.__point1.x, self.__point1.y, self.__point2.x, self.__point2.y, fill=fill_color, width=2
        )


win = Window(800, 600)
# Drawing some lines :3c
win.draw_line(Line(Point(70, 50), Point(70, 150)), "black")

win.draw_line(Line(Point(370, 50), Point(370, 150)), "black")
win.draw_line(Line(Point(470, 50), Point(470, 150)), "black")

win.draw_line(Line(Point(70, 450), Point(70, 550)), "black")
win.draw_line(Line(Point(170, 450), Point(170, 550)), "black")

win.draw_line(Line(Point(370, 450), Point(370, 550)), "black")
win.draw_line(Line(Point(470, 550), Point(570, 550)), "black")

win.wait_for_close()