#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import posix_ipc as ipc
import mmap


class SMem:
    def __init__(self, config):
        self.config = config
        self.smem = None

    def init_smem(self):
        posixsmem = ipc.SharedMemory(self.config['ipc']['name'], self.config['ipc']['flags'],
                                     size=self.config['ipc']['size'])
        self.smem = mmap.mmap(posixsmem.fd, posixsmem.size)
        posixsmem.close_fd()

    def write_smem(self, world):
        self.smem.seek(0)
        self.smem.write(("%03d%03d" % (world.hives[0].ants[0].position.get())).encode())
