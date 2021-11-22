import random

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
import generate
import Model.BaseUnit

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
    gen = generate.Generate

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
            self.gen.area = areatext.text

    def levelsvalidate(self, levelstext):
        if int(levelstext.text) > 10:
            print("10 szintnél nagyobbat ne adjál meg légy kedves")
        else:
            self.gen.levels = levelstext.text

    def layoutBack(self, layoutarea):
        if layoutarea.page != 0:
            layoutarea.page -= 1
            self.root.ids.currentLayoutLabel.text = str(self.root.ids.layoutarea.page + 1)

    def layoutForward(self, layoutarea):
        if layoutarea.page != self.noOfLayoutsCurrently - 1:
            layoutarea.page += 1
            self.root.ids.currentLayoutLabel.text = str(self.root.ids.layoutarea.page + 1)

    def generateWidgets(self):
        layoutlist = self.gen.init(self.gen)
        self.root.ids.currentLayoutLabel.text = str(self.root.ids.layoutarea.page + 1)
        self.noOfLayoutsCurrently += self.gen.noOfLayouts
        for layouts in range(int(len(layoutlist))): # 5*5 mátrix a Groupoknak
            outerLayout = GridLayout()
            outerLayout.cols = int(len(layoutlist[layouts].Space))
            for basegroups in range(len(layoutlist[layouts].Space)):
                innerLayout = GridLayout()
                innerLayout.cols = 4
                for baseunits in range(len(layoutlist[layouts].Space[basegroups])):
                    for baseunitelement in range(len(layoutlist[layouts].Space[basegroups][baseunits])):
                        for unit in range(len(layoutlist[layouts].Space[basegroups][baseunits][baseunitelement])):
                            z = Button()
                            z.size_hint = (0.1,0.1)
                            z.text = str(unit)
                            if layoutlist[layouts].Space[basegroups][baseunits][baseunitelement][unit] == "X":
                                r = 0.5
                                g = 0.5
                                b = 0.5
                            elif layoutlist[layouts].Space[basegroups][baseunits][baseunitelement][unit] == "A":
                                r = 0
                                g = 0
                                b = 1
                            else:
                                r = 1
                                g = 1
                                b = 0
                            z.background_color = (r, g, b, 1)
                            innerLayout.add_widget(z)
                outerLayout.add_widget(innerLayout)
        self.root.ids.layoutarea.add_widget(outerLayout)

        #self.root.ids.layoutarea.add_widget(outerLayout)


def create_window():
    WindowApp().run()
