import pygame, sys, os
from game import Game

class Setting():
    def __init__(self):
        #self.show_debug = False
        pass

    def allow_print(self, show_debug:bool=None):
        """
        Allow python to print in the terminal during the execution : only use for debug.
        REMEMBER : Print something take a lot of performance.
        """
        if show_debug == None: show_debug = False
        else : show_debug = show_debug

        if show_debug == True:
            sys.stdout = sys.__stdout__
        else:
            # Disable print
            sys.stdout = open(os.devnull, 'w')

def main():
    setting = Setting()
    setting.allow_print(True)
    pygame.init()
    game = Game()
    game.run()
    
if __name__ == "__main__":
    main()