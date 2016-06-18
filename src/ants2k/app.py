from kivy.app import App, Widget
from kivy.graphics import *

class Canvas(Widget):
    def __init__(self, **kwargs):
        super(Canvas, self).__init__(**kwargs)
        with self.canvas:
            Line(points=(0, 0, 100, 100))


class SimApp(App):
    def build(self):
        return Canvas()

if __name__ == '__main__':
    SimApp().run()