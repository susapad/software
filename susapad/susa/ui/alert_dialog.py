
from PySide6 import QtWidgets


class AlertDialog(QtWidgets.QDialog):

    def __init__(self, parent, message: str = None):
        super().__init__(parent)

        self.message = message
        if not self.message:
            self.message = \
                """
                SusaPad não encontrado. 
                Certifique-se que ele está conectado corretamente
                """


        self.setWindowTitle("Aviso")
        self.button_box = QtWidgets.QDialogButtonBox(QtWidgets.\
            QDialogButtonBox.Ok)
        self.button_box.accepted.connect(self.accept)


        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(QtWidgets.QLabel(self.message))
