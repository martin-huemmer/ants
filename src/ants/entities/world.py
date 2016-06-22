#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from hive import Hive
from entity import Entity

import numpy as np
from pprint import pprint


class World(Entity):
    def __init__(self, config):
        self.config = config
        self.hives = None
        self.children = None
        self.renderer = None
        self.time = 0
        self.build_hives()

    def build_hives(self):
        self.hives = []
        world_size = self.config['world']['size']
        self.movement = np.zeros((world_size.w + 1, world_size.h + 1))
        for i in range(self.config['world']['hives']):
            position = world_size.random_position()
            hive = Hive(self.config, position)
            hive.color = self.config['world']['hive_colors'][i]
            self.hives.append(hive)
        self.children = self.hives

    def tick(self, *args):
        self.time += 1
        for hive in self.hives:
            hive.tick(self.time)
        #fade movement
        for i,row in enumerate(self.movement):
            for j,col in enumerate(row):
                if self.movement[i][j] >= 0.1:
                    self.movement[i][j] -= 0.1
        #set movement points
        for hive in self.hives:
            for ant in hive.ants:
                pos = ant.position.get_tuple()
                self.movement[int(pos[0])][int(pos[1])] = 1

    def draw_movement(self):


