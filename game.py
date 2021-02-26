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

ATTACK_IMAGE = pygame.image.load(
    os.path.join(BASEDIR, 'static', 'attack.png')
)

DEACTIVATED_ROBOT_IMAGE = pygame.image.load(
    os.path.join(BASEDIR, 'static', 'deactivated_robot.png')
)


def draw_window(battle):
    WIN.fill(WHITE)

    red_robot_img = pygame.transform.rotate(
        ROBOT_IMAGE, battle.red_robot.facing.index(1) * (-90)
    )

    WIN.blit(
        red_robot_img,
        (
            battle.red_robot.position[1] * 100,
            battle.red_robot.position[0] * 100
        )
    )

    WIN.blit(
        ROBOT_IMAGE,
        (
            battle.blue_robot.position[1] * 100,
            battle.blue_robot.position[0] * 100
        )
    )

    for robot in battle.deactivated_robots:
        if robot.hp:
            WIN.blit(
                DEACTIVATED_ROBOT_IMAGE,
                (
                    robot.position[1] * 100,
                    robot.position[0] * 100
                )
            )
        else:
            battle.die(robot)

    pygame.display.update()


def main():
    img = ROBOT_IMAGE
    rect = img.get_rect()
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
                    battle.turn(battle.red_robot, Direction.NORTH)
                    battle.move(battle.red_robot, Move.UP)

                elif event.key == pygame.K_DOWN:
                    battle.turn(battle.red_robot, Direction.SOUTH)
                    battle.move(battle.red_robot, Move.DOWN)

                elif event.key == pygame.K_LEFT:
                    battle.turn(battle.red_robot, Direction.WEST)
                    battle.move(battle.red_robot, Move.LEFT)

                elif event.key == pygame.K_RIGHT:
                    battle.turn(battle.red_robot, Direction.EAST)
                    battle.move(battle.red_robot, Move.RIGHT)

                elif event.key == pygame.K_w:
                    battle.turn(battle.red_robot, Direction.NORTH)

                elif event.key == pygame.K_s:
                    battle.turn(battle.red_robot, Direction.SOUTH)

                elif event.key == pygame.K_a:
                    battle.turn(battle.red_robot, Direction.WEST)

                elif event.key == pygame.K_d:
                    battle.turn(battle.red_robot, Direction.EAST)

                elif event.key == pygame.K_SPACE:

                    battle.attack(battle.red_robot)
                    print(battle.arena.board)

        draw_window(battle)

    pygame.quit()


if __name__ == '__main__':
    main()
