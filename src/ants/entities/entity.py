#!/usr/bin/env python2
# -*- coding: utf-8 -*-


class Entity:
    def init_graphics(self, renderer):
        self.renderer = renderer
        for child in self.children:
            child.init_graphics(self.renderer)

    def update_graphics(self):
        for child in self.children:
            child.update_graphics()

    def tick(self, time):
        self.time = time
        for child in self.children:
            child.tick(time)

