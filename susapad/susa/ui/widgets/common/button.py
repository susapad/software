
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
