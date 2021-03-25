from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

from algomanim.empty_animation import is_empty_anim
from gui.panels.base_changes_panel import BaseChangesPanel

from gui.anim_utils import format_anim_block_str, format_customise_name
from .widgets.frame_layout import FrameLayout
from .widgets.input_text_box import InputTextBox
from .customisation_type import CustomisationType


OPTION_HEIGHT = 35


# pylint: disable=too-few-public-methods,too-many-instance-attributes
class CustomisePanel(BaseChangesPanel):

    def __init__(self, parent=None, changes=None):
        super().__init__(parent)
        self.custom_menu = QVBoxLayout()

        # Title
        self.title_lbl = QLabel("Please click on an animation to customize")
        self.title_lbl.setAlignment(Qt.AlignHCenter)

        # Scroll Area for form elements
        self.inner_scroll_area = QScrollArea()
        self.inner_scroll_area.setStyleSheet("border: none")
        self.inner_scroll_widget = QWidget()
        self.inner_scroll_layout = QVBoxLayout()
        self.inner_scroll_widget.setLayout(self.inner_scroll_layout)
        self.inner_scroll_area.setWidgetResizable(True)
        self.inner_scroll_area.setWidget(self.inner_scroll_widget)

        # global variables to save changes and change form elements
        self.menu_frame = None
        self.menu_layout = None
        self.change_widgets = None
        self.changes = changes
        self.insertion_widgets = None

        # global variables to do multi-block edit (this only works for total duration)
        self.multi_block_anims = None
        self.multi_block_widget = None
        self.multi_block_default_value = None

        self.save_button = QPushButton("Save changes")
        self.save_button.clicked.connect(self.save_changes)

        self.custom_menu.addWidget(self.title_lbl)
        self.custom_menu.addWidget(self.inner_scroll_area)
        self.custom_menu.addWidget(self.save_button, alignment=Qt.AlignBottom)
        self.scroll_area.setLayout(self.custom_menu)

    def save_changes(self):
        # save changes for customisations
        if self.multi_block_anims is None:
            for (action_pair_index, change_name, change_type), (change_widget, default_val) \
                    in self.change_widgets.items():
                if default_val != change_widget.get_value():
                    self.gui_window.add_change(
                        action_pair_index,
                        change_name,
                        change_type,
                        change_widget.get_value()
                    )
            # save changes for inserted animations
            self.gui_window.insert_animations({
                index: {
                    anim_type: widget.text()
                    for anim_type, widget in widgets.items()
                }
                for index, widgets in self.insertion_widgets.items()
            })
        else:
            old_duration = float(self.multi_block_default_value)
            new_duration = float(self.multi_block_widget.get_value())

            if old_duration != new_duration:
                for anim_meta_block in self.multi_block_anims:
                    for lower_meta in anim_meta_block.metadata.children:
                        action_pair = lower_meta.action_pair
                        frac_of_duration = action_pair.get_runtime_val() / old_duration
                        action_pair_index = action_pair.get_index()
                        lower_meta_name = lower_meta.meta_name
                        change_name = f'{anim_meta_block.desc(sep=" ")} > {lower_meta_name}'
                        change_type = CustomisationType.RUNTIME
                        change_value = frac_of_duration * new_duration
                        self.gui_window.add_change(
                            action_pair_index,
                            change_name,
                            change_type,
                            change_value
                        )

    def reset_frame(self, title):
        # set title
        self.title_lbl.setText(title)

        # discard old frame and reset change_widgets
        self.change_widgets = dict()
        self.insertion_widgets = dict()
        if self.menu_frame is not None:
            self.menu_frame.setParent(None)

        # initialize new frame
        self.menu_frame = QWidget()

        self.menu_layout = QVBoxLayout()
        self.menu_layout.setSpacing(0)
        self.menu_layout.setContentsMargins(0, 0, 0, 0)
        self.menu_layout.setAlignment(Qt.AlignTop)

        self.menu_frame.setLayout(self.menu_layout)

    # PRE: anims should not contain empty_animations or else this will break
    def set_animation_group(self, anims):
        contains_empty_anim = any([is_empty_anim(anim) for anim in anims])
        if contains_empty_anim:
            return

        self.multi_block_anims = anims
        change_possible = any([anim_meta_block.can_set_runtime() for anim_meta_block in anims])
        total_duration = sum([anim.runtime for anim in anims])
        self.reset_frame(title = f'{anims[0].desc(sep=" ")} \n to {anims[-1].desc(sep=" ")}')
        widget = QLineEdit()
        wrapped_widget = InputTextBox(widget)
        wrapped_widget.set_value(total_duration)
        self.multi_block_default_value = wrapped_widget.get_value()
        self.multi_block_widget = wrapped_widget

        form_layout = QFormLayout()
        form_layout.addRow(QLabel('Total Duration'), widget)

        self.save_button.setEnabled(change_possible)
        self.menu_layout.addLayout(form_layout)
        self.inner_scroll_layout.addWidget(self.menu_frame)

    def set_animation(self, anim):
        self.multi_block_anims = None
        if is_empty_anim(anim):
            self.set_empty_animation(anim)
        else:
            self.set_nonempty_animation(anim)

    def set_empty_animation(self, empty_anim):
        self.reset_frame(title="custom")
        insertion_dict = dict()
        self.insertion_widgets[empty_anim.index] = insertion_dict

        collapsible_box = FrameLayout(title="Text animations")
        form_layout = QFormLayout()
        collapsible_box.addLayout(form_layout)

        # Add text section
        add_text_widget = QLineEdit()
        form_layout.addRow(QLabel("Add Text"), add_text_widget)
        insertion_dict['slide'] = add_text_widget

        self.menu_layout.addWidget(collapsible_box)

        collapsible_box = FrameLayout(title="Others")
        form_layout = QFormLayout()
        collapsible_box.addLayout(form_layout)
        # Add wait section
        add_wait_widget = QLineEdit()
        form_layout.addRow(QLabel("Add Pause (s)"), add_wait_widget)
        insertion_dict['wait'] = add_wait_widget

        self.menu_layout.addWidget(collapsible_box)
        self.save_button.setEnabled(True)
        self.inner_scroll_layout.addWidget(self.menu_frame)

    def set_nonempty_animation(self, anim_meta_block):  # pylint: disable=too-many-locals
        self.reset_frame(title=format_anim_block_str(anim_meta_block))

        change_possible = False
        for lower_meta in anim_meta_block.metadata.children:
            if not lower_meta.show_in_panel:
                # do not display this customisation
                continue

            action_pair = lower_meta.action_pair
            action_pair_index = action_pair.get_index()
            lower_meta_name = format_customise_name(lower_meta)
            change_name = f'{anim_meta_block.desc(sep=" ")} > {lower_meta_name}'

            collapsible_box = FrameLayout(title=lower_meta_name)
            form_layout = QFormLayout()

            # for each customization available in action_pair
            for (change_type, original_val) in action_pair.customizations().items():
                change_possible = True

                # create input widget and set default value to last changed value
                # or original value
                widget = change_type.get_widget()
                wrapped_widget = change_type.wrap_input_widget(widget)
                change_key = (action_pair_index, change_type)
                if change_key in self.changes:
                    wrapped_widget.set_value(self.changes[change_key].get_value())
                else:
                    wrapped_widget.set_value(original_val)

                form_layout.addRow(QLabel(change_type.desc), widget)

                widget_key = (action_pair_index, change_name, change_type)
                self.change_widgets[widget_key] = wrapped_widget, wrapped_widget.get_value()

            collapsible_box.addLayout(form_layout)
            self.menu_layout.addWidget(collapsible_box)

        self.save_button.setEnabled(change_possible)
        self.inner_scroll_layout.addWidget(self.menu_frame)
