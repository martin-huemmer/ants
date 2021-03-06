#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock

from config import CONFIG
from entities.world import World


class WorldRenderer(Widget):
    def __init__(self, world):
        super(WorldRenderer, self).__init__()
        self.world = world
        self.world.init_graphics(self)

    def update(self, *args):
        self.world.update_graphics()


class Ants(App):
    def build(self):
        world = World(CONFIG)
        Clock.schedule_interval(world.tick, CONFIG['world']['tick_interval'])
        renderer = WorldRenderer(world)
        Clock.schedule_interval(renderer.update, CONFIG['renderer']['update_interval'])
        return renderer


if __name__ == "__main__":
    Ants().run()
