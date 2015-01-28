#!/usr/bin/python2

import sys

class Canvas(object):

    class Space(object):

        def __init__(self, frame_width, frame_height, MAX_X=1000, MAX_Y=1000):
            self._MAX_X = MAX_X
            self._MAX_Y = MAX_Y
            self._wd = frame_width
            self._ht = frame_height
            self._x = 0
            self._y = 0
            self._mat = [[None] * self._MAX_X for i in range(self._MAX_Y)]


        def _shift(self, axis, s):
            lim = self._MAX_X if axis == "X" else self._MAX_Y
            if s > 0 and self._x + self._wd + s > lim:
                self._x = self._MAX_X - self._wd
            elif s < 0 and self._x + s < 0:
                self._x = 0
            else:
                self._x += s


        def _shift_y(self, s):
            if s > 0 and self._y + self._ht + s > self._MAX_Y:
                self._x = self._MAX_X - self._wd
            elif s < 0 and self._x + s < 0:
                self._x = 0
            else:
                self._x += s

        
        def _draw_frame(self): 
            sys.stdout.write("".join(["-"] * (self._wd + 2 )) + "\n")
            for row in self._mat[self._y:(self._y+self._ht)]: 
                line = map(lambda x : " " if x == None else x, row[self._x:(self._x+self._wd)])
                sys.stdout.write("|" + "".join(line) + "|\n")
            sys.stdout.write("".join(["-"] * (self._wd + 2 )) + "\n")


        def _putc(self, x, y, c):
            if type(c) is not str or len(c) > 1:
                return
            if x > self._MAX_X:
                x = self._MAX_X
            elif x < 0:
                x = 0
            elif y > self._MAX_Y:
                y = self._MAX_Y
            elif y < 0:
                y = 0
            self._mat[y][x] = str(c)
    

    def __init__(self, frame_width, frame_height):
        self.space = self.Space(frame_width, frame_height)


    def print_int(self, x, y, val):
        if type(val) is not int:
            return 
        for c in str(val):
            self.space._putc(x, y, c)
            x += 1


    def print_str(self, x, y, val):
        if type(val) is not str:
            return
        for c in val:
            self.space._putc(x, y, c) 
            x += 1

    
    def move_x(self, s):
        self.space._shift_x(s)


    def draw(self):
        self.space._draw_frame()
        

if __name__ == "__main__":
    
    canvas = Canvas(80, 50)
    canvas.print_int(0, 0, 1234)
    canvas.print_str(4, 4, "hello")
    canvas.move_x(2)
    canvas.draw()

