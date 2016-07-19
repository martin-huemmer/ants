#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Entity:
    def __init__(self):
        self.time = 0
        self.children = None

    def tick(self, time):
        self.time = time
        for child in self.children:
            child.tick(time)
        self.step()

    def step(self):
        pass
