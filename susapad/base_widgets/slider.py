from string import Template

from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import Qt

from susapad.controller import exception

_SLIDER_STYLE = """
    QSlider::groove:horizontal {
        height: 16px;
        background-color: #090909;
        border-radius: 8px;
    }

    QSlider::handle {
        background-color: #b71970;
        width: 16px;
        height: 16px;
        border-radius: 8px;
    }

    QSlider::handle:hover {
        background-color: #dd1e87;
    }
"""


class BaseSlider(QtWidgets.QSlider):

    def __init__(self, group, window, susapad):
        super().__init__()

        self.group = group
        self.susapad = susapad
        self.window = window

        self.setOrientation(Qt.Horizontal)
        self.setMinimumWidth(330)
        self.setStyleSheet(_SLIDER_STYLE)

        self.sliderReleased.connect(self.group._update_susapad)
        self.valueChanged.connect(self.group._update_label) 


class BaseSliderGroup(QtWidgets.QWidget):

    def __init__(self, window, susapad):
        super().__init__()
        
        self.window = window
        self.susapad = susapad

        self.template: Template = Template("")

        self.title = QtWidgets.QLabel()
        self.slider = BaseSlider(self, self.window, self.susapad)
        self.min = QtWidgets.QLabel()
        self.max = QtWidgets.QLabel()

        # Configuring layout

        self.bottom = QtWidgets.QWidget()
        self.bottom_layout = QtWidgets.QHBoxLayout(self.bottom)
        self.bottom_layout.addWidget(self.min)
        self.bottom_layout.addWidget(self.slider, alignment = Qt.AlignBaseline)
        self.bottom_layout.addWidget(self.max)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.title)
        self.layout.addWidget(self.bottom)

    # Template function

    def update_susapad(self, value: int) -> bool:
        pass


    # Obrigatory use

    def set_range(self, value: tuple[int, int]):
        assert value[0] < value[1]
        self.slider.setMinimum(value[0])
        self.slider.setMaximum(value[1])
        self.min.setText(self.__in_mm(value[0]))
        self.max.setText(self.__in_mm(value[1]))

    def set_template(self, template: Template):
        self.template = template


    # Internal functions

    @staticmethod
    def __in_mm(value: int) -> str:
        return f"{value/100}mm"

    @QtCore.Slot()
    def _update_label(self):
        template = self.template.substitute(
            value = self.__in_mm(self.slider.value()))
        self.title.setText(template)

    @QtCore.Slot()
    def _update_susapad(self):
        if not self.update_susapad(self.slider.value()):
            exception.susapad_not_found(self.window)
            exception.close_current_window(self.window)


