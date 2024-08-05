# Window.py
"""
Title: Pygame Template
Author: Marco Ou
Date Created: April 12th 2024
"""

import pygame
from c_colors import Color

class Window:
    """
    Create the window that will load for pygame
    :return: None
    """

    def __init__(self, title, width=800, height=600, fps=60):
        self.__title = title  # tet that appears in the title bar
        self.__width = width  # width of the window frame
        self.__height = height  # height of the window frame
        self.__dimension = (self.__width, self.__height)  # window dimensions
        self.__fps = fps  # frames per second
        self.__bg_color = Color.GREY  # dark gray background color
        self.__clock = pygame.time.Clock()  # clock object that tracks time
        self.__screen = pygame.display.set_mode(self.__dimension)  # base surface that all surfaces are overlaid on top
        self.__screen.fill(self.__bg_color)  # colors the screen surface
        pygame.display.set_caption(self.__title)  # sets the window caption with the title


    # Modifier Methods
    def getScreen(self) -> object:
        return self.__screen

    def updateFrame(self):
        """
        Update the Window object based on the fps
        :return:
        """
        self.__clock.tick(self.__fps)  # waits the appropriate amount of time based on FPS before finishing the loop
        pygame.display.flip()  # updates the computer screen with the new frame

    def clearScreen(self):
        """
        fill the screen with the background color
        :return:
        """
        self.__screen.fill(self.__bg_color)

    def getVirtualWidth(self):
        return self.__width

    def getVirtualHeight(self):
        return self.__height

