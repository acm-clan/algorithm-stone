from abc import ABC, abstractmethod

# pylint: disable=too-few-public-methods
class InputWidget(ABC):

    def __init__(self):
        super()

    @abstractmethod
    def get_widget(self):
        pass

    @abstractmethod
    def get_value(self):
        pass

    @abstractmethod
    def set_value(self, val):
        pass

    def read_only(self):
        return self.get_widget().setEnabled(False)
