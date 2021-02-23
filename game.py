import os

import pygame

from src.base import Move
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
    print(battle.arena.board)
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    battle.move(robot=battle.robot_red, move=Move.DOWN)
                    print(battle.arena.board)
                    print(battle.robot_red.position)


        draw_window(battle)

    pygame.quit()


if __name__ == '__main__':
    main()
