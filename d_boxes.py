# d_boxes.py
"""
Title: Box class
Author: Marco Ou
Date Created: April 16th 2024
"""

import pygame
from c_colors import Color


class Box:
    def __init__(self, width=1, height=1, x=0, y=0, speed=10):
        self.__width = width
        self.__height = height
        self.__dimension = (self.__width, self.__height)
        self.__x = x
        self.__y = y
        self.__position = (self.__x, self.__y)
        self.__color = Color.WHITE
        self.__surface = pygame.Surface(self.__dimension, pygame.SRCALPHA, 32)
        self.__surface.fill(self.__color)
        self.__speed = speed

    # modifier methods

    def setColor(self, COLOR):
        self.__color = COLOR
        self.__surface.fill(self.__color)

    def WASDMove(self, pressed_keys):
        """
        move the box with WASD
        :param pressed_keys: list
        :return: None
        """
        if pressed_keys[pygame.K_d]:
            self.__x += self.__speed
        if pressed_keys[pygame.K_a]:
            self.__x -= self.__speed
        if pressed_keys[pygame.K_w]:
            self.__y -= self.__speed
        if pressed_keys[pygame.K_s]:
            self.__y += self.__speed
        self.__position = (self.__x, self.__y)

    def stopAtEdge(self, max_width, max_height, min_width=0, min_height=0):
        if self.__x > max_width - self.__surface.get_width():
            self.__x = max_width - self.__surface.get_width()
        if self.__x < min_width:
            self.__x = min_width

        if self.__y > max_height - self.__surface.get_height():
            self.__y = max_height - self.__surface.get_height()
        if self.__y < min_height:
            self.__y = min_height
        self.__surface = (self.__x, self.__y)

    def wrapEdge(self, max_width, max_height, min_width=0, min_height=0):
        """
        When an object moves offscreen wrap it to the other side
        :param max_width: int
        :param max_height: int
        :param min_width: int
        :param min_height: int
        :return: None
        """
        if self.__x > max_width:
            self.__x = min_width - self.__surface.get_width()
        elif self.__x < min_width - self.__surface.get_width():
            self.__x = max_width

        if self.__y > max_height:
            self.__y = min_height - self.__surface.get_height()
        elif self.__y < min_height - self.__surface.get_height():
            self.__y = max_height
        self.__position = (self.__x, self.__y)

    # accessor methods

    def getSurface(self):
        return self.__surface

    def getPosition(self):
        return self.__position


if __name__ == "__main__":
    from a_template import Window

    pygame.init()

    WINDOW = Window("Boxes")
    RED_BOX = Box(100, 200)
    RED_BOX.setColor(Color.RED)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        KEYS_PRESSED = pygame.key.get_pressed()  # gets the state of all keys
        RED_BOX.WASDMove(KEYS_PRESSED)
        #RED_BOX.stopAtEdge(WINDOW.getVirtualWidth(), WINDOW.getVirtualHeight())
        RED_BOX.wrapEdge(WINDOW.getVirtualWidth(), WINDOW.getVirtualHeight())

        WINDOW.clearScreen()
        WINDOW.getScreen().blit(RED_BOX.getSurface(), RED_BOX.getPosition())
        WINDOW.updateFrame()
