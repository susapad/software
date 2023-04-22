from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import Qt


class BaseButton(QtWidgets.QPushButton):

    def __init__(self, text: str, shortcut: [str | None]):
        super().__init__(text)
        self._init_style()
        if shortcut:
            self.setShortcut(shortcut)

    def _init_style(self):
        self.setFixedSize(100, 40)
        self.setStyleSheet(
            """
                background-color: #0e639e;
                border-radius: 15px;
                min-width: 10em;
                padding: 6px;
                font: bold;
                color: white;
            """
        )

    def change_background(self, color: str):
        result = self.styleSheet().replace(
            "background-color: #0e639e", 
            f"background-color: {color}", 
            1
        )
        self.setStyleSheet(result)


class ActionButton(BaseButton):

    def __init__(self, window):
        super().__init__("Conectar", "Enter")
        self.set_found(window.susapad.serial)
        self.clicked.connect(window.connect_to_susapad)

    def set_found(self, found: bool = True):
        if found:
            self.setText("Configurar")
        else:
            self.setText("Tentar novamente!")


class CloseButton(BaseButton):

    def __init__(self):
        super().__init__("Fechar", "Escape")
        self.change_background("#b71970")
        self.clicked.connect(self.close_application)

    @QtCore.Slot()
    def close_application(self):
        QtCore.QCoreApplication.instance().quit()
