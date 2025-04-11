import pygame
from constants import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    black = "#000000"
    ONOFF = True
    while ONOFF:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(0000, None, 0) 
        pygame.display.flip()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")






if __name__ == "__main__":
    main()