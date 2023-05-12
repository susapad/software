from __feature__ import true_property
from __feature__ import snake_case

from . import button as base

from PySide6.QtWidgets import QWidget


_FLOATING_STYLE = """
    QPushButton[accessibleName="floating"] {
        background-color: #b71970;
        border-radius: 10px;
        min-width: 60px;
        max-width: 60px;
        font: bold;
        color: white;
    }

    QPushButton:hover[accessibleName="floating"] {
        background-color: #dd1e87;
    }
"""


class BaseFloatingButton(base.BaseButton):

    def __init__(
            self,
            window: QWidget,
            text: str = None,
            shortcut: str = None):
        super().__init__(text, parent=window)

        self.window: QWidget = window
        self.text: str = text
        self.shortcut = shortcut

        self.accessible_name: str = "floating"
        self.clicked.connect(self.action)
        self.style_sheet: str = _FLOATING_STYLE

    def action(self):
        pass
