from gui.panels.widgets.input_widget import InputWidget

# pylint: disable=too-few-public-methods
class InputCheckBox(InputWidget):

    def __init__(self, qcheck_box):
        super().__init__()
        self.qcheck_box = qcheck_box

    def get_widget(self):
        return self.qcheck_box

    def get_value(self):
        return self.qcheck_box.isChecked()

    def set_value(self, val):
        return self.qcheck_box.setChecked(bool(val))
