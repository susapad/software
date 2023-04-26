
from PySide6 import QtWidgets
from PySide6.QtCore import Qt


class BaseButton(QtWidgets.QPushButton):

    def __init__(self, text: str, shortcut: [str | None]):
        super().__init__(text)
        self._init_style()
        if shortcut:
            self.setShortcut(shortcut)
            self.setCursor(Qt.PointingHandCursor)

    def _init_style(self):
        self.setFixedSize(100, 40)
        self.setStyleSheet(
            """
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
        )
