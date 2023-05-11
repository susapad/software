
from susapad import base_widgets


class AlertUI(base_widgets.BaseFrame):

    def __init__(self, dialog, message: str):
        super().__init__()
        self.dialog = dialog

        self.init_widgets(message)
        self.init_layout()

    def init_close_button(self) -> base_widgets.BaseButton:
        button = base_widgets.BaseButton("Ok", "Enter")
        button.setAccessibleName("secondary")
        button.clicked.connect(self.dialog.close_dialog)
        return button

    def init_widgets(self)
        self.close_button = self.init_close_button()
        self.content = QtWidgets.QLabel(message)

    def init_layout(self):
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.close)