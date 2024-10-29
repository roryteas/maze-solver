class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
    
    def draw(self, canvas, fill_colour):
        canvas.create_line(
                self.point1.x,
                self.point1.y,
                self.point2.x,
                self.point2.y,
                fill=fill_colour,
                width = 2)
class Cell:
    def __init__(self,  x1, y1, x2, y2, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._window = window

    def draw(self):
        top_left = Point(self._x1,self._y1)
        top_right = Point(self._x2, self._y1)
        bottom_right = Point(self._x2, self._y2)
        bottom_left = Point(self._x1, self._y2) 

        top = Line(top_left, top_right)
        bottom = Line(bottom_left, bottom_right)
        left = Line(top_left, bottom_left)
        right = Line(top_right, bottom_right)
        if self.has_top_wall:
            self._window.draw_line(top, 'black')
        if self.has_bottom_wall:
            self._window.draw_line(bottom, 'black')
        if self.has_left_wall:
            self._window.draw_line(left, 'black')
        if self.has_right_wall:
            self._window.draw_line(right, 'black')
    
    def draw_move(self, to_cell, undo=False):
        p1x = self._x2 - (self._x2- self._x1)/2
        p1y = self._y2 - (self._y2- self._y1)/2
        p2x = to_cell._x2 - (to_cell._x2- to_cell._x1)/2
        p2y = to_cell._y2 - (to_cell._y2- to_cell._y1)/2
        point1 = Point(p1x,p1y)
        point2 = Point(p2x,p2y)
        line = Line(point1, point2)
        colour = 'red'
        if undo:
            colour = 'gray'
        self._window.draw_line(line, colour)
