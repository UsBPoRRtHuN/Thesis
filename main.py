from kivy.config import Config
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
Config.set('graphics', 'resizable', True)

class Thesis(GridLayout):
    pass
class ThesisApp(App):
    def build(self):
        return Thesis()
if __name__ == '__main__':
    ThesisApp().run()