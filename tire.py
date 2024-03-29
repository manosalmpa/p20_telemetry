import kivy
kivy.require('1.10.1')
from kivy.graphics import Rectangle, Color
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle, Canvas, RoundedRectangle, Line
from kivy.properties import StringProperty, ListProperty, NumericProperty


Builder.load_string('''
<Tire>:
    name: self.name
    orientation: "horizontal"
    Label:
        text: "lo"
        canvas.before:
            Color:
                rgba: 0,0,1,1
            RoundedRectangle:
                pos: self.x, self.y
                size: self.size
                radius: [20,0,0,20]
            #Color:
                #rgba: 1,1,1,1
            #Line:
               #rectangle: self.x,self.y,self.width,self.height
                #width: 1
    Label:
        text: "li"
        canvas.before:
            Color:
                rgba: 0,1,0,1
            RoundedRectangle:
                pos: self.x, self.y
                size: self.size
                radius: [0,0,0,0]
    Label:
        text: "ri"
        canvas.before:
            Color:
                rgba: 0,1,0,1
            RoundedRectangle:
                pos: self.x, self.y
                size: self.size
                radius: [0,0,0,0]
    Label:
        text: "ro"
        canvas.before:
            Color:
                rgba: 0,1,0,1
            RoundedRectangle:
                pos: self.x, self.y
                size: self.size
                radius: [0,20,20,0]
''')

class Tire(BoxLayout):
    name = StringProperty()
    temp = ListProperty()

    def __init__(self,x=None,y=None, **kwargs):
        super(Tire, self).__init__(**kwargs)
        


