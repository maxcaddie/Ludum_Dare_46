import pygame


class Graphics:
    SIZE = 1.2
    HEIGHT = int(SIZE*800)
    WIDTH = int(SIZE*600)
    BACKGROUND_COLOUR = [255, 255, 255]

    def __init__(self):
        self.game_display = pygame.display.set_mode((self.HEIGHT, self.WIDTH))
        pygame.display.set_caption('TBC')

    def updateGraphics(self):
        self.game_display.fill(self.BACKGROUND_COLOUR)
        pygame.display.update()
