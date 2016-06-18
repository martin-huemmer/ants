#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import random
from src.utils import directions


# Basic ant class. Initializes Ant with a home position and a pheromoneMap which is updated every time the ant moves.
# The ant has a roam function, that is executed for each step it is walking. There is a 10% Chance to change the
# direction for each step.

class Ant:

    def __init__(self, id, pos, pheromoneMap):
        self.id = id
        self.pos = pos
        self.pheromoneMap = pheromoneMap
        self.maxX, self.maxY = self.pheromoneMap.size
        self.minX, self.minY = [0,0]
        # random initial heading
        self.heading = random.randrange(0, 360, 45)

    def setDirection(self):
        # 10% chance to change direction
        if random.random() < .10:
            # direction change (+/- 45deg)
            if random.getrandbits(1) == 0:
                self.heading = self.heading + 45
            else:
                self.heading = self.heading - 45

    def roam(self):

        self.setDirection()
        direction = self.heading % 360
        # walk one step in direction
        self.pos = directions[direction](self.pos)
        # turn arround when reaching the border
        if self.pos[0] >= self.maxX:
            self.pos[0] = self.maxX - 1
        if self.pos[0] <= self.minX:
            self.pos[0] = 1
        if self.pos[1] >= self.maxY:
            self.pos[1] = self.maxY - 1
        if self.pos[1] <= self.minY:
            self.pos[1] = 1
        self.excretePheromones()

        return self.pos

    def excretePheromones(self):
        self.pheromoneMap.map[self.pos[0]][self.pos[1]] = self.pheromoneMap.map[self.pos[0]][self.pos[1]] + 1

