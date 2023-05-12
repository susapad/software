from __feature__ import true_property
from __feature__ import snake_case

from PySide6 import QtWidgets
from PySide6.QtCore import Qt

from . import _slider_qss


class BaseSlider(QtWidgets.QSlider):

    def __init__(self, vertical: bool = False):
        super().__init__()
        self.style_sheet = _slider_qss.SLIDER_STYLE

        if vertical:
            self.orientation = Qt.Vertical
            self.minimum_height = 200
            self.minimum_width = 100
            self.inverted_appearance = True
        else:
            self.orientation = Qt.Horizontal
            self.minimum_width = 330
            self.minimum_height = 40
            self.minimum_width = 200

__all__ = ["BaseSlider"]
