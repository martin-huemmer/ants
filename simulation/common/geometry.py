#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randint


class Position:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def get(self):
        return self.x, self.y

    def __str__(self):
        return "x: %f, y: %f" % (self.x, self.y)


class Size:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def randpos(self):
        return Position(randint(0, self.w), randint(0, self.h))

    def get(self):
        return self.w, self.h

    def __str__(self):
        return "w: %f, h: %f" % (self.w, self.h)
