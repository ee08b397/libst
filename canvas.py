#!/usr/bin/python2

class Canvas(object):
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.frame = [['|'] + [' '] * width + ['|'] for row in range(height)]
        self.frame.insert(0, ['-'] * (width + 2))
        self.frame.append(['-'] * (width + 2))


    def draw_frame(self):
        for row in self.frame: 
            print "".join(row)


    def _put_sym(self, x, y, sym):
        if x > self.width:
            x = self.width
        elif x < 1:
            x = 1
        elif y > self.height:
            y = self.height
        elif y < 1:
            y = 1
        self.frame[y][x] = sym


    def print_int(self, x, y, val):
        if type(val) is not int:
            return 
        

if __name__ == "__main__":
    
    canvas = Canvas(80, 50)
    canvas._put_sym(40, 25, 'X')
    canvas.draw_frame()

