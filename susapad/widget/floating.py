from __feature__ import true_property
from __feature__ import snake_case

from . import button as base


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

    def __init__(self, window, text, shortcut: str = None):
        super().__init__(text, parent=window, shortcut=shortcut)

        self.window = window

        self.accessible_name = "floating"
        self.clicked.connect(self.action)
        self.style_sheet = _FLOATING_STYLE

    def action(self):
        pass
