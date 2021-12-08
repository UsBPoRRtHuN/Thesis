from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import generate
from kivy.uix.popup import Popup
from kivy.uix.label import Label
import threading


# TODO Visio diagram
# TODO Unit test
# TODO Futási idő diagram


class Window(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.height = 599

    pass


class WindowApp(App):
    gen = generate.Generate
    noOfLayoutsCurrently = 0
    maxArea = 20000
    maxLevels = 20

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
        if int(areatext.text) > self.maxArea:
            box = BoxLayout()
            box.orientation = "vertical"
            label = Label()
            label.text = "The maximum allowed area is : " + str(self.maxArea) + " m2!"
            button = Button()
            button.text = "OK"
            button.size_hint = 0.7, 0.5
            box.add_widget(label)
            box.add_widget(button)
            popup = Popup(title='Error: Invalid data', content=box, size=(100, 100), auto_dismiss=False)
            popup.size_hint = 0.45, 0.45
            popup.open()
            button.bind(on_press=popup.dismiss)
        else:
            self.gen.area = areatext.text

    def levelsvalidate(self, levelstext):
        if int(levelstext.text) > self.maxLevels:
            box = BoxLayout()
            box.orientation = "vertical"
            label = Label()
            label.text = "The maximum allowed number of levels is: " + str(self.maxLevels) + "!"
            button = Button()
            button.text = "OK"
            button.size_hint = 0.7, 0.5
            box.add_widget(label)
            box.add_widget(button)
            popup = Popup(title='Error: Invalid data', content=box, size=(100, 100), auto_dismiss=False)
            popup.size_hint = 0.45, 0.45
            popup.open()
            button.bind(on_press=popup.dismiss)
        else:
            self.gen.levels = levelstext.text

    def layoutBack(self, layoutarea):
        if layoutarea.page != 0:
            self.root.ids.layoutarea.clear_widgets()
            layoutarea.page -= 1
            self.root.ids.currentLayoutLabel.text = str(self.root.ids.layoutarea.page + 1)
            t1 = threading.Thread(target=self.generateWidgets())
            t1.start()

    def layoutForward(self, layoutarea):
        if layoutarea.page != self.noOfLayoutsCurrently - 1:
            self.root.ids.layoutarea.clear_widgets()
            layoutarea.page += 1
            self.root.ids.currentLayoutLabel.text = str(self.root.ids.layoutarea.page + 1)
            t1 = threading.Thread(target=self.generateWidgets())
            t1.start()

    def generateWidgets(self):
        num = self.root.ids.layoutarea.page
        layout = self.gen.getLayout(self.gen, num)
        self.noOfLayoutsCurrently = self.gen.noOfLayouts
        self.root.ids.currentLayoutLabel.text = str(self.root.ids.layoutarea.page + 1)
        num = int(self.root.ids.currentLayoutLabel.text) - 1
        outerLayout = GridLayout()
        outerLayout.cols = int(len(layout.Space))
        for basegroups in range(len(layout.Space)):
            innerLayout = GridLayout()
            innerLayout.cols = 4
            for baseunits in range(len(layout.Space[basegroups])):
                for baseunitelement in range(len(layout.Space[basegroups][baseunits])):
                    for unit in range(len(layout.Space[basegroups][baseunits][baseunitelement])):
                        z = Button()
                        z.text = str(unit)
                        if layout.Space[basegroups][baseunits][baseunitelement][unit] == "X":
                            z.background_color = (0, 0, 1, 1)
                            z.text = ""
                        elif layout.Space[basegroups][baseunits][baseunitelement][unit] == "A":
                            r = 1
                            g = 0
                            b = 1
                            z.background_color = (r, g, b, 1)
                            z.text = "A"
                        else:
                            r = 1
                            g = 1
                            b = 0
                            z.background_color = (r, g, b, 1)
                            z.text = "I"
                        innerLayout.padding = 3
                        innerLayout.add_widget(z)
            outerLayout.add_widget(innerLayout)
        self.root.ids.layoutarea.add_widget(outerLayout)


def create_window():
    WindowApp().run()
