from __feature__ import true_property
from __feature__ import snake_case

from string import Template

from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Qt

from susapad.controller import exception
from susapad import widget


class SensiblitySlidersGroup(widget.BaseDualSliderGroup):

    def __init__(self, window, susapad):
        super().__init__(window, susapad)

        self.set_template(Template(
            "Sensibilidade: Pressionar (${value1}) e Soltar (${value2})"))
        self.range = (10, 400)
        self._update_label()

    @QtCore.Slot() # press
    def update_susapad_slider1(self, value: int) -> bool:
        return self.susapad.set_press_sensibility(value)

    @QtCore.Slot() # release
    def update_susapad_slider2(self, value: int) -> bool:
        return self.susapad.set_release_sensibility(value)
