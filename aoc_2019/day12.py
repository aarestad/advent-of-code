from itertools import count
from typing import NamedTuple, Iterable


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

    def time_step_vector(self, other_planets: Iterable['Planet']):
        vel_del_x = 0
        vel_del_y = 0
        vel_del_z = 0

        for planet in other_planets:
            vel_del_x += spaceship(planet.pos.x, self.pos.x)
            vel_del_y += spaceship(planet.pos.y, self.pos.y)
            vel_del_z += spaceship(planet.pos.z, self.pos.z)

        self.vel = Vector(self.vel.x + vel_del_x,
                          self.vel.y + vel_del_y,
                          self.vel.z + vel_del_z
                          )

    def time_step_pos(self):
        self.pos = Vector(self.pos.x + self.vel.x,
                          self.pos.y + self.vel.y,
                          self.pos.z + self.vel.z
                          )


if __name__ == '__main__':
    # my input:
    # <x=4, y=12, z=13>
    # <x=-9, y=14, z=-3>
    # <x=-7, y=-1, z=2>
    # <x=-11, y=17, z=-1>

    planets = [
        Planet(Vector(x=-1, y=0, z=2), 'A'),
        Planet(Vector(x=2, y=-10, z=-7), 'B'),
        Planet(Vector(x=4, y=-8, z=8), 'C'),
        Planet(Vector(x=3, y=5, z=-1), 'D'),
    ]

    initial_state = {
        'A': Planet(Vector(x=-1, y=0, z=2), 'A'),
        'B': Planet(Vector(x=2, y=-10, z=-7), 'B'),
        'C': Planet(Vector(x=4, y=-8, z=8), 'C'),
        'D': Planet(Vector(x=3, y=5, z=-1), 'D'),
    }

    for i in count(1):
        if i % 10000 == 0: print(i)

        for planet in planets:
            planet.time_step_vector(p for p in planets if p != planet)
        for planet in planets:
            planet.time_step_pos()

        if all(p.state_eq(initial_state[p.name]) for p in planets):
            print(i)
            break
