from __feature__ import true_property
from __feature__ import snake_case

from PySide6 import QtCore

from susapad import widget


class SensiblitySlidersGroup(widget.DoubleSlider):

    def __init__(self, window, susapad):
        super().__init__(
            template =
                "Sensibilidade: Pressionar (${value1}) e Soltar (${value2})",
                range = (10, 400))

        self.susapad = susapad

        self.group1.slider.sliderReleased.connect(self.update_susapad_press)
        self.group2.slider.sliderReleased.connect(self.update_susapad_release)

        self.update_label()

    @QtCore.Slot()
    def update_susapad_press(self):
        if self.susapad.set_press_sensibility(self.group1.slider.value):
            self.update_label()
        else:
            self.error()

    @QtCore.Slot()
    def update_susapad_release(self):
        if self.susapad.set_release_sensibility(self.group2.slider.value):
            self.update_label()
        else:
            self.error()
