#!/usr/bin/env python3

from common.geometry import Size
from entities.world import World
from common.smem import SMem

from time import sleep
import posix_ipc as ipc

CONFIG = {
    'ant': {
        'random_heading_p': 0.2,
        'random_heading_angle': 45,
        'step_distance': 1.0
    },
    'hive': {
        'ants': 2
    },
    'world': {
        'size': Size(999, 999),
        'hives': 1,
        'tick_pause_s': 0.01
    },
    'ipc': {
        'name': '/antsfoo',
        'flags': ipc.O_CREAT,
        'size': 4096
    }
}

def main():
    smem = SMem(CONFIG)
    smem.init_smem()
    world = World(CONFIG)
    while True:
        world.tick()
        smem.write_smem(world)
        if CONFIG['world']['tick_pause_s'] > 0:
            sleep(CONFIG['world']['tick_pause_s'])

if __name__ == '__main__':
    main()
