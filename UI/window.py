from kivy.app import App
from kivy.uix.widget import Widget


class Window(Widget):
    pass


class WindowApp(App):

    def build(self):
        return Window()

    def process(self):
        return 0

    def showArea(self):
        self.root.ids.Area.opacity = 1
        self.root.ids.Area.disabled = False

    def showLevels(self):
        self.root.ids.Levels.opacity = 1
        self.root.ids.Levels.disabled = False

    def hideArea(self):
        self.root.ids.Area.opacity = 0
        self.root.ids.Area.disabled = True

    def hideLevels(self):
        self.root.ids.Levels.opacity = 0
        self.root.ids.Levels.disabled = True

    def saveValues(self):
        area = self.root.ids.Area.text
        levels = self.root.ids.Levels.text
        print(area, levels)

def create_window():
    WindowApp().run()
