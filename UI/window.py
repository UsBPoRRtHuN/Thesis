from kivy.app import App
from kivy.uix.widget import Widget


class Window(Widget):
    pass


class WindowApp(App):
    area = 8000
    levels = 4

    def build(self):
        return Window()

    def optionstogglebutton(self, togglebutton):

        if (togglebutton.state == "down"):
            self.root.ids.AreaInput.disabled = 0
            self.root.ids.LevelsInput.disabled = 0
            self.root.ids.AreaInput.opacity = 1
            self.root.ids.LevelsInput.opacity = 1
        else:
            self.root.ids.AreaInput.disabled = 1
            self.root.ids.LevelsInput.disabled = 1
            self.root.ids.AreaInput.opacity = 0
            self.root.ids.LevelsInput.opacity = 0

    def areavalidate(self, areatext):
        print(areatext.text)
        self.area = areatext.text

    def levelsvalidate(self,levelstext):
        self.levels = levelstext.text

    def print (self):
        print (str(self.area) + "   " + str(self.levels))

def create_window():
    WindowApp().run()
