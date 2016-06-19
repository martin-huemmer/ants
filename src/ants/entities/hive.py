#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from ant import Ant
from entity import Entity
import copy


class Hive(Entity):
    def __init__(self, config, position):
        self.config = config
        self.position = position
        self.time = 0
        self.ants = None
        self.renderer = None
        self.children = None
        self.color = None
        self.spawn_ants()

    def spawn_ants(self):
        self.ants = []
        for i in range(self.config['hive']['ants']):
            ant = Ant(self, self.config, copy.deepcopy(self.position))
            self.ants.append(ant)
        self.children = self.ants
