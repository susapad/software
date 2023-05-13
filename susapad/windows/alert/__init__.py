
from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import Qt

from susapad import base_widgets as base


class CloseButton(base.BaseButton):

    def __init__(self, dialog, parent):
        super().__init__("Ok", "Enter")

        self.dialog = dialog
        self.parent = parent

        self.setAccessibleName("secondary")
        self.clicked.connect(self.close_dialog)

    @QtCore.Slot()
    def close_dialog(self):
        self.parent.setEnabled(True)
        self.dialog.close()


class AlertFrame(base.BaseFrame):

    def __init__(self, dialog, parent, message: str):
        super().__init__()

        self.dialog = dialog
        self.parent = parent

        self.close = CloseButton(self.dialog, self.parent)
        self.label = QtWidgets.QLabel(message)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.close)


class AlertDialog(base.BaseWindow):

    def __init__(self, parent, message: str, susapad = None):
        super().__init__(susapad)

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

        self.parent = parent
        self.message = message

        ## Configure Layout
        self.main_widget = AlertFrame(self, self.parent, self.message)
        self.layout.addWidget(self.main_widget)
