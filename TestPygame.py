import pygame

SIZE = 1.2
HEIGHT = int(SIZE*800)
WIDTH = int(SIZE*600)
white = [255, 255, 255]


def main():
    pygame.init()

    game_display = pygame.display.set_mode((HEIGHT, WIDTH))
    pygame.display.set_caption('TBC')

    game_display.fill(white)

    clock = pygame.time.Clock()
    crashed = False

    while not crashed:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

            print(event)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()


if __name__ == "__main__":
    main()
