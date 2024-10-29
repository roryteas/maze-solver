from tkinter import Tk, BOTH, Canvas
from geometry import *
from maze import *
class Window:
    def __init__(self,width,height):
        self.root = Tk()
        self.root.title = 'The Title'
        self.canvas = Canvas(height = height, width = width)
        self.canvas.pack()
        self.window_running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)
    def redraw(self):
        self.root.update_idletasks()
        self.root.update()
    def wait_for_close(self):
        self.window_running = True
        while self.window_running == True:
            self.redraw()
    def close(self):
        self.window_running = False
    def draw_line(self, line, fill_colour):
        line.draw(self.canvas, fill_colour)



def main():
    win = Window(800, 600)
    maze = Maze(5,5,10,10,50,50,win)

    win.wait_for_close()
if __name__ == '__main__':
    main()
