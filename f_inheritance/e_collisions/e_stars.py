#e_stars.py
"""
Title: star field
Author: Marco Ou
Date: April 17th 2024
"""

if __name__ == "__main__":
    import pygame
    from a_template import Window
    from d_boxes import Box
    from random import randint
    pygame.init()

    WINDOW = Window("Stars")
    STARS = []

    for i in range(200):
        STAR_SIZE = randint(3, 6)

        STARS.append(Box(STAR_SIZE, STAR_SIZE, randint(0, WINDOW.getVirtualWidth()-STAR_SIZE), randint(0, WINDOW.getVirtualHeight()-STAR_SIZE), randint(9, 11)))

    while True:
        # INPUT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        KEYS_PRESSED = pygame.key.get_pressed()
        # Processing
        for star in STARS:
            star.WASDMove(KEYS_PRESSED)
            star.wrapEdge(WINDOW.getVirtualWidth(), WINDOW.getVirtualHeight())
        # OUTPUTS
        WINDOW.clearScreen()
        for star in STARS:
            WINDOW.getScreen().blit(star.getSurface(), star.getPosition())
        WINDOW.updateFrame()
