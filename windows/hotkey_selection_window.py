from PyQt6.QtWidgets import QWidget, QPushButton
from pyqt6_plugins.examplebutton import QtWidgets

from HotKey import Ui_Form

BRUSH_HOT = None
LINE_HOT = None




class HotKey(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.apply_btn = QPushButton('Apply', self)
        self.apply_btn.move(self.label_11.x() + 15, self.label_11.y() - 25)
        self.apply_btn.setStyleSheet("""
        QPushButton {
                border: 1px solid;
                border-radius: 5px;
            }""")
        self.apply_btn.resize(50, 20)
        self.apply_btn.clicked.connect(self.apply_hoykeys)

    def apply_hoykeys(self):
        pass


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = HotKey()
    window.show()
    sys.exit(app.exec())