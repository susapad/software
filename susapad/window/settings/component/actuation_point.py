from __feature__ import true_property
from __feature__ import snake_case

from string import Template

from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Qt

from susapad import widget
from susapad.controller import exception

class ActuationPointGroup(widget.SingleSlider):

    def __init__(self, susapad):
        super().__init__(
            template = "Ponto de atuação: (${value})",
            range = (10, 390),
            vertical = True)
        self.susapad = susapad
        self.group.slider.sliderReleased.connect(self.update_susapad)

        self.update_label()

    def update_susapad(self):
        if self.susapad.set_actuation_point(
            self.reverse(self.group.slider.value)):
            self.update_label()
        else:
            self.error()

    @staticmethod
    def reverse(value: int) -> int:
        if 190 == value:
            return 190
        else:
            return 400 - value
