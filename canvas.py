#!/usr/bin/python2

class Canvas(object):

    class Space(object):

        def __init__(self, width, height):
            self._MAX_X = 1000
            self._MAX_Y = 1000
            self._frame_wd = width
            self._frame_ht = height
            self._origin_x = 0
            self._origin_y = 0
            self._mat = [[None] * self._MAX_X for i in range(self._MAX_Y)]
        
        def _
    

    def __init__(self, frame_width, frame_height):
        self.frame = Frame(frame_width, frame_height)
        self.space = Space(1000, 1000)
        self.width = width
        self.height = height
        self.frame = [['|'] + [' '] * width + ['|'] for row in range(height)]
        self.frame.insert(0, ['-'] * (width + 2))
        self.frame.append(['-'] * (width + 2))
        self.space = [] 


    def draw_frame(self):
        for row in self.frame: 
            print "".join(row)


    def _putc(self, x, y, c):
        if type(c) is not str or len(c) > 1:
            return
        if x > self.width:
            x = self.width
        elif x < 1:
            x = 1
        elif y > self.height:
            y = self.height
        elif y < 1:
            y = 1
        self.frame[y][x] = str(c)


    def print_int(self, x, y, val):
        if type(val) is not int:
            return 
        for c in str(val):
            self._putc(x, y, c)
            x += 1

    def print_str(self, x, y, val):
        if type(val) is not str:
            return
        for c in val:
            self._putc(x, y, c) 
            x += 1
        

if __name__ == "__main__":
    
    canvas = Canvas(80, 50)
    canvas._putc(40, 25, 'X')
    canvas.print_int(1, 1, 1234)
    canvas.print_str(4, 4, "hello")
    canvas.draw_frame()

