import pygame
from Graphics import Graphics
from Move import Move
from GameState import GameState
from Enemy import Enemy


def main():
    # Setup
    pygame.init()
    clock = pygame.time.Clock()
    current_players_turn = True

    game_state = GameState()
    game_state.addPeices(4, 4, 2, True)
    game_state.addPeices(0, 5, -2, False)
    state = game_state.getState()
    enemy = Enemy()

    game_graphics = Graphics(state)

    selected_tile = None

    crashed = False
    while not crashed:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                tile_clicked_on = game_graphics.tileClickingOn(x, y)
                if selected_tile:
                    selected_tile.reset_tile_colour()
                if tile_clicked_on:
                    if current_players_turn:
                        if tile_clicked_on.isPlayer():
                            selected_tile = tile_clicked_on
                            tile_clicked_on.select()
                        elif selected_tile:
                            if tile_clicked_on.isEmpty():
                                game_state.move(
                                    selected_tile, tile_clicked_on, True)
                                current_players_turn = False
                                game_graphics.updateGraphics(state)
                                selected_tile = None
                                # game_state.printState()
                                game_state.processMove(
                                    enemy.makeMove(game_state))
                                # for e in game_state.getEnemyPeices():
                                #     print(e.i, e.j)
                                current_players_turn = True
                else:
                    selected_tile = None

        state = game_state.getState()
        game_graphics.updateGraphics(state)

        clock.tick(60)

    pygame.quit()
    quit()


if __name__ == "__main__":
    main()
