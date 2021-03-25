# pylint: disable=too-few-public-methods
class AnimChange:

    def __init__(self, action_pair_index, change_name, change_type, change_value):
        self.action_pair_index = action_pair_index
        self.change_name = change_name
        self.change_type = change_type
        self.change_value = change_value

    def update_value(self, change_value):
        self.change_value = change_value

    def get_value(self):
        return self.change_value
