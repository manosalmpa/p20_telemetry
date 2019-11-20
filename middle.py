import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle, Canvas, Line
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_string('''
<Middle>:
    canvas.before:
        Color:
            rgba: 1,0,0,1
        Line:
            rectangle: self.x, self.y, self.height/2, self.width
    Label:
        pos_hint: {"top":1, "x":0.3}
        size_hint: 0.2, 0.2
        text: "middle"
''')



class Middle(FloatLayout):
    def __init__(self, **kwargs):
        super(Middle, self).__init__(**kwargs)
