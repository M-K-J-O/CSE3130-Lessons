# box.py in f_inheritance folder

"""
Title: Box Class
Author: Marco Ou
Date Created: April 19th 2024
"""

from my_sprite import MySprite
import pygame


class Box(MySprite):

    def __init__(self, width=1, height=1):
        MySprite.__init__(self, width=width, height=height)
        # super().__init__(width=width, height=height) This does the same thing as the line above
        self._surface = pygame.Surface(self._dimensions, pygame.SRCALPHA, 32)
        self._surface.fill(self._color)

    def setColor(self, new_color):
        MySprite.setColor(self, new_color)
        self._surface.fill(self._color)


if __name__ == "__main__":

    from Window import Window
    from Colors import Color

    pygame.init()

    WINDOW = Window("boxes inherited")

    BLUE_BOX = Box(50, 50)
    BLUE_BOX.setColor(Color.BLUE)
    BLUE_BOX.setPosition(0, 0)
    BLUE_BOX.setSpeed(50)

    RED_BOX = Box(100, 100)
    RED_BOX.setColor(Color.RED)
    RED_BOX.setPosition(WINDOW.getVirtualWidth() // 2 - RED_BOX.get_width()//2, WINDOW.getVirtualHeight() // 2 - RED_BOX.get_height()//2)
    RED_BOX.setSpeed(10)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        PRESSED_KEYS = pygame.key.get_pressed()

        RED_BOX.WASDMove(PRESSED_KEYS)
        RED_BOX.stopAtEdge(WINDOW.getVirtualWidth(), WINDOW.getVirtualHeight())

        BLUE_BOX.bounceX(WINDOW.getVirtualWidth())
        BLUE_BOX.bounceY(WINDOW.getVirtualHeight())

        WINDOW.clearScreen()
        WINDOW.getScreen().blit(RED_BOX.getSurface(), RED_BOX.getPosition())
        WINDOW.getScreen().blit(BLUE_BOX.getSurface(), BLUE_BOX.getPosition())
        WINDOW.updateFrame()
