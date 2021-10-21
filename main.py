from kivy.app import App
from kivy.uix.button import Button


if __name__ == '__main__':
    from kivy.uix.dropdown import DropDown
    from kivy.uix.button import Button
    from kivy.base import runTouchApp
    dropdown = DropDown()
    names = ["options", "exit"]
    for index in range(2):

        btn = Button(text=names[index], size_hint_y=None, height=20)
        btn.bind(on_release=lambda btn: dropdown.select(btn.text))

        # then add the button inside the dropdown
        dropdown.add_widget(btn)

    # create a big main button
    mainbutton = Button(text='Hello', size_hint=(None, None))

    # show the dropdown menu when the main button is released
    # note: all the bind() calls pass the instance of the caller (here, the
    # mainbutton instance) as the first argument of the callback (here,
    # dropdown.open.).
    mainbutton.bind(on_release=dropdown.open)

    # one last thing, listen for the selection in the dropdown list and
    # assign the data to the button text.
    dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))

    runTouchApp(mainbutton)
