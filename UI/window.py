from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.core.window import Window
# TODO adatok validálása (max. 20km2, max 20lvl), popup rá
# TODO multithread?
#
import generate


class Window(Widget):
    pass


class WindowApp(App):
    # Default értékek
    area = 8000
    levels = 4
    noOfLayouts = 20
    noOfLayoutsCurrently = 0

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

        self.area = areatext.text

    def levelsvalidate(self, levelstext):
        self.levels = levelstext.text

    def calculateNoOfLayouts(self):
        self.noOfLayouts = generate.calculate(self.area, self.levels)
        self.root.ids.numberOfLayoutsLabel.text = str(self.noOfLayouts)

    def createLayouts(self):
        for i in range(int(self.noOfLayouts)):
            b = Button()
            b.text = str(i + 1)
            self.root.ids.layoutarea.add_widget(b)
        self.root.ids.currentLayoutLabel.text = str(self.root.ids.layoutarea.page + 1)
        self.noOfLayoutsCurrently += self.noOfLayouts

    def layoutBack(self, layoutarea):
        if layoutarea.page != 0:
            layoutarea.page -= 1
            self.root.ids.currentLayoutLabel.text = str(self.root.ids.layoutarea.page + 1)

    def layoutForward(self, layoutarea):
        if layoutarea.page != self.noOfLayoutsCurrently - 1:
            layoutarea.page += 1
            self.root.ids.currentLayoutLabel.text = str(self.root.ids.layoutarea.page + 1)


def create_window():
    WindowApp().run()
