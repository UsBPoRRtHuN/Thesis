from kivy.app import App
from kivy.uix.button import Button


if __name__ == '__main__':

    class TestApp(App):
        def build(self):
            return Button(text='Hello World')
    TestApp().run()

