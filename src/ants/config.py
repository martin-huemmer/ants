#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from entities.common import Size

CONFIG = {
    'ant': {
        'random_heading_p': 0.1,
        'random_heading_angle': 45,
        'def_step_distance': 1.0,
        'rect_size_pixel': Size(2, 2)
    },
    'hive': {
        'ants': 25
    },
    'world': {
        'size': Size(1000, 1000),
        'hives': 3,
        'hive_colors': [(1, 0, 0, 1), (0, 1, 0, 1), (0, 0, 1, 1)],
        'tick_interval': 0.05
    },
    'renderer': {
        'update_interval': 0.1
    }
}
