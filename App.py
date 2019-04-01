from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.properties import NumericProperty, Property
from kivy.clock import Clock
from random import randint

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.behaviors.button import ButtonBehavior

from kivy.animation import Animation
from kivy.graphics import Canvas

class Gerenciador(ScreenManager):
    pass

class Menu(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class Game(Screen):
    score = NumericProperty(0)

    def on_pre_enter(self, *args):
        lanes = self.ids.jogo.children
        Clock.schedule_interval(lambda e: lanes[randint(0, len(lanes) - 1)].createTile(), 1)
        return super().on_pre_enter(*args)

    def increase_score(self):
        self.score += 10

class Lane(ButtonBehavior, FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def createTile(self):
        tileHeight = self.height * 0.3
        self.add_widget(Tile(size=(self.width * 0.9, tileHeight), y=self.height, x=self.x + (self.width * 0.1) / 2))

class Tile(ButtonBehavior, Label):
    y = NumericProperty(0)
    x = NumericProperty(0)
    cor = Property((0, 0, 0, 1))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        anim = Animation(y=-self.height)
        anim.start(self)

    def on_press(self):
        App.get_running_app().root.current_screen.increase_score()
        self.cor = 0, 0, 0, 0.3
        return super().on_press()
    
class Boi(App):
    def build(self):
        return Gerenciador()

Boi().run()