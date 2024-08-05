# my_sprite.py in f_inheritance folder

"""
Title: The my sprite abstract class
Author: Marco Ou
Date: April 18th 2024
"""

from Colors import Color
import pygame


class MySprite:
    """
    Abstract sprite class to build other sprites
    """

    def __init__(self, width=0, height=0, x=0, y=0, speed=10, color=Color.WHITE):
        self.__width = width
        self.__height = height
        self._dimensions = (self.__width, self.__height)
        self.__x = x
        self.__y = y
        self.__position = (self.__x, self.__y)
        self.__speed = speed
        self._color = color
        self._surface = pygame.Surface
        self.__dir_x = 1
        self.__dir_y = 1

    # Modifier Methods (setter methods)
    def bounceX(self, MAX_WIDTH):
        """
        Text will bounce back and forth on the borders
        :param MAX_WIDTH: int
        :return: None
        """
        self.__x += self.__dir_x * self.__speed
        if self.__x >= MAX_WIDTH - self._surface.get_width():
            self.__dir_x = -1
        elif self.__x <= 0:
            self.__x = 0
            self.__dir_x = 1
        self.__position = (self.__x, self.__y)

    def bounceY(self, MAX_HEIGHT):
        """
        Text will bounce back and forth on the borders
        :param MAX_HEIGHT: int
        :return: None
        """
        self.__y += self.__dir_y * self.__speed
        if self.__y >= MAX_HEIGHT - self._surface.get_height():
            self.__dir_y = -1
        elif self.__y <= 0:
            self.__y = 0
            self.__dir_y = 1
        self.__position = (self.__x, self.__y)

    def stopAtEdge(self, max_width, max_height, min_width=0, min_height=0):
        if self.__x > max_width - self._surface.get_width():
            self.__x = max_width - self._surface.get_width()
        if self.__x < min_width:
            self.__x = min_width

        if self.__y > max_height - self._surface.get_height():
            self.__y = max_height - self._surface.get_height()
        if self.__y < min_height:
            self.__y = min_height
        self.__updatePosition()

    def WASDMove(self, pressed_keys):
        if pressed_keys[pygame.K_d]:
            self.__x += self.__speed
        if pressed_keys[pygame.K_a]:
            self.__x -= self.__speed
        if pressed_keys[pygame.K_w]:
            self.__y -= self.__speed
        if pressed_keys[pygame.K_s]:
            self.__y += self.__speed
        self.__updatePosition()

    def marqueeX(self, max_x, min_x=0):
        self.__x += self.__speed
        if self.__x > max_x:
            self.__x = min_x - self._surface.get_width()
        self.__updatePosition()

    def setSpeed(self, new_speed):
        self.__speed = new_speed

    def setX(self, x):
        self.__x = x
        self.__updatePosition()

    def setY(self, y):
        self.__y = y
        self.__updatePosition()

    def setColor(self, new_color):
        """
        This only changes the variable, it does not change the surface
        :param new_color: tuple
        :return: None
        """
        self._color = new_color

    def setPosition(self, x, y):
        self.__x = x
        self.__y = y
        self.__updatePosition()

    def __updatePosition(self):
        self.__position = (self.__x, self.__y)

    # Accessor Methods (getter methods)
    # def getX(self):
        # return self.__x

    def getSurface(self):
        return self._surface

    def getPosition(self):
        return self.__position

    def get_width(self):
        return self._surface.get_width()

    def get_height(self):
        return self._surface.get_height()


