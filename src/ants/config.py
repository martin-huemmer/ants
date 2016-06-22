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
        'ants': 1
    },
    'world': {
        'size': Size(10, 10),
        'hives': 1,
        'hive_colors': [(1, 0, 0, 1), (0, 1, 0, 1), (0, 0, 1, 1)],
        'tick_interval': 1
    },
    'renderer': {
        'update_interval': 1
    }
}
