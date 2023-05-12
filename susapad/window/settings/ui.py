from __feature__ import true_property
from __feature__ import snake_case

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt

from susapad import widget
from .component import actuation_point, rapid_trigger as rt, sensibility

_SETTINGS_STYLE = """
    QLabel {
        color: white;
        font: 16px;
        margin-top: 20px;
        margin-bottom: 10px;
    }

    QLabel#first-h2 {
        margin-top: 0px;
    }

    QPushButton {
        margin-left: 20px;
    }
"""


class SettingsUI(widget.BaseFrame):

    def __init__(self, window, susapad):
        super().__init__()

        # Configure Style
        self.style_sheet += _SETTINGS_STYLE
        self.init_widgets(window, susapad)
        self.init_layout()

    def init_widgets(self, window, susapad):
        self.input_label = QtWidgets.QLabel("Habilitar Input")
        self.input_label.object_name = "first-h2"
        self.input_button = rt.TriggerButton(window, susapad)

        self.rt_label = QtWidgets.QLabel("Rapid Trigger")
        self.rt_button = rt.RapidTriggerButton(window, susapad)

        self.crt_label = QtWidgets.QLabel("Rapid Trigger Contínuo")
        self.crt_button = rt.ContinuousRapidTriggerButton(window, susapad)

        self.actuation_slider = actuation_point.ActuationPointGroup(susapad)

        self.sensibility_slider = sensibility.SensiblitySlidersGroup(window, susapad)

    def init_layout(self):
        layout = QtWidgets.QVBoxLayout(self)
        layout.add_layout(self.__init_upper_layout())
        layout.add_widget(self.sensibility_slider)

    def __init_upper_layout(self):

        left_layout = QtWidgets.QVBoxLayout()
        left_layout.add_widget(self.input_label)
        left_layout.add_widget(self.input_button)
        left_layout.add_widget(self.rt_label)
        left_layout.add_widget(self.rt_button)
        left_layout.add_widget(self.crt_label)
        left_layout.add_widget(self.crt_button)

        right_layout = QtWidgets.QVBoxLayout()
        right_layout.add_widget(self.actuation_slider)

        upper_layout = QtWidgets.QHBoxLayout()
        upper_layout.add_layout(left_layout, 1)
        upper_layout.add_layout(right_layout, 1)

        return upper_layout
