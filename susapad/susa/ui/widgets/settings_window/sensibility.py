from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Qt



class PressSensibilitySlider(QtWidgets.QSlider):

    def __init__(self, window, susapad, forms):
        super().__init__()

        self.susapad = susapad
        self.forms = forms

        self.setMinimumWidth(330)
        self.setMinimum(10)
        self.setMaximum(400)
        self.setOrientation(Qt.Horizontal)

        self.sliderReleased.connect(self.action)
        self.valueChanged.connect(self.update_label)

    @QtCore.Slot()
    def action(self):
        self.susapad.set_press_sensibility(self.value())

    @QtCore.Slot()
    def update_label(self):
        self.forms.sensibility_label.setText(
            f"Sensibilidade: Pressionar ({self.value()}) e Soltar ({self.forms.sensibility_slider_release.value()})"
        )


class ReleaseSensibilitySlider(QtWidgets.QSlider):

    def __init__(self, window, susapad, forms):
        super().__init__()

        self.susapad = susapad
        self.forms = forms

        self.setMinimumWidth(330)
        self.setMinimum(10)
        self.setMaximum(400)
        self.setOrientation(Qt.Horizontal)

        self.sliderReleased.connect(self.action)
        self.valueChanged.connect(self.update_label)

    @QtCore.Slot()
    def action(self):
        self.susapad.set_release_sensibility(self.value())

    @QtCore.Slot()
    def update_label(self):
        self.forms.sensibility_label.setText(
            f"Sensibilidade: Pressionar ({self.forms.sensibility_slider_press.value()}) e Soltar ({self.value()})"
        )
