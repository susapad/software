from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt

from . import actuation_point, togglers, sensibility


class FormsGroup(QtWidgets.QWidget):

    def __init__(self, window, susapad):
        super().__init__()

        self.first_h2 = QtWidgets.QLabel("Rapid Trigger")
        self.first_h2.setObjectName("first-h2")

        self.rt_button = togglers.RapidTriggerButton(window, susapad)
        self.crt_button = togglers.ContinuousRapidTriggerButton(window, susapad)

        self.sensibility_slider_press = sensibility.PressSensibilitySlider(window, susapad, self)
        self.sensibility_slider_release = sensibility.ReleaseSensibilitySlider(window, susapad, self)
        self.sensibility_label = QtWidgets.QLabel(
            f"Sensibilidade: Pressionar ({self.__get_press()}) e Soltar ({self.__get_release()})")
        
        self.actuation_slider = actuation_point.ActuationSlider(window, susapad, self)
        self.actuation_label = QtWidgets.QLabel(
            f"Ponto de Atuação: ({self.__get_actuation_point()})")

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.first_h2)
        self.layout.addWidget(self.rt_button)
        self.layout.addWidget(QtWidgets.QLabel("Rapid Trigger Contínuo"))
        self.layout.addWidget(self.crt_button)
        self.layout.addWidget(self.sensibility_label)
        self.layout.addWidget(self.sensibility_slider_press, alignment = Qt.AlignJustify)
        self.layout.addWidget(self.sensibility_slider_release, alignment = Qt.AlignJustify)
        self.layout.addWidget(self.actuation_label)
        self.layout.addWidget(self.actuation_slider, alignment = Qt.AlignJustify)


    def __get_actuation_point(self) -> str:
        value = self.actuation_slider.value()
        return self.actuation_slider.in_mm(value)

    def __get_press(self) -> str:
        return sensibility.in_mm(
            self.sensibility_slider_press.value()
        )

    def __get_release(self) -> str:
        return sensibility.in_mm(
            self.sensibility_slider_release.value()
        )



class WindowLayout(QtWidgets.QFrame):

    def __init__(self, window, susapad):
        super().__init__()

        self.setObjectName("background-frame")
        self.__init_style()

        self.forms = FormsGroup(window, susapad)
        
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.forms)


    def __init_style(self):
        self.setStyleSheet(
            """

            QFrame {
                border-radius: 20px;
                background-color: #121212;
            }

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

            QSlider::groove:horizontal {
                height: 16px;
                background-color: #861252;
                border-radius: 8px;
            }

            QSlider::handle:horizontal {
                width: 16px;
                height: 16px;
                border-radius: 8px;
                background-color: #127ecb;
                cursor: pointer;
            }

            """
        )
        self.setContentsMargins(20, 20, 20, 20)
