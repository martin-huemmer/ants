from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, NumericProperty
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.clock import Clock
from position import Position
from hive import Hive

class AntHive(Widget):

    def createHive(self, size):
        self.hive = Hive(Position(Window.size[0]/2,Window.size[1]/2), size)


class HiveCanvas(Widget):

    hiveObject = ObjectProperty(None)

    def createHiveInstance(self, size):
       self.hiveObject.createHive(size)

    # update canvas
    def draw(self, dt):
        self.hiveObject.canvas.clear()

        for ant in self.hiveObject.hive.ants:

            with self.hiveObject.canvas:
                # Add a white color
                Color(1, 1, 1)
                # Add a rectangle
                Rectangle(pos=ant.pos.returnTuple(), size=(1, 1))

    # update position
    def tick(self, dt):
        for ant in self.hiveObject.hive.ants:
            foo = ant
            pos = foo.pos
            ant.move()
            test = ant.pos


class SimApp(App):
    def build(self):
        canvas = HiveCanvas()
        # call update position calculation
        canvas.createHiveInstance(5)
        Clock.schedule_interval(canvas.tick, 1)
        # call redrawing of canvas
        Clock.schedule_interval(canvas.draw, 1)
        return canvas


if __name__ == '__main__':
    SimApp().run()