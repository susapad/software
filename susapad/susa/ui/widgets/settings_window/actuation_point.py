from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Qt



class LowerActuationSlider(QtWidgets.QSlider):

    def __init__(self, window, susapad, forms):
        super().__init__()

        self.susapad = susapad
        self.forms = forms

        self.setMinimum(10)
        self.setMaximum(400)
        self.setOrientation(Qt.Horizontal)
        self.setMinimumWidth(330)


        self.sliderReleased.connect(self.action)
        self.valueChanged.connect(self.update_label)

    @QtCore.Slot()
    def action(self):
        self.susapad.set_actuation_point_lower(self.value())
        self.forms.actuation_slider_upper.setMinimum(self.value())

    @QtCore.Slot()
    def update_label(self):
        self.forms.actuation_label.setText(
            f"Pontos de Ativação: Mínimo ({self.value()}) e Máximo ({self.forms.actuation_slider_upper.value()})"
        )


class UpperActuationSlider(QtWidgets.QSlider):

    def __init__(self, window, susapad, forms):
        super().__init__()

        self.susapad = susapad
        self.forms = forms

        self.setMinimum(10)
        self.setMaximum(400)
        self.setOrientation(Qt.Horizontal)
        self.setMinimumWidth(330)

        self.sliderReleased.connect(self.action)
        self.valueChanged.connect(self.update_label)

    @QtCore.Slot()
    def action(self):
        self.susapad.set_actuation_point_upper(self.value())
        self.forms.actuation_slider_lower.setMaximum(self.value())

    @QtCore.Slot()
    def update_label(self):
        self.forms.actuation_label.setText(
            f"Pontos de Ativação: Mínimo ({self.forms.actuation_slider_lower.value()}) e Máximo ({self.value()})"
        )
