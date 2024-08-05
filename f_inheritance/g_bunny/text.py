# text.py in f_inheritance folder

"""
Title:
Author: Marco Ou
Date: April 18th 2024
"""

from my_sprite import MySprite
import pygame


class Text(MySprite):

    def __init__(self, text, font_family="Arial", font_size=36, x=0, y=0):
        MySprite.__init__(self, x=x, y=y)
        self.__text = text
        self.__font_family = font_family
        self.__font_size = font_size
        self.__font = pygame.font.SysFont(self.__font_family, self.__font_size)
        self._surface = self.__font.render(self.__text, True, self._color)


if __name__ == "__main__":
    from Window import Window

    pygame.init()
    WINDOW = Window("Inheritance")
    TEXT = Text("Inheritance Example")
    TEXT.setPosition(100, 150)

    TEXT.setSpeed(32)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        PRESSED_KEYS = pygame.key.get_pressed()

        TEXT.WASDMove(PRESSED_KEYS)

        WINDOW.clearScreen()
        WINDOW.getScreen().blit(TEXT.getSurface(), TEXT.getPosition())
        WINDOW.updateFrame()




