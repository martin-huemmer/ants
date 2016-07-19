#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from entities.entity import Entity
from entities.hive import Hive


class World(Entity):
    def __init__(self, config):
        self.config = config
        self.time = 0
        self.hives = []
        self.children = self.hives
        self.build_hives()

    def build_hives(self):
        world_size = self.config['world']['size']
        for i in range(self.config['world']['hives']):
            position = world_size.randpos()
            hive = Hive(self.config, position)
            self.hives.append(hive)

    def tick(self):
        self.time += 1
        for child in self.children:
            child.tick(self.time)
