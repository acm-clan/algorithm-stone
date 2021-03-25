from gui.panels.widgets.input_widget import InputWidget

class InputDropdown(InputWidget):

    def __init__(self, qcombobox):
        super().__init__()
        self.qcombobox = qcombobox

    def get_widget(self):
        return self.qcombobox

    def get_value(self):
        return self.qcombobox.currentText()

    def set_value(self, val):
        return self.qcombobox.setCurrentText(str(val))
