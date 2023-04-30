

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

        self.width = 60
        self.height = 16
        self.margin = 20

        self.setAccessibleName("floating")
        self.clicked.connect(self.action)
        self.setStyleSheet(_FLOATING_STYLE)
        self._set_position()

    def action(self):
        pass

    def _set_position(self):
        self.setGeometry(
            self.window.width() - self.width - self.margin,
            self.margin,
            self.width,
            self.height
        )
