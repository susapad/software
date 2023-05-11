from __feature__ import true_property
from __feature__ import snake_case

from PySide6 import QtWidgets
from PySide6.QtCore import Qt


_BUTTON_STYLE = """
    QPushButton {
        background-color: #0e639e;
        border-radius: 15px;
        height: 30px;
        padding: 6px;
        font: bold;
        color: white;
    }

    QPushButton:hover {
        background-color: #127ecb;
    }

    QPushButton:pressed {
        background-color: #0a4874;
    }

    QPushButton[accessibleName="secondary"] {
        background-color: #b71970;
    }

    QPushButton:hover[accessibleName="secondary"] {
        background-color: #dd1e87;
    }

    QPushButton:pressed[accessibleName="secondary"] {
        background-color: #861252;
    }
"""


class BaseButton(QtWidgets.QPushButton):

    def __init__(
            self,
            text: str = None,
            shortcut: str = None,
            parent: QtWidgets.QWidget = None
        ):

        super().__init__(text, parent)

        self.style_sheet: str = _BUTTON_STYLE
        self.cursor: Qt = Qt.PointingHandCursor

        if shortcut:
            self.shortcut = shortcut
