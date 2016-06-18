#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from ant import Ant
from position import Position

class Hive:

    def __init__(self, pos, size):
        self.pos = pos
        self.size = size
        self.ants = []
        self.init_hive()


    def init_hive(self):
        for i in range(self.size):
            self.ants.append(Ant(self.pos))
