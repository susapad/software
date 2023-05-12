"""Common Widgets used by `MainWindow`"""

from __feature__ import true_property
from __feature__ import snake_case

from PySide6 import QtCore, QtGui, QtWidgets


class SusaPadLogo(QtWidgets.QLabel):

    def __init__(self):
        super().__init__()
        self.pixmap = QtGui.QPixmap("susapad/media/logo.png")
        self.style_sheet = "border-radius: 75%; margin: 0, 10px, 0, 20px;"
        self.purple_shadow()

    def purple_shadow(self):
        shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        shadow.offset = QtCore.QPoint(0,5)
        shadow.blur_radius = 25
        shadow.color = QtGui.QColor(195, 27, 120, 40)
        self.graphics_effect = shadow


class SusaPadTitle(QtWidgets.QLabel):

    def __init__(self):
        super().__init__("SusaPad")
        self.style_sheet = """
                color: white;
                font: 24px;
            """


class StatusLabel(QtWidgets.QLabel):

    def __init__(self, main_window):
        super().__init__()
        self.__init_style()

        self.set_found(main_window.susapad.serial)


    def set_found(self, found: bool = True):
        if found:
            self.text = "SusaPad encontrado!"
        else:
            self.text = "SusaPad não encontrado!"

    def __init_style(self):
        self.style_sheet = "font: 12px; color: white;"
