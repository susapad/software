
from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import Qt

from susapad import base_widgets as base

from . import ui


_DEFAULT_MESSAGE = """SusaPad não encontrado.
Certifique-se que ele está conectado corretamente
"""


class AlertDialog(base.BaseWindow):

    def __init__(self, parent, message: str = None, susapad = None):
        super().__init__(susapad)

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

        self.parent = parent
        self.message = message if message else _DEFAULT_MESSAGE

        ## Configure Layout
        self.main_widget = ui.AlertUI(self, self.parent, self.message)
        self.layout.addWidget(self.main_widget)
