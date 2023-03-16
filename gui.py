import pygame
from global_var import *

class Gui():
    def __init__(self, screen):
        self.cp437 = pygame.font.Font(".\\font\PerfectDOSVGA437.ttf", 16) # font
        self.screen = screen

    def show_debug_info(self, clock=None, player=None):
        debug_str = "Debug Info :"

        if clock != None : # show fps
            debug_str += "\n" + str(int(clock.get_fps())) + " FPS"
        if player != None :# Player coordinates
            debug_str += "\nx : " + str(player.rect.x) + "\ny : " + str(player.rect.y)
        if debug_str == "Debug Info :":
            debug_str += "\nNo parameters given"
        
        debug_disp = self.cp437.render(debug_str, False, COLOR[3])
        self.screen.blit(debug_disp, (scr_width -TILE_SIZE*16, 0))