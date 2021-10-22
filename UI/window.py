from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.lang import Builder
#TODO Basic textet törölje, de az utána jövő adatokat ne
#TODO vizsgálni a paramétereket, pl. 1000 szintes ne legyen valami
#TODO érintéses propertyt kikapcsolni

class Window(GridLayout):
    pass


class WindowApp(App):

    def build(self):
        return Window()

    def process(self):
        return 0

    def show(self):
        self.root.ids.BaseAreaTextInput.text = "Enter the area..."
        self.root.ids.LevelsTextInput.text = "No of max levels..."
        self.root.ids.BaseAreaTextInput.opacity = 1
        self.root.ids.LevelsTextInput.opacity = 1

    def hide(self):
        self.root.ids.BaseAreaTextInput.opacity = 0
        self.root.ids.LevelsTextInput.opacity = 0

    def print(self):
        print (self.root.ids.BaseAreaTextInput.text)
        print (self.root.ids.LevelsTextInput.text)


def create_window():
    WindowApp().run()
