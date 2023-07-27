from fltk import *
from PIL import Image
import io
import socket
import pickle

class TicTacToe(Fl_Window):
    def __init__(self, x, y, w, h, label="Ultimate TicTacToe"):
        Fl_Window.__init__(self, x, y, w, h, label)
        self.begin()

        self.x_image = Fl_PNG_Image('x.png')
        self.o_image = Fl_PNG_Image('o.png')

        self.gray_border = Fl_Box(40, 40, 810, 810)
        self.gray_border.color(FL_DARK_CYAN)
        self.gray_border.box(FL_BORDER_BOX)

        self.round = 0
        self.square_list=[]
        self.box_size = 250

        self.player_turn = 'x'

        for x in range(3):
            for y in range(3):

                button = Fl_Button(60+(x*(10 + self.box_size)), 60+(y*(10 + self.box_size)), self.box_size, self.box_size)
                button.color(FL_BLACK)
                button.box(FL_BORDER_BOX)
                button.callback(self.turn)

        
    def turn(self, widget):
        self.round += 1
        if widget.image() == None:
            if self.player_turn == 'x':
                widget.image(self.x_image.copy(self.box_size, self.box_size))
                widget.redraw()
                self.player_turn = 'o'
            else:
                widget.image(self.o_image.copy(self.box_size, self.box_size))
                widget.redraw()
                self.player_turn = 'x'
        else:
            return
        
        self.win()
    
    def win(self):
        if self.round == 9:
            print('Draw! Gameover')
        
        
        return
    

if __name__ == "__main__":
    window = TicTacToe(100, 100, 900, 900)
    window.end()
    window.show()
    Fl.run()