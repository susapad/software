from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import Qt


class BaseButton(QtWidgets.QPushButton):

    def __init__(self, text: str, shortcut: str):
        super().__init__(text)
        self.setShortcut(shortcut)
        self._init_style()

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


class ConnectButton(BaseButton):

    def __init__(self, window):
        super().__init__("Conectar", "Enter")
        self.clicked.connect(self.connect_to_susapad)

    @QtCore.Slot()
    def connect_to_susapad(self, window):
        pass


class SettingsButton(BaseButton):

    def __init__(self, window):
        super().__init__("Configurar", "Ctrl + P")
        self.clicked.connect(self.open_settings)

    @QtCore.Slot()
    def open_settings(self, window):
        pass



class CloseButton(BaseButton):

    def __init__(self, window):
        super().__init__("Fechar", "Escape")
        self.clicked.connect(self.close_application)
        self.change_background("#b71970")

    @QtCore.Slot()
    def close_application(self, window):
        QtCore.QCoreApplication.instance().quit()
