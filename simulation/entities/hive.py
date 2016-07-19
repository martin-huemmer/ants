#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from entities.entity import Entity
from entities.ant import Ant

import copy


class Hive(Entity):
    def __init__(self, config, position):
        self.config = config
        self.position = position
        self.time = 0
        self.ants = []
        self.children = self.ants
        self.spawn_ants()

    def spawn_ants(self):
        for i in range(self.config['hive']['ants']):
            ant = Ant(self.config, copy.deepcopy(self.position))
            self.ants.append(ant)
        self.children = self.ants
