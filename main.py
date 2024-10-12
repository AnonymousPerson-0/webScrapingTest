import tkinter
import pygame
import sys
import math
import os
from settings.py import *

pygame.init()
pygame.display.init()
pygame.Mixer.init()
# if someone can find a w background track that'd be lit

def main():
    # i prefer pygame honestly.
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    # Tk(classname = 'Cost Lower Bound Estimation')
    # mainloop()
    run = True
    while run:
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.display.quit()
                pygame.quit()
                run = False
                break
            if (event.type == pygame.MOUSEBUTTONDOWN):
                # clicked.
                continue
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_RETURN):
                    continue
        '''for key, bool in zip(pygame.key.get_pressed()):
            if (key):
                #etc etc
                continue'''
    break

if (__name__ == "__main__"):
    # event based.
    main()
    sys.exit()
