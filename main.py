# this allows us to use code from
# the open-source pygame library
# throught this file
import pygame
from constants import *

def starting():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

starting()

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        screen.fill(color="black")
        pygame.display.flip()

    main()
