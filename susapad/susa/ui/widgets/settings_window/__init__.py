from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt

from . import actuation_point, togglers, sensibility


class FormsGroup(QtWidgets.QWidget):

    def __init__(self, window, susapad):
        super().__init__()

        self.rt_button = togglers.RapidTriggerButton(window, susapad)
        self.crt_button = togglers.ContinuousRapidTriggerButton(window, susapad)

        self.sensibility_slider_press = sensibility.PressSensibilitySlider(window, susapad)
        self.sensibility_slider_release = sensibility.ReleaseSensibilitySlider(window, susapad)
        
        self.actuation_slider_lower = actuation_point.LowerActuationSlider(window, susapad, self)
        self.actuation_slider_upper = actuation_point.UpperActuationSlider(window, susapad, self)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(QtWidgets.QLabel("Rapid Trigger"))
        self.layout.addWidget(self.rt_button)
        self.layout.addWidget(QtWidgets.QLabel("Rapid Trigger Contínuor"))
        self.layout.addWidget(self.crt_button)
        self.layout.addWidget(QtWidgets.QLabel("Sensibilidade: Pressionar e Soltar"))
        self.layout.addWidget(self.sensibility_slider_press, alignment = Qt.AlignJustify)
        self.layout.addWidget(self.sensibility_slider_release, alignment = Qt.AlignJustify)
        self.layout.addWidget(QtWidgets.QLabel("Pontos de Ativação: Mínimo e Máximo"))
        self.layout.addWidget(self.actuation_slider_lower, alignment = Qt.AlignJustify)
        self.layout.addWidget(self.actuation_slider_upper, alignment = Qt.AlignJustify)



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

            QPushButton {
                    background-color: #0e639e;
                    border-radius: 15px;
                    min-width: 10em;
                    padding: 6px;
                    font: bold;
                    color: white;
                }

            QPushButton:hover {
                background-color: #127ecb;
            }

            """
        )
        self.setContentsMargins(20, 20, 20, 20)
