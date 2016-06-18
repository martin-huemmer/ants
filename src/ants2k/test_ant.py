#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from ant import Ant
from position import Position

class TestAnt(unittest.TestCase):
    def test_coodinates(self):
        ant = Ant(Position(0.0, 0.0))
        for i in xrange(0, 100):
            ant.move()
            print(ant.pos)

