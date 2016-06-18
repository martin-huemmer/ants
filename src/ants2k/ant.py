#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import random
import math

STEP_DISTANCE = 1
ROAM_RANDOM_HEADING_P = 0.4
ROAM_ANGLE_DIFF = 15

STATE_ROAM = 0

class Ant:
    def __init__(self, pos):
        self.pos = pos
        self.heading = random.randrange(0, 360)
        self.state = STATE_ROAM

    def move(self):
        if self.state == STATE_ROAM:
            self.random_heading()
        self.pos.x += math.cos(self.heading * math.pi / 180 ) * STEP_DISTANCE
        self.pos.y += math.sin(self.heading * math.pi / 180 ) * STEP_DISTANCE


    def random_heading(self):
        if random.random() < ROAM_RANDOM_HEADING_P:
            self.heading += (random.randrange(-ROAM_ANGLE_DIFF, ROAM_ANGLE_DIFF) % 360)



