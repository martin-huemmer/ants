#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import numpy as np

# PheromoneMap Class
# creation of pheromone map and handeling decay
# over time
# map is updated by ants
class PheromoneMap:

    def __init__(self, size):
        self.size = size
        self.map = []
        self.createMap()

    def createMap(self):
        self.map = np.zeros((self.size[0], self.size[1]))

    # decay every timestep every location with -0.1
    def decayMap(self):
        self.map = self.map - 0.01
        # set values < 0 to 0
        self.map = self.map.clip(min=0)
        # allow only max values of 1
        self.map = self.map.clip(max=1)
