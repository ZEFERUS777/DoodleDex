import sys
from PyQt6.QtWidgets import QWidget, QPushButton
from PyQt6.QtCore import pyqtSignal

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
    hotkeys_applied = pyqtSignal(dict)

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
        self.apply_btn.clicked.connect(self.apply_hotkeys)

        self.SAVE_HOT = SAVE_HOT
        self.BRUSH_HOT = BRUSH_HOT
        self.LINE_HOT = LINE_HOT
        self.CIRCLE_HOT = CIRCLE_HOT
        self.TRIANGLE_HOT = TRIANGLE_HOT
        self.SQUARE_HOT = SQUARE_HOT
        self.STAR_MOT = STAR_MOT
        self.ARROW_MOT = ARROW_MOT
        self.TEXT_HOT = TEXT_HOT

        self.UNDO_HOT = UNDO_HOT
        self.REDO_HOT = REDO_HOT

        self.ZOOM_IN = ZOOM_IN
        self.ZOOM_OUT = ZOOM_OUT

    def apply_hotkeys(self):
        self.BRUSH_HOT = self.keySequenceEdit.keySequence().toString()
        self.LINE_HOT = self.keySequenceEdit_2.keySequence().toString()
        self.CIRCLE_HOT = self.keySequenceEdit_3.keySequence().toString()
        self.TRIANGLE_HOT = self.keySequenceEdit_4.keySequence().toString()
        self.SQUARE_HOT = self.keySequenceEdit_5.keySequence().toString()
        self.STAR_MOT = self.keySequenceEdit_6.keySequence().toString()
        self.ARROW_MOT = self.keySequenceEdit_7.keySequence().toString()
        self.TEXT_HOT = self.keySequenceEdit_8.keySequence().toString()

        print(self.SAVE_HOT, self.BRUSH_HOT, self.LINE_HOT, self.CIRCLE_HOT, self.TRIANGLE_HOT, self.SQUARE_HOT,
              self.STAR_MOT, self.ARROW_MOT, self.TEXT_HOT)
