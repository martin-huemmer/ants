__author__ = 'martinhummer'


import random
from src.utils import directions

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

