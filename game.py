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


class Game:

    def __init__(self):
        self.has_moved = False
        self.has_attacked = False
        self.battle = Battle()

    def render_items(self):
        for item in self.battle.items:
            WIN.blit(
                ITEM_IMAGE,
                (
                    item.position[1] * 100,
                    item.position[0] * 100
                )
            )

    def render_deactivated_robots(self):
        for robot in self.battle.deactivated_robots:
            if robot.hp > 0:
                WIN.blit(
                    DEACTIVATED_ROBOT_IMAGE,
                    (
                        robot.position[1] * 100,
                        robot.position[0] * 100
                    )
                )
            else:
                self.battle.destroy(robot)

    def render_activated_robot(self, robot):
        if not robot:
            return

        if robot.hp:
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

        else:
            self.battle.destroy(robot)

    def render_attack(self, extra=False):
        robot = self.battle.red_robot
        for field in self.battle.get_attack_fields(robot, extra):
            WIN.blit(
                ATTACK_IMAGE,
                (
                    field[1] * 100,
                    field[0] * 100
                )
            )
            pygame.display.update()
        pygame.time.wait(250)

    def draw_window(self, attacks=False):
        WIN.fill(WHITE)

        self.render_activated_robot(self.battle.red_robot)
        self.render_activated_robot(self.battle.blue_robot)
        self.render_deactivated_robots()
        self.render_items()

        pygame.display.update()

    def handle_movement(self, key):
        if key == pygame.K_UP:
            self.battle.turn(self.battle.red_robot, Direction.NORTH, log=False)
            self.battle.move(self.battle.red_robot, Move.UP)

        elif key == pygame.K_DOWN:
            self.battle.turn(self.battle.red_robot, Direction.SOUTH, log=False)
            self.battle.move(self.battle.red_robot, Move.DOWN)

        elif key == pygame.K_LEFT:
            self.battle.turn(self.battle.red_robot, Direction.WEST, log=False)
            self.battle.move(self.battle.red_robot, Move.LEFT)

        elif key == pygame.K_RIGHT:
            self.battle.turn(self.battle.red_robot, Direction.EAST, log=False)
            self.battle.move(self.battle.red_robot, Move.RIGHT)

    def handle_turning(self, key):
        if key == pygame.K_w:
            self.battle.turn(self.battle.red_robot, Direction.NORTH)

        elif key == pygame.K_s:
            self.battle.turn(self.battle.red_robot, Direction.SOUTH)

        elif key == pygame.K_a:
            self.battle.turn(self.battle.red_robot, Direction.WEST)

        elif key == pygame.K_d:
            self.battle.turn(self.battle.red_robot, Direction.EAST)

    def handle_attack(self, key):
        if key == pygame.K_SPACE:
            self.battle.attack(self.battle.red_robot)
            self.render_attack()

        elif key == pygame.K_RETURN:
            if self.battle.red_robot.extra_slot and self.battle.red_robot.extra_weapon:
                self.battle.attack(self.battle.red_robot, extra=True)
                self.render_attack(extra=True)

    def handle_select_weapon(self, key):
        mods = pygame.key.get_mods()

        if key == pygame.K_1:
            if mods & pygame.KMOD_CTRL:
                self.battle.select_extra_weapon(self.battle.red_robot, 0)
            else:
                self.battle.select_weapon(self.battle.red_robot, 0)

        elif key == pygame.K_2:
            if mods & pygame.KMOD_CTRL:
                self.battle.select_extra_weapon(self.battle.red_robot, 1)
            else:
                self.battle.select_weapon(self.battle.red_robot, 1)

        elif key == pygame.K_3:
            if mods & pygame.KMOD_CTRL:
                self.battle.select_extra_weapon(self.battle.red_robot, 2)
            else:
                self.battle.select_weapon(self.battle.red_robot, 2)

        elif key == pygame.K_4:
            if mods & pygame.KMOD_CTRL:
                self.battle.select_extra_weapon(self.battle.red_robot, 3)
            else:
                self.battle.select_weapon(self.battle.red_robot, 3)

        elif key == pygame.K_5:
            if mods & pygame.KMOD_CTRL:
                self.battle.select_extra_weapon(self.battle.red_robot, 4)
            else:
                self.battle.select_weapon(self.battle.red_robot, 4)

    def handle_select_body(self, key):
        if key == pygame.K_6:
            self.battle.select_body(self.battle.red_robot, 0)

        elif key == pygame.K_7:
            self.battle.select_body(self.battle.red_robot, 1)

        elif key == pygame.K_8:
            self.battle.select_body(self.battle.red_robot, 2)

        elif key == pygame.K_9:
            self.battle.select_body(self.battle.red_robot, 3)

        elif key == pygame.K_0:
            self.battle.select_body(self.battle.red_robot, 4)

    def run(self):
        clock = pygame.time.Clock()
        self.battle.start()
        run = True
        while run:
            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.KEYDOWN:
                    self.handle_movement(event.key)

                    self.handle_turning(event.key)

                    self.handle_attack(event.key)

                    self.handle_select_weapon(event.key)

                    self.handle_select_body(event.key)

            self.draw_window()

        pygame.quit()


if __name__ == '__main__':
    Game().run()
