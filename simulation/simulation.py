#!/usr/bin/env python3

from common.geometry import Size
from entities.world import World

from time import sleep

CONFIG = {
    'ant': {
        'random_heading_p': 0.1,
        'random_heading_angle': 45,
        'step_distance': 1.0
    },
    'hive': {
        'ants': 2
    },
    'world': {
        'size': Size(999, 999),
        'hives': 1,
        'tick_pause_s': 0
    }
}


def analyze(world):
    pass
    #for ant in world.hives[0].ants:
    #    print(ant.position)


def main():
    world = World(CONFIG)
    while True:
        world.tick()
        analyze(world)
        if CONFIG['world']['tick_pause_s'] > 0:
            sleep(CONFIG['world']['tick_pause_s'])


if __name__ == '__main__':
    main()
