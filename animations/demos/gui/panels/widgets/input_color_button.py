from gui.panels.widgets.input_widget import InputWidget

# pylint: disable=too-few-public-methods
class InputColorButton(InputWidget):

    def __init__(self, qcolor_button):
        super().__init__()
        self.qcolor_button = qcolor_button

    def get_widget(self):
        return self.qcolor_button

    def get_value(self):
        return self.qcolor_button.get_color()

    def set_value(self, val):
        return self.qcolor_button.set_color(val)
