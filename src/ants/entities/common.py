#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from random import randint


def get_gui_pos(simsize, guisize, simpos):
    factor_x = float(guisize[0]) / float(simsize[0])
    factor_y = float(guisize[1]) / float(simsize[1])
    return simpos[0] * factor_x, simpos[1] * factor_y


class Position:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def get_tuple(self):
        return self.x, self.y

    def __str__(self):
        return "x: %f, y: %f" % (self.x, self.y)


class Size:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def random_position(self):
        return Position(randint(0, self.w), randint(0, self.h))

    def get_tuple(self):
        return self.w, self.h

    def __str__(self):
        return "w: %f, h: %f" % (self.w, self.h)

