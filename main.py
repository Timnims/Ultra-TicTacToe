from fltk import *
import socket
import pickle

class TicTacToe(Fl_Window):
    def __init__(self, x, y, w, h, label="Ultimate TicTacToe"):
        Fl_Window.__init__(self, x, y, w, h, label)
        self.begin()



    

if __name__ == "__main__":
    window = TicTacToe(100, 100, 1200, 900)
    window.end()
    window.show()
    Fl.run()