from kivy.app import App
from kivy.uix.widget import Widget


class Window(Widget):
    pass


class WindowApp(App):

    def build(self):
        return Window()

def create_window():
    WindowApp().run()
