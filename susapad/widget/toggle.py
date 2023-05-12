from __feature__ import true_property
from __feature__ import snake_case

from PySide6 import QtCore
from PySide6.QtCore import Qt


from susapad.controller import exception
from . import button as base


_TOGGLE_STYLE = """
        QPushButton {
                background-color: #0e639e;
                border-radius: 15px;
                min-width: 10em;
                padding: 6px;
                font: bold;
                color: white;
        }

        QPushButton:hover {
            background-color: #127ecb;
        }

        QPushButton[accessibleName="off"] {
                background-color: #b71970;
        }

        QPushButton:hover[accessibleName="off"] {
            background-color: #dd1e87;
        }
    """


class BaseToggleButton(base.BaseButton):

    def __init__(self):
        super().__init__()

        self.set_fixed_size(100, 30)
        self.text = ""
        self.shortcut = None
        self.cursor = Qt.PointingHandCursor

    # Template functions

    @QtCore.Slot()
    def turn_on(self):
        pass

    @QtCore.Slot()
    def turn_off(self):
        pass

    # Internal functions

    def reload_style(self):
        self.style_sheet = _TOGGLE_STYLE

    def error(self):
        exception.susapad_not_found(self.window)
        exception.close_current_window(self.window)

    @QtCore.Slot()
    def toggle(self):
        if "on" == self.accessible_name:
            self.turn_off()
        else:
            self.turn_on()
