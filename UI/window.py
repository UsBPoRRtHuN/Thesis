from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.lang import Builder

class Window(GridLayout):
    pass

class WindowApp(App):
    def build(self):
        return Window()

    def process(self):
        text = self.root.ids.BaseAreaTextInput.text
        text2 = self.root.ids.LevelsTextInput.text
        print(text)
        print(text2)
    def show (self):
        self.root.ids.BaseAreaTextInput.opacity = 1
        self.root.ids.LevelsTextInput.opacity = 1
    def hide (self):
        self.root.ids.BaseAreaTextInput.opacity = 0
        self.root.ids.LevelsTextInput.opacity = 0

def create_window():
    WindowApp().run()

