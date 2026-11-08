import pygame
from .display_handler  import Display_Handler
import sprite_constants

class Input_Handler():

    def __init__(self):
        self.display = Display_Handler()
        self.display.display(sprite_constants.BG_1) 