#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from entity import Entity
from common import get_gui_pos
from random import randint
from math import sin, cos, pi

from kivy.graphics import Rectangle, Color


class Ant(Entity):
    def __init__(self, hive, config, position):
        self.config = config
        self.position = position
        self.graphic = None
        self.renderer = None
        self.hive = hive
        self.time = 0
        self.heading = randint(0, 359)

    def get_ant_gui_pos(self):
        simsize = self.config['world']['size'].get_tuple()
        guisize = self.renderer.width, self.renderer.height
        simpos = self.position.get_tuple()
        guipos = get_gui_pos(simsize, guisize, simpos)
        guipos = guipos[0] - float(self.config['ant']['rect_size_pixel'].get_tuple()[0]) / 2, guipos[1] - float(self.config['ant']['rect_size_pixel'].get_tuple()[1]) / 2
        return guipos

    def init_graphics(self, renderer):
        self.renderer = renderer
        with renderer.canvas:
            Color(self.hive.color[0], self.hive.color[1], self.hive.color[2])
            self.graphic = Rectangle(pos=self.get_ant_gui_pos(), size=self.config['ant']['rect_size_pixel'].get_tuple())

    def update_graphics(self):
        self.graphic.pos = self.get_ant_gui_pos()

    def tick(self, time):
        self.time = time
        self.walk()

    def walk(self):
        self.random_heading()
        distance = self.config['ant']['def_step_distance']
        self.position.x += cos(self.heading * pi / 180) * distance
        self.position.y += sin(self.heading * pi / 180) * distance
        self.stop_at_border()

    def stop_at_border(self):
        if self.position.x > self.config['world']['size'].w: self.position.x = self.config['world']['size'].w
        elif self.position.x < 0: self.position.x = 0
        if self.position.y > self.config['world']['size'].h: self.position.y = self.config['world']['size'].h
        elif self.position.y < 0: self.position.y = 0

    def random_heading(self):
        if randint(0, 100) < self.config['ant']['random_heading_p'] * 100:
            angle_diff = self.config['ant']['random_heading_angle']
            self.heading = (self.heading + randint(-angle_diff, angle_diff)) % 360
