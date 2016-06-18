'''
Rotation Example
================

This example rotates a button using PushMatrix and PopMatrix. You should see
a static button with the words 'hello world' rotated at a 45 degree angle.
'''

from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.properties import NumericProperty, BooleanProperty, ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget

from src.objects.hive import Hive


class AntHive(Widget):

    counter = NumericProperty(0)
    hive = ObjectProperty(None)

    def createHive(self, size):
        self.hive = Hive([Window.size[0]/2,Window.size[1]/2], size, [Window.size[0],Window.size[1]])



class Terimal(FloatLayout):

    locations = []
    pheromones = []
    hiveObject = ObjectProperty(None)
    pheromoneStatus = BooleanProperty(False)

    #antHive = AntHive()
    dt = NumericProperty(0)

    def animate(self, do_animation):

        if do_animation:
            self.ids.button1.text = "Stop Animation"
            Clock.schedule_interval(self.update_points_animation, 0)
        else:
            self.ids.button1.text = "Run Animation"
            Clock.unschedule(self.update_points_animation)

    def update_points_animation(self, dt):
        self.hiveObject.counter = self.dt
        cy = self.height * 0.6
        cx = self.width * 0.1
        w = self.width * 0.8
        self.hiveObject.canvas.clear()
        self.locations, self.pheromones = self.hiveObject.hive.updateHive()


        if self.pheromoneStatus:
            rowCounter = 0
            for row in self.pheromones:
                colCounter = 0
                for col in row:
                    if col > 0:
                        with self.hiveObject.canvas:
                            # Add a red color
                            Color(0, 0, 1, col)
                            # Add a rectangle
                            Rectangle(pos=(rowCounter, colCounter), size=(1, 1))
                        #qp.setPen(QtGui.QColor(0, 0, 255, col*255))
                        #qp.drawPoint(rowCounter, colCounter)
                    colCounter = colCounter + 1
                rowCounter = rowCounter + 1

        for el in self.locations:
            self.updateAnts(el[0],el[1])
        # wait a bit
        #time.sleep(.1)
        self.dt += dt

    def reset(self):
        self.hiveObject.counter = 0
        self.hiveObject.canvas.clear()
        self.hiveObject.createHive(int(self.ids.test.text))

    def updateAnts(self, x, y):
        with self.hiveObject.canvas:
            # Add a red color
            Color(1, 1, 1)
            # Add a rectangle
            Rectangle(pos=(x, y), size=(1, 1))


    def pheromoneAnimate(self, test):
        print test
        print self.pheromoneStatus

    pass

class Ant(App):
    kv_directory = 'template'
    def build(self):
        return Terimal()


if __name__ == '__main__':
    Ant().run()