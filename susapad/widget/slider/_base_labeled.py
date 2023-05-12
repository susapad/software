from __feature__ import true_property
from __feature__ import snake_case

from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import Qt

from susapad.controller import exception

from . import _group_qss, _slider

class BaseLabeledSlider(QtWidgets.QWidget):

    def __init__(self, vertical: bool = False):
        super().__init__()
        self.vertical = vertical

        self._init_configuration()
        self._init_widgets()
        self._init_layout()

    def _init_widgets(self):
        self.slider = _slider.BaseSlider(self.vertical)
        self.min = QtWidgets.QLabel()
        self.max = QtWidgets.QLabel()

    def _init_layout(self):
        alignment, layout = \
            (Qt.AlignHCenter, QtWidgets.QVBoxLayout(self)) if self.vertical else  \
            (Qt.AlignVCenter, QtWidgets.QHBoxLayout(self))

        layout.add_widget(self.min,    alignment = alignment)
        layout.add_widget(self.slider, alignment = alignment)
        layout.add_widget(self.max,    alignment = alignment)
        layout.contents_margins = QtCore.QMargins(10, 5, 10, 5)
        layout.alignment        = alignment

    def _init_configuration(self):
        self.style_sheet = _group_qss.GROUP_STYLE

    def __configure_widgets(self):
        self.min.accessible_name = "side"
        self.max.accessible_name = "side"
