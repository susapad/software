
from susapad import base_widgets


class AlertUI(base_widgets.BaseFrame):

    def __init__(self, dialog, caller, message: str):
        super().__init__()
        self.message = message
        self.dialog = dialog
        self.caller = caller

        self.init_widgets()
        self.init_layout()

    def init_close_button(self) -> base_widgets.BaseButton:
        button = base_widgets.BaseButton("Ok", "Enter")
        button.setAccessibleName("secondary")
        button.clicked.connect(self.close_dialog)
        return button

    def init_widgets(self)
        self.close_button = self.init_close_button()
        self.content = QtWidgets.QLabel(self.message)

    def init_layout(self):
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.close)


    @QtCore.Slot()
    def close_dialog(self):
        self.caller.setEnabled(True)
        self.dialog.close()
