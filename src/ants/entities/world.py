#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from hive import Hive
from entity import Entity

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
