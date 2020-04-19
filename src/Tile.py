import pygame

from Graphics import TILE_SIZE, HEIGHT, WIDTH, TILE_GAP, PLAYER_COLOUR, ENEMY_COLOUR, EMPTY_COLOUR, SELECTED_COLOUR_OFFSET


class Tile(pygame.sprite.Sprite):
    def __init__(self, i, j):
        pygame.sprite.Sprite.__init__(self)
        self.i = i
        self.j = j
        self.stack_size = 0
        self.colour = EMPTY_COLOUR.copy()
        self.update_tile()

    def update_tile(self):
        self.image = pygame.Surface([TILE_SIZE, TILE_SIZE])
        self.image.fill(self.colour)
        self.rect = self.image.get_rect()

        x_offset = int((WIDTH/2)-(TILE_SIZE/2)) + \
            ((self.i-4)*(TILE_GAP+TILE_SIZE))
        y_offset = int((HEIGHT/2)-(TILE_SIZE/2)) + \
            ((self.j-4)*(TILE_GAP+TILE_SIZE))

        self.rect = self.rect.move(x_offset, y_offset)

    def reset_tile_colour(self):
        if self.stack_size > 0:
            self.colour = PLAYER_COLOUR.copy()
        elif self.stack_size < 0:
            self.colour = ENEMY_COLOUR.copy()
        else:
            self.colour = EMPTY_COLOUR.copy()
        self.update_tile()

    def select(self):
        for i in range(0, len(self.colour)):
            self.colour[i] = self.colour[i]+SELECTED_COLOUR_OFFSET[i]
        self.update_tile()

    def copy(self):
        temp_tile = Tile(self.i, self.j)
        temp_tile.stack_size = self.stack_size
        return temp_tile

    def isPlayer(self):
        return self.stack_size > 0

    def isEmpty(self):
        return self.stack_size == 0

    def isEnemy(self):
        return self.stack_size < 0
