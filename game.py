import os

import pygame

from src.base import Move, Direction
from src.battle import Battle

WIDTH, HEIGHT = 600, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Robots Battle")

WHITE = (255, 255, 255)
FPS = 60
BASEDIR = os.path.abspath('.')

ROBOT_IMAGE = pygame.image.load(
    os.path.join(BASEDIR, 'static', 'robot.png')
)


def draw_window(battle):
    WIN.fill(WHITE)
    WIN.blit(
        ROBOT_IMAGE,
        (
            battle.robot_red.position[1] * 100,
            battle.robot_red.position[0] * 100
        )
    )
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    battle = Battle()
    battle.start()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    battle.turn(battle.robot_red, Direction.NORTH)
                    battle.move(battle.robot_red, Move.UP)
                    print(battle.robot_red.facing)

                elif event.key == pygame.K_DOWN:
                    battle.turn(battle.robot_red, Direction.SOUTH)
                    battle.move(battle.robot_red, Move.DOWN)
                    print(battle.robot_red.facing)

                elif event.key == pygame.K_LEFT:
                    battle.turn(battle.robot_red, Direction.WEST)
                    battle.move(battle.robot_red, Move.LEFT)
                    print(battle.robot_red.facing)

                elif event.key == pygame.K_RIGHT:
                    battle.turn(battle.robot_red, Direction.EAST)
                    battle.move(battle.robot_red, Move.RIGHT)
                    print(battle.robot_red.facing)

        draw_window(battle)

    pygame.quit()


if __name__ == '__main__':
    main()
