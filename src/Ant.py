__author__ = 'martinhummer'


import random
from utils import directions
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

class Ant:

    def __init__(self, name, home, pheromoneMap):
        self.name = name
        self.home = home
        self.homing = False
        # only pass value
        xHome = home[0]
        yHome = home[1]

        self.pos = [xHome, yHome]
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
        if self.pos[0] > 500:
            self.homing = True
        if self.homing:
            self.comeHome()
        else:
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

    def comeHome(self):
        # get home
        if self.pos[0] > self.home[0]:
            self.pos[0] = self.pos[0] - 1
        elif self.pos[0] < self.home[0]:
            self.pos[0] = self.pos[0] + 1
        else:
            self.pos[0] = self.pos[0]

        if self.pos[1] > self.home[1]:
            self.pos[1] = self.pos[1] - 1
        elif self.pos[1] < self.home[1]:
            self.pos[1] = self.pos[1] + 1
        else:
            self.pos[1] = self.pos[1]
        self.excretePheromones()


    def excretePheromones(self):
        self.pheromoneMap.map[self.pos[0]][self.pos[1]] = self.pheromoneMap.map[self.pos[0]][self.pos[1]] + 1


class Hive(Ant, PheromoneMap):

    def __init__(self, home, size, area):
        print home
        self.hiveHomeX = home[0]
        self.hiveHomeY = home[1]
        self.size = size
        self.areaSize = area
        self.ants = []
        self.memberPositions = []
        # create pheromoneMap
        self.pheromoneMap = PheromoneMap(self.areaSize)
        self.createHive()


    def createHive(self):
        for el in range(self.size):
            ant = Ant('Ant'+str(el),[self.hiveHomeX, self.hiveHomeY],self.pheromoneMap)
            self.ants.append(ant)

    def hiveRoam(self):
        self.memberPositions = []
        for ant in self.ants:
            self.memberPositions.append(ant.roam())


    def updateHive(self):
        self.hiveRoam()
        self.pheromoneMap.decayMap()
        return self.memberPositions, self.pheromoneMap.map
