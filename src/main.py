import pygame
from Graphics import Graphics
from Move import Move


def main():
    pygame.init()

    game_graphics = Graphics()
    clock = pygame.time.Clock()
    current_players_turn = True

    crashed = False
    while not crashed:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

            print(event)

        game_graphics.updateGraphics()

        clock.tick(60)

    pygame.quit()
    quit()


def updateBoardGraphics():
    board_state = getState()
    updateGraphics(board_state)


if __name__ == "__main__":
    main()
