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

        # Configuring Sliders
        self.slider.sliderReleased.connect(self._update_susapad)
        self.slider.valueChanged.connect(self._update_label) 

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


class BaseDualSliderGroup(QtWidgets.QWidget):

    def __init__(self, window, susapad):
        super().__init__()

        self.window = window
        self.susapad = susapad

        self.template: Template = Template("")

        self.title = QtWidgets.QLabel()
        self.slider1 = BaseSlider(self, self.window, self.susapad)
        self.slider2 = BaseSlider(self, self.window, self.susapad)
        self.min1 = QtWidgets.QLabel()
        self.max1 = QtWidgets.QLabel()
        self.min2 = QtWidgets.QLabel()
        self.max2 = QtWidgets.QLabel()

        # Configuring layout

        self.slider1_group = QtWidgets.QWidget()
        self.slider1_layout = QtWidgets.QHBoxLayout(self.slider1_group)
        self.slider1_layout.addWidget(self.min1)
        self.slider1_layout.addWidget(self.slider1, alignment = Qt.AlignBaseline)
        self.slider1_layout.addWidget(self.max1)

        self.slider2_group = QtWidgets.QWidget()
        self.slider2_layout = QtWidgets.QHBoxLayout(self.slider2_group)
        self.slider2_layout.addWidget(self.min2)
        self.slider2_layout.addWidget(self.slider2, alignment = Qt.AlignBaseline)
        self.slider2_layout.addWidget(self.max2)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.title)
        self.layout.addWidget(self.slider1_group)
        self.layout.addWidget(self.slider2_group)

        # Configuring sliders
        self.slider1.sliderReleased.connect(self._update_susapad_slider1)
        self.slider2.sliderReleased.connect(self._update_susapad_slider2)
        self.slider1.valueChanged.connect(self._update_label) 
        self.slider2.valueChanged.connect(self._update_label) 

    # Template function

    def update_susapad_slider1(self, value: int) -> bool:
        pass

    def update_susapad_slider2(self, value: int) -> bool:
        pass


    # Obrigatory use

    def set_range(self, value: tuple[int, int]):
        assert value[0] < value[1]
        self.slider1.setMinimum(value[0])
        self.slider1.setMaximum(value[1])
        self.slider2.setMinimum(value[0])
        self.slider2.setMaximum(value[1])
        self.min1.setText(self.__in_mm(value[0]))
        self.max1.setText(self.__in_mm(value[1]))
        self.min2.setText(self.__in_mm(value[0]))
        self.max2.setText(self.__in_mm(value[1]))

    def set_template(self, template: Template):
        self.template = template


    # Internal functions

    @staticmethod
    def __in_mm(value: int) -> str:
        return f"{value/100}mm"

    @QtCore.Slot()
    def _update_label(self):
        template = self.template.substitute(
            value1 = self.__in_mm(self.slider1.value()),
            value2 = self.__in_mm(self.slider2.value()))
        self.title.setText(template)

    @QtCore.Slot()
    def _update_susapad_slider1(self):
        if not self.update_susapad_slider1(self.slider1.value()):
            exception.susapad_not_found(self.window)
            exception.close_current_window(self.window)

    @QtCore.Slot()
    def _update_susapad_slider2(self):
        if not self.update_susapad_slider2(self.slider2.value()):
            exception.susapad_not_found(self.window)
            exception.close_current_window(self.window)
