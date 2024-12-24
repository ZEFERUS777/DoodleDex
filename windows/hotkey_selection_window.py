import sys
from email.policy import default
from fileinput import close

from PyQt6.QtWidgets import QWidget, QPushButton
from PyQt6.QtCore import pyqtSignal

from windows.HotKey import Ui_Form

SAVE_HOT = None
BRUSH_HOT = None
LINE_HOT = None
CIRCLE_HOT = None
TRIANGLE_HOT = None
SQUARE_HOT = None
STAR_MOT = None
ARROW_MOT = None
TEXT_HOT = 'F8'

UNDO_HOT = None
REDO_HOT = None

ZOOM_IN = None
ZOOM_OUT = None

default_settings = """Ctrl+S
F1
F2
F3
F4
F5
F6
F7
F8
Ctrl+Z
Ctrl+X
Ctrl+=
Ctrl+-""" # стандартные настройки

with open('.\settings.txt', 'r') as f:
    lines = f.readlines()
    SAVE_HOT = lines[0].strip()
    BRUSH_HOT = lines[1].strip()
    LINE_HOT = lines[2].strip()
    CIRCLE_HOT = lines[3].strip()
    TRIANGLE_HOT = lines[4].strip()
    SQUARE_HOT = lines[5].strip()
    STAR_MOT = lines[6].strip()
    ARROW_MOT = lines[7].strip()
    TEXT_HOT = lines[8].strip()
    UNDO_HOT = lines[9].strip()
    REDO_HOT = lines[10].strip()
    ZOOM_IN = lines[11].strip()
    ZOOM_OUT = lines[12].strip()
    f.close()


class HotKey(QWidget, Ui_Form):
    hotkeys_applied = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.apply_btn = QPushButton('Apply', self)
        self.apply_btn.move(self.label_11.x() + 15, self.label_11.y() - 25)
        self.apply_btn.setStyleSheet("""
        QPushButton {
                border: 1px solid;
                border-radius: 5px;
            }""")
        self.apply_btn.resize(50, 20)
        self.apply_btn.clicked.connect(self.apply_hotkeys)

        self.default_settings = default_settings
        self.default_settings_btn = QPushButton('Default', self)
        self.default_settings_btn.move(self.apply_btn.x() + 60, self.apply_btn.y())
        self.default_settings_btn.setStyleSheet("""
        QPushButton {
                border: 1px solid;
                border-radius: 5px;
            }""")
        self.default_settings_btn.resize(50, 20)
        self.default_settings_btn.clicked.connect(self.set_default_settings)

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
        self.set_def_val_hotkeys()

    def apply_hotkeys(self):
        self.BRUSH_HOT = self.keySequenceEdit.keySequence().toString() if self.keySequenceEdit.keySequence().toString() else self.BRUSH_HOT
        self.LINE_HOT = self.keySequenceEdit_2.keySequence().toString() if self.keySequenceEdit_2.keySequence().toString() else self.LINE_HOT
        self.CIRCLE_HOT = self.keySequenceEdit_3.keySequence().toString() if self.keySequenceEdit_3.keySequence().toString() else self.CIRCLE_HOT
        self.TRIANGLE_HOT = self.keySequenceEdit_4.keySequence().toString() if self.keySequenceEdit_4.keySequence().toString() else self.TRIANGLE_HOT
        self.SQUARE_HOT = self.keySequenceEdit_5.keySequence().toString() if self.keySequenceEdit_5.keySequence().toString() else self.SQUARE_HOT
        self.STAR_MOT = self.keySequenceEdit_6.keySequence().toString() if self.keySequenceEdit_6.keySequence().toString() else self.STAR_MOT
        self.ARROW_MOT = self.keySequenceEdit_7.keySequence().toString() if self.keySequenceEdit_7.keySequence().toString() else self.ARROW_MOT
        self.SAVE_HOT = self.keySequenceEdit_8.keySequence().toString() if self.keySequenceEdit_8.keySequence().toString() else self.SAVE_HOT
        self.UNDO_HOT = self.keySequenceEdit_9.keySequence().toString() if self.keySequenceEdit_9.keySequence().toString() else self.UNDO_HOT
        self.REDO_HOT = self.keySequenceEdit_10.keySequence().toString() if self.keySequenceEdit_10.keySequence().toString() else self.REDO_HOT

    def set_default_settings(self):
        with open('.\settings.txt', 'w') as f:
            f.write(self.default_settings)
            f.close()
            self.set_class_variable()

    def set_def_val_hotkeys(self):
        self.keySequenceEdit_8.setKeySequence(self.SAVE_HOT)
        self.keySequenceEdit.setKeySequence(self.BRUSH_HOT)
        self.keySequenceEdit_2.setKeySequence(self.LINE_HOT)
        self.keySequenceEdit_3.setKeySequence(self.CIRCLE_HOT)
        self.keySequenceEdit_4.setKeySequence(self.TRIANGLE_HOT)
        self.keySequenceEdit_5.setKeySequence(self.SQUARE_HOT)
        self.keySequenceEdit_6.setKeySequence(self.STAR_MOT)
        self.keySequenceEdit_7.setKeySequence(self.ARROW_MOT)
        self.keySequenceEdit_9.setKeySequence(self.UNDO_HOT)
        self.keySequenceEdit_10.setKeySequence(self.REDO_HOT)

    def set_class_variable(self):
        with open('.\settings.txt', 'r') as f:
            lines = f.readlines()
            self.SAVE_HOT = lines[0].strip()
            self.BRUSH_HOT = lines[1].strip()
            self.LINE_HOT = lines[2].strip()
            self.CIRCLE_HOT = lines[3].strip()
            self.TRIANGLE_HOT = lines[4].strip()
            self.SQUARE_HOT = lines[5].strip()
            self.STAR_MOT = lines[6].strip()
            self.ARROW_MOT = lines[7].strip()
            self.TEXT_HOT = lines[8].strip()
            self.UNDO_HOT = lines[9].strip()
            self.REDO_HOT = lines[10].strip()
            self.ZOOM_IN = lines[11].strip()
            self.ZOOM_OUT = lines[12].strip()
            f.close()
        self.set_def_val_hotkeys()

    def closeEvent(self, a0):
        with open('.\settings.txt', 'w') as f:
            f.write(self.SAVE_HOT + '\n')
            f.write(self.BRUSH_HOT + '\n')
            f.write(self.LINE_HOT + '\n')
            f.write(self.CIRCLE_HOT + '\n')
            f.write(self.TRIANGLE_HOT + '\n')
            f.write(self.SQUARE_HOT + '\n')
            f.write(self.STAR_MOT + '\n')
            f.write(self.ARROW_MOT + '\n')
            f.write(self.TEXT_HOT + '\n')
            f.write(self.UNDO_HOT + '\n')
            f.write(self.REDO_HOT + '\n')
            f.write(self.ZOOM_IN + '\n')
            f.write(self.ZOOM_OUT + '\n')
            f.close()