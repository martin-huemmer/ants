#!/usr/bin/env python2
# -*- coding: utf-8 -*-

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "x: %f, y: %f" % (self.x, self.y)