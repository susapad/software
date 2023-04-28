from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Qt

from susapad.susa.ui import alert_dialog


class ActuationSlider(QtWidgets.QSlider):

    def __init__(self, window, susapad, forms):
        super().__init__()

        self.susapad = susapad
        self.forms = forms
        self.window = window

        self.setMinimum(10)
        self.setMaximum(390)
        self.setOrientation(Qt.Horizontal)
        self.setMinimumWidth(330)


        self.sliderReleased.connect(self.action)
        self.valueChanged.connect(self.update_label)

    def __raise_alert(self):
        alert = alert_dialog.AlertDialog(self.window)
        alert.show()
        self.window.close()

    @staticmethod
    def reverse(value: int) -> int:
        if 190 == value:
            return 190
        else:
            return 400 - value

    @staticmethod
    def in_mm(value: int) -> str:
        return f"{value/100}mm"

    @QtCore.Slot()
    def action(self):
        if not self.susapad.set_actuation_point(self.reverse(self.value())):
            self.__raise_alert()

    @QtCore.Slot()
    def update_label(self):
        value = self.in_mm(self.reverse(self.value()))
        self.forms.actuation_label.setText(
            f"Ponto de Atuação: ({value})"
        )
