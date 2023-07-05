from PySide6.QtWidgets import QPushButton
from PySide6.QtGui import QPixmap,QIcon,QCursor
from PySide6.QtCore import Qt

class Button(QPushButton):
    def __init__(self,icon,color):
        super().__init__()
        self.setMinimumSize(30,30)
        self.set_curosr()
        self.setIcon(QIcon(f"assets/iconos/{icon}.png"))
        self.setStyleSheet(f"border-radius:14px; background-color:{color};")
        
    def set_curosr(self):
        pointer=QCursor(Qt.PointingHandCursor)
        self.setCursor(pointer)
    
