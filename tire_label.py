import kivy
kivy.require('1.10.1')
from kivy.graphics import Rectangle, Color
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, Rectangle, Canvas, RoundedRectangle
from kivy.properties import StringProperty, ListProperty, NumericProperty


class Tire_Label(Label):
    strip_id = NumericProperty()
    temp = NumericProperty()

    def __init__(self, **kwargs):
        super(Tire_Label, self).__init__(**kwargs)
        self.text = str(self.temp)

#class Tire_Strip(Label):
#    strip_id = NumericProperty()
#    temp = NumericProperty()
#    def __init__(self, **kwargs):
#        super(Tire_Strip, self).__init__(**kwargs)
#        self.text = str(self.temp)
#        with self.canvas:
#            Color(0,0,1,.2, mode = "rgba")
#            if self.strip_id == 0:
#                self.rect = RoundedRectangle(pos = (self.x,self.y), size = self.size, radius = [20,20,0,0])
#            elif self.strip_id == 3:                
#                self.rect = RoundedRectangle(pos = self.pos, size = self.size, radius = [0,0,20,20])
#            else:
#                self.rect = RoundedRectangle(pos = self.pos, size = self.size, radius = [0,0,0,0]) 


