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

    def __init__(self, window, susapad):
        super().__init__("", None)
        self.setFixedSize(100, 30)

        self.window = window
        self.susapad = susapad

        self.clicked.connect(self.toggle)
        self.setCursor(Qt.PointingHandCursor)

        self.style = _TOGGLE_STYLE

    # Template functions

    def command_on(self) -> bool:
        pass

    def command_off(self) -> bool:
        pass

    # Internal functions

    def __reload_style(self):
        self.setStyleSheet(self.style)

    def turn_on(self):
        if self.command_on():
            self.setAccessibleName("on")
            self.setText("Desligar")
            self.__reload_style()
        else:
            self.__error()

    def turn_off(self):
        if self.command_off():
            self.setAccessibleName("off")
            self.setText("Ligar")
            self.__reload_style()
        else:
            self.__error()

    def __error(self):
        exception.susapad_not_found(self.window, self.language["error"]["not-found"])
        exception.close_current_window(self.window)


    @QtCore.Slot()
    def toggle(self):
        if "on" == self.accessibleName():
            self.turn_off()
        else:
            self.turn_on()
