from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Qt

from susapad.controller import exception


def in_mm(value: int) -> str:
    return f"{value/100}mm"

class PressSensibilitySlider(QtWidgets.QSlider):

    def __init__(self, window, susapad, forms):
        super().__init__()

        self.susapad = susapad
        self.forms = forms
        self.window = window

        self.setMinimumWidth(330)
        self.setMinimum(10)
        self.setMaximum(400)
        self.setOrientation(Qt.Horizontal)

        self.sliderReleased.connect(self.action)
        self.valueChanged.connect(self.update_label)

    @QtCore.Slot()
    def action(self):
        if not self.susapad.set_press_sensibility(self.value()):
            exception.susapad_not_found(self.window)
            exception.close_current_window(self.window)

    @QtCore.Slot()
    def update_label(self):
        press = in_mm(self.value())
        release = in_mm(self.forms.sensibility_slider_release.value())
        self.forms.sensibility_label.setText(
            f"Sensibilidade: Pressionar ({press}) e Soltar ({release})"
        )


class ReleaseSensibilitySlider(QtWidgets.QSlider):

    def __init__(self, window, susapad, forms):
        super().__init__()

        self.susapad = susapad
        self.forms = forms
        self.window = window

        self.setMinimumWidth(330)
        self.setMinimum(10)
        self.setMaximum(400)
        self.setOrientation(Qt.Horizontal)

        self.sliderReleased.connect(self.action)
        self.valueChanged.connect(self.update_label)

    @QtCore.Slot()
    def action(self):
        if not self.susapad.set_release_sensibility(self.value()):
            exception.susapad_not_found(self.window)
            exception.close_current_window(self.window)

    @QtCore.Slot()
    def update_label(self):
        release = in_mm(self.value())
        press = in_mm(self.forms.sensibility_slider_press.value())
        self.forms.sensibility_label.setText(
            f"Sensibilidade: Pressionar ({press}) e Soltar ({release})"
        )
