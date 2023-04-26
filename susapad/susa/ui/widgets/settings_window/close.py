
from susapad.susa.ui.widgets.common import button


class CloseButton(button.BaseButton):

    def __init__(self, window, main_window):
        super().__init__("Fechar", "Escape", window)

        self.setAccessibleName("close")
        #self.setFixedSize(30, 30)
        self.setGeometry(420, 20, 60, 16)
        self.clicked.connect(main_window.close_settings_window)
        self.setStyleSheet(
            """
            QPushButton[accessibleName="close"] {
                    background-color: #b71970;
                    border-radius: 10px;
                    min-width: 60px;
                    max-width: 60px;
                    font: bold;
                    color: white;
                }

            QPushButton:hover[accessibleName="close"] {
                background-color: #dd1e87;
            }
            """
        )
