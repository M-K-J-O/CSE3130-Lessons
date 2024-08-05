# box.py in f_inheritance folder

"""
Title: Box Class
Author: Marco Ou
Date Created: April 19th 2024
"""

from my_sprite import MySprite
import pygame
from random import randrange


class Box(MySprite):

    def __init__(self, width=1, height=1):
        MySprite.__init__(self, width=width, height=height)
        # super().__init__(width=width, height=height) This does the same thing as the line above
        self._surface = pygame.Surface(self._dimensions, pygame.SRCALPHA, 32)
        self._surface.fill(self._color)

    def setColor(self, new_color):
        MySprite.setColor(self, new_color)
        self._surface.fill(self._color)

    def setScale(self, scale_x, scale_y=None):
        """
        changes the scale of the image making it bigger or smaller
        :param scale_x: float
        :param scale_y: float
        :return: None
        """
        if scale_y is None:
            scale_y = scale_x

        self._surface = pygame.transform.scale(self._surface, (self.get_width() * scale_x, self.get_height() * scale_y))


if __name__ == "__main__":

    from Window import Window
    from Colors import Color

    pygame.init()

    WINDOW = Window("boxes inherited")

    BLUE_BOX = Box(50, 50)
    BLUE_BOX.setColor(Color.BLUE)
    BLUE_BOX.setPosition(0, 0)

    RED_BOX = Box(100, 100)
    RED_BOX.setColor(Color.RED)
    RED_BOX.setPosition(WINDOW.getVirtualWidth() // 2 - RED_BOX.get_width() // 2,
                        WINDOW.getVirtualHeight() // 2 - RED_BOX.get_height() // 2)
    RED_BOX.setSpeed(10)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        PRESSED_KEYS = pygame.key.get_pressed()

        BLUE_BOX.WASDMove(PRESSED_KEYS)
        if RED_BOX.isCollision(BLUE_BOX.get_width(), BLUE_BOX.get_height(), BLUE_BOX.getPosition()):
            print("HIT")

            while RED_BOX.isCollision(BLUE_BOX.get_width(), BLUE_BOX.get_height(), BLUE_BOX.getPosition()):
                RED_BOX.setPosition(randrange(WINDOW.getVirtualWidth() - RED_BOX.get_width()),
                                    randrange(WINDOW.getVirtualHeight() - RED_BOX.get_height()))
        else:
            BLUE_BOX.setColor(Color.BLUE)

        BLUE_BOX.stopAtEdge(WINDOW.getVirtualWidth(), WINDOW.getVirtualHeight())

        RED_BOX.bounceX(WINDOW.getVirtualWidth())
        RED_BOX.bounceY(WINDOW.getVirtualHeight())

        WINDOW.clearScreen()
        WINDOW.getScreen().blit(RED_BOX.getSurface(), RED_BOX.getPosition())
        WINDOW.getScreen().blit(BLUE_BOX.getSurface(), BLUE_BOX.getPosition())
        WINDOW.updateFrame()
