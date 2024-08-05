# b_text.py
"""
Title: Text Class
Author: Marco Ou
Date Created: April 15th 2024
"""

import pygame
from c_colors import Color


class Text:
    """
    Creates a text object to be placed on a Screen
    """

    def __init__(self, text):
        self.__text = text
        self.__color = (255, 255, 255)  # White
        self.__font_family = "Arial"
        self.__font_size = 36
        self.__font = pygame.font.SysFont("Arial", 36)
        self.__surface = self.__font.render(self.__text, True, self.__color)
        self.__x = 0
        self.__y = 0
        self.__position = (self.__x, self.__y)
        self.__speed = 5
        self.__dirX = 1  # default is going to the left
        self.__dirY = 1

    # modifier methods
    def marqueeX(self, MAX_WIDTH):
        """
        move the text from left to right and then wrap around to the other side
        :param: MAX_WIDTH
        :return: None
        """
        if self.__x >= MAX_WIDTH:
            self.__x = -self.__surface.get_width()
        else:
            self.__x += self.__speed
        self.__x += self.__speed
        self.__position = (self.__x, self.__y)

    def marqueeY(self, MAX_HEIGHT):
        """
        move text from top to bottom and then wrap around to the other side
        :param MAX_HEIGHT: int
        :return: None
        """
        if self.__y >= MAX_HEIGHT:
            self.__x = -self.__surface.get_height()
        else:
            self.__y += self.__speed
        self.__y += self.__speed
        self.__position = (self.__x, self.__y)

    def bounceX(self, MAX_WIDTH):
        """
        Text will bounce back and forth on the borders
        :param MAX_WIDTH: int
        :return: None
        """
        self.__x += self.__dirX * self.__speed
        if self.__x >= MAX_WIDTH - self.__surface.get_width():
            self.__dirX = -1
        elif self.__x <= 0:
            self.__x = 0
            self.__dirX = 1
        self.__position = (self.__x, self.__y)

    def bounceY(self, MAX_HEIGHT):
        """
        Text will bounce back and forth on the borders
        :param MAX_HEIGHT: int
        :return: None
        """
        self.__y += self.__dirY * self.__speed
        if self.__y >= MAX_HEIGHT - self.__surface.get_height():
            self.__dirY = -1
        elif self.__y <= 0:
            self.__y = 0
            self.__dirY = 1
        self.__position = (self.__x, self.__y)

    def setPosition(self, x, y):
        self.__x = x
        self.__y = y
        self.__position = (self.__x, self.__y)

    def setTextColor(self, color):
        """
        updates the color of the text
        :param color: tuple -> (red, green, blue)
        :return: None
        """
        self.__color = color
        self.__surface = self.__font.render(self.__text, True, self.__color)

    def setTextSize(self, size):
        """
        updates the size of the text
        :param size:
        :return:
        """
        self.__font_size = size
        self.__font = pygame.font.SysFont(self.__font_family, self.__font_size)
        self.__surface = self.__font.render(self.__text, True, self.__color)

    def updateText(self, text):
        self.__text = text
        self.__font.render(self.__text, True, self.__color)

    # accessor methods

    def getSurface(self):
        return self.__surface

    def getPosition(self):
        return self.__position

    def getWidth(self):
        return self.__surface.get_width()

    def getHeight(self):
        return self.__surface.get_height()


if __name__ == "__main__":
    from a_template import Window

    pygame.init()

    WINDOW = Window("Hello World 2", 800, 600, 30)
    TEXT1 = Text("Hello World")
    TEXT1.setTextSize(72)
    TEXT1.setPosition(WINDOW.getVirtualWidth() // 2 - TEXT1.getWidth() // 2,
                      WINDOW.getVirtualHeight() // 2 - TEXT1.getHeight() // 2)
    TEXT1.setTextColor(Color.getRandom())

    TEXT2 = Text("Computers")
    TEXT2.setPosition(0, 0)

    COUNT = 0

    while True:
        # INPUTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Processing

        # TEXT1.setTextColor(Color.getRandom())
        TEXT1.updateText(str(COUNT))
        # COUNT += 1
        TEXT2.bounceX(WINDOW.getVirtualWidth())
        TEXT2.bounceY(WINDOW.getVirtualHeight())

        # Outputs
        WINDOW.clearScreen()
        WINDOW.getScreen().blit(TEXT1.getSurface(), TEXT1.getPosition())
        WINDOW.getScreen().blit(TEXT2.getSurface(), TEXT2.getPosition())
        WINDOW.updateFrame()
