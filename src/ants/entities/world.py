#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from hive import Hive
from entity import Entity
from common import get_gui_pos

from kivy.graphics import Rectangle, Color

class World(Entity):
    def __init__(self, config):
        self.config = config
        self.hives = None
        self.children = None
        self.renderer = None
        self.movement = None
        self.mapgraphic = None
        self.time = 0
        self.build_hives()

    def build_hives(self):
        self.hives = []
        world_size = self.config['world']['size']
        self.movement = []
        for i in xrange(world_size.w + 1):
            foo = []
            for j in xrange(world_size.h + 1):
                foo.append(0)
            self.movement.append(foo)
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
        for i in xrange(len(self.movement)):
            for j in xrange(len(self.movement[i])):
                if self.movement[i][j] >= 1:
                    self.movement[i][j] -= 1
        #set movement points
        for hive in self.hives:
            for ant in hive.ants:
                pos = ant.position.get_tuple()
                self.movement[int(pos[0])][int(pos[1])] = 100

    def get_movement_gui_pos(self, simpos):
        simsize = self.config['world']['size'].get_tuple()
        guisize = self.renderer.width, self.renderer.height
        guipos = get_gui_pos(simsize, guisize, simpos)
        guipos = guipos[0] - float(self.config['ant']['rect_size_pixel'].get_tuple()[0]) / 2, guipos[1] - float(self.config['ant']['rect_size_pixel'].get_tuple()[1]) / 2
        return guipos

    def draw_movement(self):
        self.renderer.canvas.clear()
        for i in xrange(len(self.movement)):
            for j in xrange(len(self.movement[i])):
                if self.movement[i][j] >= 1:
                    with self.renderer.canvas:
                        Color(1, 1, 1, float(self.movement[i][j]) / 250)
                        Rectangle(pos=self.get_movement_gui_pos((i, j)), size=self.config['ant']['rect_size_pixel'].get_tuple())
