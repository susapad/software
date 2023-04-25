from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Qt



class PressSensibilitySlider(QtWidgets.QSlider):

    def __init__(self, window, susapad):
        super().__init__()

        self.susapad = susapad

        self.setMinimumWidth(400)
        self.setMinimum(10)
        self.setMaximum(400)
        self.setOrientation(Qt.Horizontal)

        self.sliderReleased.connect(self.action)

    @QtCore.Slot()
    def action(self):
        self.susapad.set_press_sensibility(self.value)


class ReleaseSensibilitySlider(QtWidgets.QSlider):

    def __init__(self, window, susapad):
        super().__init__()

        self.susapad = susapad

        self.setMinimumWidth(400)
        self.setMinimum(10)
        self.setMaximum(400)
        self.setOrientation(Qt.Horizontal)

        self.sliderReleased.connect(self.action)

    @QtCore.Slot()
    def action(self):
        self.susapad.set_release_sensibility(self.value)
