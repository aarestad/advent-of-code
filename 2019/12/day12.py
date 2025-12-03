from itertools import count
from typing import NamedTuple, Iterable
from aoc_2019.utils import lcm


def spaceship(a, b):
    return 1 if a > b else -1 if a < b else 0


class Vector(NamedTuple):
    x: int
    y: int
    z: int


class Planet:
    def __init__(self, pos: Vector, name: str):
        self.pos = pos
        self.vel = Vector(0, 0, 0)
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def state_eq(self, other):
        return self.pos == other.pos and self.vel == other.vel

    def __repr__(self):
        return "{}: pos={}, vel={}".format(self.name, self.pos, self.vel)

    def time_step_vector(self, other_planets: Iterable["Planet"]):
        vel_del_x = 0
        vel_del_y = 0
        vel_del_z = 0

        for planet in other_planets:
            vel_del_x += spaceship(planet.pos.x, self.pos.x)
            vel_del_y += spaceship(planet.pos.y, self.pos.y)
            vel_del_z += spaceship(planet.pos.z, self.pos.z)

        self.vel = Vector(
            self.vel.x + vel_del_x, self.vel.y + vel_del_y, self.vel.z + vel_del_z
        )

    def time_step_pos(self):
        self.pos = Vector(
            self.pos.x + self.vel.x, self.pos.y + self.vel.y, self.pos.z + self.vel.z
        )


if __name__ == "__main__":
    planets = [
        Planet(Vector(x=4, y=12, z=13), "A"),
        Planet(Vector(x=-9, y=14, z=-3), "B"),
        Planet(Vector(x=-7, y=-1, z=2), "C"),
        Planet(Vector(x=-11, y=17, z=-1), "D"),
    ]

    initial_state = {
        "A": Planet(Vector(x=4, y=12, z=13), "A"),
        "B": Planet(Vector(x=-9, y=14, z=-3), "B"),
        "C": Planet(Vector(x=-7, y=-1, z=2), "C"),
        "D": Planet(Vector(x=-11, y=17, z=-1), "D"),
    }

    steps_for_x = 0
    steps_for_y = 0
    steps_for_z = 0

    for i in count(1):
        if i % 10000 == 0:
            print("step {}".format(i))

        for planet in planets:
            planet.time_step_vector(p for p in planets if p != planet)
        for planet in planets:
            planet.time_step_pos()

        if not steps_for_x and all(
            p.pos.x == initial_state[p.name].pos.x
            and p.vel.x == initial_state[p.name].vel.x
            for p in planets
        ):
            steps_for_x = i
            print("steps for x: {}".format(steps_for_x))

        if not steps_for_y and all(
            p.pos.y == initial_state[p.name].pos.y
            and p.vel.y == initial_state[p.name].vel.y
            for p in planets
        ):
            steps_for_y = i
            print("steps for y: {}".format(steps_for_y))

        if not steps_for_z and all(
            p.pos.z == initial_state[p.name].pos.z
            and p.vel.z == initial_state[p.name].vel.z
            for p in planets
        ):
            steps_for_z = i
            print("steps for z: {}".format(steps_for_z))

        if all((steps_for_x, steps_for_y, steps_for_z)):
            print(lcm(steps_for_x, lcm(steps_for_y, steps_for_z)))
            break
