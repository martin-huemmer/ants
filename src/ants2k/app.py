from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from ant import Ant
from kivy.clock import Clock
from position import Position


class AntPixel(Widget):

    antObject = ObjectProperty(None)
    antObject = Ant(Position(400,400))

    def move(self):
        self.antObject.move()

    def draw(self):
        self.pos = self.antObject.pos.returnTuple()

class HiveCanvas(Widget):

    ant = ObjectProperty(None)

    # update canvas
    def draw(self, dt):
        self.ant.draw()

    # update position
    def tick(self, dt):
        self.ant.move()


class SimApp(App):
    def build(self):
        canvas = HiveCanvas()
        # call update position calculation
        Clock.schedule_interval(canvas.tick, .1)
        # call redrawing of canvas
        Clock.schedule_interval(canvas.draw, 1)
        return canvas


if __name__ == '__main__':
    SimApp().run()