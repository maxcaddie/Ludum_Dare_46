import pygame

SIZE = 1.2
HEIGHT = int(SIZE*600)
WIDTH = int(SIZE*800)
TILE_SIZE = min(WIDTH, HEIGHT)/13
TILE_GAP = int(TILE_SIZE/3)
PLAYER_COLOUR = [0, 0, 100]
ENEMY_COLOUR = [0, 100, 0]
EMPTY_COLOUR = [50, 50, 50]
SELECTED_COLOUR_OFFSET = [40, 40, 40]


class Graphics:

    BACKGROUND_COLOUR = [255, 255, 255]
    tiles = pygame.sprite.Group()

    def __init__(self, state):
        self.game_display = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('This game is broken don\'t play')
        for row in state:
            for tile in state:
                self.tiles.add(tile)

    def updateGraphics(self, state):
        self.game_display.fill(self.BACKGROUND_COLOUR)
        for tile in self.tiles:
            tile.update()
            tile.update_tile()
        self.tiles.draw(self.game_display)
        pygame.display.update()

    def tileClickingOn(self, x, y):
        for tile in self.tiles:
            if tile.rect.collidepoint((x, y)):
                return tile
