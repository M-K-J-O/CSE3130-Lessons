# image_sprite.py in f_inheritance folder
"""
Title: Image sprites
Author: Marco Ou
Date-Created: April 22nd 2024
"""

import pygame
from my_sprite import MySprite


class ImageSprite(MySprite):

    def __init__(self, image_file_location):
        MySprite.__init__(self)
        self.__file_location = image_file_location
        self._surface = pygame.image.load(self.__file_location).convert_alpha()
        self.__image_dir_x = False  # True is looking to the right

    def setScale(self, scale_x, scale_y=None):
        """
        changes the scale of the image making it bigger or smaller
        :param scale_x: float
        :param scale_y: float
        :return: None
        """
        if scale_y is None:
            scale_y = scale_x

        self._surface = pygame.transform.scale(self._surface, (self.get_width()*scale_x, self.get_height()*scale_y))

    def WASDMove(self, pressed_keys):
        # Polymorphism example of modifying the WASDMove() method
        MySprite.WASDMove(self, pressed_keys)
        if pressed_keys[pygame.K_d] and self.__image_dir_x:
            # if d key is pressed and image is looking to the left
            self._surface = pygame.transform.flip(self._surface, True, False)
            self.__image_dir_x = False  # image is now looking right
        if pressed_keys[pygame.K_a] and not self.__image_dir_x:
            # if a key is pressed and image is looking to the right
            self._surface = pygame.transform.flip(self._surface, True, False)
            self.__image_dir_x = True  # image is now looking left

    def setImageDirection(self, boole):
        self.__image_dir_x = boole


if __name__ == "__main__":
    from Window import Window
    from random import randrange
    from Colors import Color
    from text import Text
    from box import Box

    pygame.init()

    SCORE = 0
    SPEED = 10
    SIZE = 1

    WINDOW = Window("Image Sprite")
    BG_IMAGE = ImageSprite("media/grass (1).png")
    BG_IMAGE.setScale(1.6)
    BUNNY = ImageSprite("media/bunny (1).png")
    BUNNY.setScale(0.5)
    EGG_1 = ImageSprite("media/egg1 (1).png")
    EGG_1.setScale(0.5)
    EGG_1.setPosition(randrange(WINDOW.getVirtualWidth()-EGG_1.get_width()), randrange(WINDOW.getVirtualHeight()-EGG_1.get_height()))
    EGG_2 = ImageSprite("media/egg2 (1).png")
    EGG_2.setScale(0.5)
    EGG_2.setPosition(randrange(WINDOW.getVirtualWidth()-EGG_1.get_width()), randrange(WINDOW.getVirtualHeight()-EGG_1.get_height()))
    TEXT_1 = Text("Egg Hunt")
    TEXT_1.setPosition(WINDOW.getVirtualWidth()//2-TEXT_1.get_width()//2, 10)
    TEXT_SCORE = Text(f"Eggs Obtained: {SCORE}")
    TEXT_SCORE.setPosition(WINDOW.getVirtualWidth()*0.64, 10)
    GREY_BOX = Box(WINDOW.getVirtualWidth(), 10*2 + TEXT_1.get_height())
    GREY_BOX.setColor(Color.GREY)

    while True:
        # INPUTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # PROCESSING
        PRESSED_KEYS = pygame.key.get_pressed()
        if BUNNY.isCollision(EGG_1.get_width(), EGG_1.get_height(), EGG_1.getPosition()):
            if BUNNY.get_width() < 196:
                BUNNY.setScale(1.005)
            TEXT_SCORE = Text(f"Eggs Obtained: {SCORE}")
            TEXT_SCORE.setPosition(WINDOW.getVirtualWidth() * 0.64, 10)
            EGG_1.setPosition(randrange(WINDOW.getVirtualWidth()-EGG_1.get_width()), randrange(WINDOW.getVirtualHeight()-EGG_1.get_height()))
        elif BUNNY.isCollision(EGG_2.get_width(), EGG_2.get_height(), EGG_2.getPosition()):
            SCORE += 1
            SPEED += 0.25**(SCORE*0.025)
            BUNNY.setSpeed(SPEED)
            TEXT_SCORE = Text(f"Eggs Obtained: {SCORE}")
            TEXT_SCORE.setPosition(WINDOW.getVirtualWidth() * 0.64, 10)
            EGG_2.setPosition(randrange(WINDOW.getVirtualWidth()-EGG_1.get_width()), randrange(WINDOW.getVirtualHeight()-EGG_1.get_height()))


        # OUTPUTS
        BUNNY.WASDMove(PRESSED_KEYS)
        BUNNY.stopAtEdge(WINDOW.getVirtualWidth(), WINDOW.getVirtualHeight(), 0, GREY_BOX.get_height())
        EGG_1.stopAtEdge(WINDOW.getVirtualWidth(), WINDOW.getVirtualHeight(), 0, GREY_BOX.get_height())
        EGG_2.stopAtEdge(WINDOW.getVirtualWidth(), WINDOW.getVirtualHeight(), 0, GREY_BOX.get_height())

        WINDOW.clearScreen()

        WINDOW.getScreen().blit(BG_IMAGE.getSurface(), BG_IMAGE.getPosition())
        WINDOW.getScreen().blit(BUNNY.getSurface(), BUNNY.getPosition())
        WINDOW.getScreen().blit(EGG_1.getSurface(), EGG_1.getPosition())
        WINDOW.getScreen().blit(EGG_2.getSurface(), EGG_2.getPosition())
        WINDOW.getScreen().blit(GREY_BOX.getSurface(), GREY_BOX.getPosition())
        WINDOW.getScreen().blit(TEXT_1.getSurface(), TEXT_1.getPosition())
        WINDOW.getScreen().blit(TEXT_SCORE.getSurface(), TEXT_SCORE.getPosition())
        WINDOW.updateFrame()
