from PySide6.QtWidgets import QGraphicsDropShadowEffect

class GeneralCustom():
    def __init__(self,ui):
        self.ui = ui
        self.Close_window()

    def Close_window(self):
        self.ui.pushButton_2.clicked.connect(self.ui.close)

