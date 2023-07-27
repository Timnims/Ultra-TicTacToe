from fltk import *
import socket
import pickle

class TicTacToe(Fl_Window):
    def __init__(self, x, y, w, h, label="Ultimate TicTacToe"):
        Fl_Window.__init__(self, x, y, w, h, label)
        self.begin()

        self.gray_border = Fl_Box(40, 40, 920, 820)
        self.gray_border.color(FL_DARK_CYAN)
        self.gray_border.box(FL_BORDER_BOX)

        self.square_list=[]

        for box_x in range(3):
            for box_y in range(3):
                for x in range(3):
                    for y in range(3):
        



    

if __name__ == "__main__":
    window = TicTacToe(100, 100, 1000, 900)
    window.end()
    window.show()
    Fl.run()