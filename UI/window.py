import random

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
import generate


# TODO adatok validálása (max. 20km2, max 20lvl), popup rá
# TODO multithread?
# TODO Visio diagram!
# TODO Unit test
# TODO Futási idő diagram


class Window(Widget):
    def __init__(self, **kwargs):
        super(Window, self).__init__(**kwargs)
        self.height = 599

    pass


class WindowApp(App):
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
        if int(areatext.text) > 8000:
            print("8000-nél nagyobbat ne adjál meg légy kedves")
        else:
            generate.area = areatext.text

    def levelsvalidate(self, levelstext):
        if int(levelstext.text) > 10:
            print("10 szintnél nagyobbat ne adjál meg légy kedves")
        else:
            generate.levels = levelstext.text

    def layoutBack(self, layoutarea):
        if layoutarea.page != 0:
            layoutarea.page -= 1
            self.root.ids.currentLayoutLabel.text = str(self.root.ids.layoutarea.page + 1)

    def layoutForward(self, layoutarea):
        if layoutarea.page != self.noOfLayoutsCurrently - 1:
            layoutarea.page += 1
            self.root.ids.currentLayoutLabel.text = str(self.root.ids.layoutarea.page + 1)

    def generateWidgets(self):
        generate.noOfLayouts = generate.calculate()
        self.root.ids.currentLayoutLabel.text = str(self.root.ids.layoutarea.page + 1)
        self.noOfLayoutsCurrently += generate.noOfLayouts
        self.root.ids.numberOfLayoutsLabel.text = str(generate.noOfLayouts)
        for i in range(int(generate.noOfLayouts)):
            bigLayout = GridLayout()
            bigLayout.cols = 3
            for i in range (5):
                layout = GridLayout()
                layout.cols = 4
                for i in range (16):
                    z = Button()
                    z.size_hint = (0.1,0.1)
                    r = random.uniform(0, 1)
                    g = random.uniform(0, 1)
                    b = random.uniform(0, 1)
                    z.background_color = (r, g, b, 1)
                    z.text = str(i + 1)
                    layout.add_widget(z)
                bigLayout.add_widget(layout)
            self.root.ids.layoutarea.add_widget(bigLayout)


def create_window():
    WindowApp().run()
