import os
import time

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

ITEM_IMAGE = pygame.image.load(
    os.path.join(BASEDIR, 'static', 'item.png')
)


def render_items(battle):
    for item in battle.items:
        WIN.blit(
            ITEM_IMAGE,
            (
                item.position[1] * 100,
                item.position[0] * 100
            )
        )


def render_deactivated_robots(battle):
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


def render_activated_robot(robot):
    robot_img = pygame.transform.rotate(
        ROBOT_IMAGE, robot.facing.index(1) * (-90)
    )

    WIN.blit(
        robot_img,
        (
            robot.position[1] * 100,
            robot.position[0] * 100
        )
    )


def render_attack(battle):
    robot = battle.red_robot
    for field in battle.get_attack_fields(robot):
        WIN.blit(
            ATTACK_IMAGE,
            (
                field[1] * 100,
                field[0] * 100
            )
        )
        pygame.display.update()
    pygame.time.wait(250)


def draw_window(battle, attacks=False):
    WIN.fill(WHITE)

    render_activated_robot(battle.red_robot)
    render_activated_robot(battle.blue_robot)
    render_deactivated_robots(battle)
    render_items(battle)

    pygame.display.update()


def handle_movement(battle, key):
    if key == pygame.K_UP:
        battle.turn(battle.red_robot, Direction.NORTH)
        battle.move(battle.red_robot, Move.UP)

    elif key == pygame.K_DOWN:
        battle.turn(battle.red_robot, Direction.SOUTH)
        battle.move(battle.red_robot, Move.DOWN)

    elif key == pygame.K_LEFT:
        battle.turn(battle.red_robot, Direction.WEST)
        battle.move(battle.red_robot, Move.LEFT)

    elif key == pygame.K_RIGHT:
        battle.turn(battle.red_robot, Direction.EAST)
        battle.move(battle.red_robot, Move.RIGHT)


def handle_turning(battle, key):
    if key == pygame.K_w:
        battle.turn(battle.red_robot, Direction.NORTH)

    elif key == pygame.K_s:
        battle.turn(battle.red_robot, Direction.SOUTH)

    elif key == pygame.K_a:
        battle.turn(battle.red_robot, Direction.WEST)

    elif key == pygame.K_d:
        battle.turn(battle.red_robot, Direction.EAST)


def handle_attack(battle, key):
    if key == pygame.K_SPACE:
        battle.attack(battle.red_robot)
        render_attack(battle)


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
                handle_movement(battle, event.key)

                handle_turning(battle, event.key)

                handle_attack(battle, event.key)

        draw_window(battle)

    pygame.quit()


if __name__ == '__main__':
    main()
