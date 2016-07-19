#!/usr/bin/env python3

from common.geometry import Size
from entities.world import World

import posix_ipc as ipc
import mmap
from time import sleep

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


def analyze(world, smem):
    smem.seek(0)
    smem.write(("%03d%03d"%(world.hives[0].ants[0].position.get())).encode())
    for ant in world.hives[0].ants:
        print(ant.position)


def main():
    ipcsmem  = ipc.SharedMemory(CONFIG['ipc']['name'], CONFIG['ipc']['flags'], size=CONFIG['ipc']['size'])
    smem = mmap.mmap(ipcsmem.fd, ipcsmem.size)
    ipcsmem.close_fd()

    world = World(CONFIG)

    try:
        while True:
            world.tick()
            analyze(world, smem)
            if CONFIG['world']['tick_pause_s'] > 0:
                sleep(CONFIG['world']['tick_pause_s'])
    except KeyboardInterrupt:
        pass
    finally:
        smem.close()

if __name__ == '__main__':
    main()
