from __feature__ import true_property
from __feature__ import snake_case

from PySide6 import QtWidgets

from susapad import widget


class AlertUI(widget.BaseFrame):

    def __init__(self, dialog, message: str):
        super().__init__()
        self.dialog = dialog

        self.init_widgets(message)
        self.init_layout()

    def init_close_button(self) -> widget.BaseButton:
        button = widget.BaseButton("Ok", "Enter")
        button.accessible_name = "secondary"
        button.clicked.connect(self.dialog.close_dialog)
        return button

    def init_widgets(self, message):
        self.close_button = self.init_close_button()
        self.content = QtWidgets.QLabel(message)

    def init_layout(self):
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.add_widget(self.content)
        self.layout.add_widget(self.close_button)
