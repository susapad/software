
from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import Qt

from susapad import base_widgets as base

from . import ui


_DEFAULT_MESSAGE = """SusaPad não encontrado.
Certifique-se que ele está conectado corretamente
"""


class AlertDialog(base.BaseWindow):

    def __init__(self, caller, message: str = None, susapad = None):
        super().__init__(susapad)
        self.caller = caller
        self.message = message if message else _DEFAULT_MESSAGE

        self.init_proprieties()
        self.init_widgets()
        self.init_layout()

    def init_proprieties(self):
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

    def init_widgets(self):
        self.main_widget = ui.AlertUI(self, self.message)

    def init_layout(self):
        self.layout.addWidget(self.main_widget)

    @QtCore.Slot()
    def close_dialog(self):
        self.caller.setEnabled(True)
        self.close()
