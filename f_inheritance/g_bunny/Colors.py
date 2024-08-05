# Colors.py
"""
title: Color Class
author: Marco Ou
date created: April 15th 2024
"""

from random import randrange


class Color:
    WHITE = (255, 255, 255)
    GREY = (50, 50, 50)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    ORANGE = (255, 145, 0)
    PURPLE = (175, 25, 255)

    @ staticmethod
    def getRandom():
        return randrange(256), randrange(256), randrange(256)
