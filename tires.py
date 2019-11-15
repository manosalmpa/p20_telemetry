import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle, Canvas
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

from tire_label import Tire_Label

class Tires(FloatLayout):
    def __init__(self, **kwargs):
        super(Tires, self).__init__(**kwargs)
        print("init")
        self.fl = GridLayout(cols = 4, rows = 1, pos_hint = {"top":1, "left":1}, size_hint = (0.2, 0.2))
        self.fr = GridLayout(cols = 4, rows = 1, pos_hint = {"top":1, "right":1}, size_hint = (0.2, 0.2))
        self.rl = GridLayout(cols = 4, rows = 1, pos_hint = {"bottom":1, "left":1}, size_hint = (0.2, 0.2))
        self.rr = GridLayout(cols = 4, rows = 1, pos_hint = {"bottom":1, "right":1}, size_hint = (0.2, 0.2))
        

        self.add_widget(self.fl)
        self.add_widget(self.fr)
        self.add_widget(self.rl)
        self.add_widget(self.rr)
        print(self.children)

        for x in self.children:
            for y in range(4):
                x.add_widget(Tire_Label(strip_id = y, temp=0))



