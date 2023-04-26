from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Qt



class LowerActuationSlider(QtWidgets.QSlider):

    def __init__(self, window, susapad, forms):
        super().__init__()

        self.susapad = susapad

        self.setMinimum(10)
        self.setMaximum(400)
        self.setOrientation(Qt.Horizontal)
        self.setMinimumWidth(400)


        self.sliderReleased.connect(self.action)

    @QtCore.Slot()
    def action(self):
        self.susapad.set_actuation_point_lower(self.value())
        self.forms.actuation_slider_upper.setMinimum(self.value())


class UpperActuationSlider(QtWidgets.QSlider):

    def __init__(self, window, susapad, forms):
        super().__init__()

        self.susapad = susapad
        self.forms = forms

        self.setMinimum(10)
        self.setMaximum(400)
        self.setOrientation(Qt.Horizontal)
        self.setMinimumWidth(400)

        self.sliderReleased.connect(self.action)

    @QtCore.Slot()
    def action(self):
        self.susapad.set_actuation_point_upper(self.value())
        self.forms.actuation_slider_lower.setMaximum(self.value())
