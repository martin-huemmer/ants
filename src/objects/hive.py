#!/usr/bin/env python2
# -*- coding: utf-8 -*-


from permomonemap import *
from ant import *


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