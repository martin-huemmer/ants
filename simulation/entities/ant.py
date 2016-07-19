#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from entities.entity import Entity

from random import randint
from math import sin, cos, pi


class Ant(Entity):
    def __init__(self, config, position):
        self.config = config
        self.position = position
        self.time = 0
        self.heading = randint(0, 359)

    def tick(self, time):
        self.time = time
        self.step()

    def step(self):
        self.random_heading()
        distance = self.config['ant']['step_distance']
        self.position.x += cos(self.heading * pi / 180) * distance
        self.position.y += sin(self.heading * pi / 180) * distance
        self.snap_bounds()

    def snap_bounds(self):
        if self.position.x > self.config['world']['size'].w:
            self.position.x = self.config['world']['size'].w
        elif self.position.x < 0:
            self.position.x = 0
        if self.position.y > self.config['world']['size'].h:
            self.position.y = self.config['world']['size'].h
        elif self.position.y < 0:
            self.position.y = 0

    def random_heading(self):
        if randint(0, 100) < self.config['ant']['random_heading_p'] * 100:
            angle_diff = self.config['ant']['random_heading_angle']
            self.heading = (self.heading + randint(-angle_diff, angle_diff)) % 360
