from kivy.core.window import Window
import kivy
kivy.require("1.10.1")
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, Rectangle, Canvas
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.lang import Builder

#kv = Builder.load_file("tire_temps.kv")

from tires import Tires

class MainScreen(App):

    def build(self):
        Window.clearcolor = (0, 0, 0, 1)
        Window.fullscreen = False
        mainscreen = GridLayout()
        mainscreen.cols = 3
        left = FloatLayout()

        #tire_temps
        tire_temps = Tires(
            pos_hint={'x':0, 'y':0},
            size_hint = (1, 0.5)
        )
        left.add_widget(tire_temps)
        mainscreen.add_widget(left)
        mainscreen.add_widget(Label(text = "tipota"))
        mainscreen.add_widget(Label(text = "tipota"))
        return mainscreen


if __name__ == '__main__':
    try:
        MainScreen().run()
    except Exception as e:
        raise e        
