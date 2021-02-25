from src import arena, robot
from src.base import Move, Direction


class Battle:

    def __init__(self):
        self.arena = arena.Arena()
        self.robot_red = robot.ActivatedRobot(robot.Team.RED)
        self.robot_blue = robot.ActivatedRobot(robot.Team.BLUE)

    def start(self):
        self.arena.init()
        self.init_robots()

    def move(self, robot: robot.ActivatedRobot, move: Move):
        position = robot.position
        dest = self.arena.move(position, move)
        robot.position = dest

    def turn(self, robot: robot.ActivatedRobot, direction: Direction):
        robot.turn(direction)

    def attack(self, robot: robot.ActivatedRobot, idx: int = 0):
        weapon = robot.attack(idx)
        # szuka czy w zasiegu razenia jest jakis robot
        facing = robot.facing.index(1)
        rng = weapon.range
        dircts = weapon.directions
        print(rng)
        print(dircts)
        # w zaleznosci od facingu - zmieniaja sie macierze broni

        rng = turn_matrix(rng)
        dircts = turn_matrix(dircts)
        print(rng)
        print(dircts)

        # jesli nie - nic sie nie dzieje
        # jesli tak - pobiera jego polozenie i sprawdza po wszystkich robotach ktory to
        # nastepnie odejmuje mu 1hp

    def init_robots(self):
        robot_red_position_y = self.arena.board[0].index('x')
        robot_blue_position_y = self.arena.board[5].index('x')
        self.robot_red.position = (0, robot_red_position_y)
        self.robot_red.facing = [0, 0, 1, 0]
        self.robot_blue.position = (5, robot_blue_position_y)

