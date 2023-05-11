
from susapad import base_widgets


class CloseButton(base_widgets.BaseButton):

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


class AlertFrame(base_widgets.BaseFrame):

    def __init__(self, dialog, parent, message: str):
        super().__init__()


        self.dialog = dialog
        self.parent = parent

        self.close = CloseButton(self.dialog, self.parent)
        self.label = QtWidgets.QLabel(message)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.close)
