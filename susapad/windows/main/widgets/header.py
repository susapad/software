"""Common Widgets used by `MainWindow`"""

from PySide6 import QtCore, QtGui, QtWidgets


class SusaPadLogo(QtWidgets.QLabel):

    def __init__(self):
        super().__init__()
        self.setPixmap(QtGui.QPixmap("susapad/media/logo.png"))
        self.setStyleSheet("border-radius: 75%; margin: 0, 10px, 0, 20px;")
        self.purple_shadow()

    def purple_shadow(self):
        shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        shadow.setOffset(QtCore.QPoint(0,5))
        shadow.setBlurRadius(25)
        shadow.setColor(QtGui.QColor(195, 27, 120, 40))
        self.setGraphicsEffect(shadow)


class SusaPadTitle(QtWidgets.QLabel):

    def __init__(self):
        super().__init__("SusaPad")
        self.setStyleSheet(
            """
                color: white;
                font: 24px;
            """
        )


class StatusLabel(QtWidgets.QLabel):

    def __init__(self, main_window):
        super().__init__()
        self.__init_style()

    def __init_style(self):
        self.setStyleSheet("font: 12px; color: white;")
