from PyQt6.QtWidgets import QWidget, QPushButton
from pyqt6_plugins.examplebutton import QtWidgets

from windows.HotKey import Ui_Form

SAVE_HOT = 'Ctrl+S'
BRUSH_HOT = 'F1'
LINE_HOT = 'F2'
CIRCLE_HOT = 'F3'
TRIANGLE_HOT = 'F4'
SQUARE_HOT = 'F5'
STAR_MOT = 'F6'
ARROW_MOT = 'F7'
TEXT_HOT = 'F8'

UNDO_HOT = 'Ctrl+Z'
REDO_HOT = 'Ctrl+Y'

ZOOM_IN = 'Ctrl+='
ZOOM_OUT = 'Ctrl+-'




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

        self.SAVE_HOT = 'Ctrl+S'
        self.BRUSH_HOT = 'F1'
        self.LINE_HOT = 'F2'
        self.CIRCLE_HOT = 'F3'
        self.TRIANGLE_HOT = 'F4'
        self.SQUARE_HOT = 'F5'
        self.STAR_MOT = 'F6'
        self.ARROW_MOT = 'F7'
        self.TEXT_HOT = 'F8'

        self.UNDO_HOT = 'Ctrl+Z'
        self.REDO_HOT = 'Ctrl+Y'

        self.ZOOM_IN = 'Ctrl+='
        self.ZOOM_OUT = 'Ctrl+-'


    def apply_hoykeys(self):
            pass


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = HotKey()
    window.show()
    sys.exit(app.exec())