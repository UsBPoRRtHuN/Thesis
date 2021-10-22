from kivy.app import App
from kivy.uix.gridlayout import GridLayout


class Thesis(GridLayout):
    pass

class ThesisApp(App):
    def build(self):
        return Thesis()

def create_window():
    ThesisApp().run()