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
        text = self.root.ids.textinp.text
        print(text)



def create_window():
    WindowApp().run()

