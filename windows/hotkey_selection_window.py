from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QWidget, QPushButton

# Импорт UI-формы
from windows.HotKey import Ui_Form

# Переменные для хранения горячих клавиш
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

# Стандартные настройки
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
Ctrl+-"""

# Чтение настроек из файла
with open('.\\settings.txt', 'r') as f:
    lines = f.readlines()
    SAVE_HOT, BRUSH_HOT, LINE_HOT, CIRCLE_HOT, TRIANGLE_HOT,\
        SQUARE_HOT, STAR_MOT, ARROW_MOT, TEXT_HOT, UNDO_HOT, REDO_HOT, ZOOM_IN, ZOOM_OUT = [
        line.strip() for line in lines]


class HotKey(QWidget, Ui_Form):
    hotkeys_applied = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())

        # Кнопка "Применить"
        self.apply_btn = QPushButton('Apply', self)
        self.apply_btn.move(self.label_11.x() + 15, self.label_11.y() - 25)
        self.apply_btn.setStyleSheet("QPushButton { border: 1px solid; border-radius: 5px; }")
        self.apply_btn.resize(50, 20)
        self.apply_btn.clicked.connect(self.apply_hotkeys)

        # Кнопка "По умолчанию"
        self.default_settings_btn = QPushButton('default', self)
        self.default_settings_btn.move(self.apply_btn.x() + 60, self.apply_btn.y())
        self.default_settings_btn.setStyleSheet("QPushButton { border: 1px solid; border-radius: 5px; }")
        self.default_settings_btn.resize(50, 20)
        self.default_settings_btn.clicked.connect(self.set_default_settings)

        # Инициализация переменных с текущими настройками
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

        # Установка значений горячих клавиш по умолчанию
        self.set_def_val_hotkeys()

    def apply_hotkeys(self):
        """Применяет новые горячие клавиши"""
        self.BRUSH_HOT = self.keySequenceEdit.keySequence().toString() or self.BRUSH_HOT
        self.LINE_HOT = self.keySequenceEdit_2.keySequence().toString() or self.LINE_HOT
        self.CIRCLE_HOT = self.keySequenceEdit_3.keySequence().toString() or self.CIRCLE_HOT
        self.TRIANGLE_HOT = self.keySequenceEdit_4.keySequence().toString() or self.TRIANGLE_HOT
        self.SQUARE_HOT = self.keySequenceEdit_5.keySequence().toString() or self.SQUARE_HOT
        self.STAR_MOT = self.keySequenceEdit_6.keySequence().toString() or self.STAR_MOT
        self.ARROW_MOT = self.keySequenceEdit_7.keySequence().toString() or self.ARROW_MOT
        self.SAVE_HOT = self.keySequenceEdit_8.keySequence().toString() or self.SAVE_HOT
        self.UNDO_HOT = self.keySequenceEdit_9.keySequence().toString() or self.UNDO_HOT
        self.REDO_HOT = self.keySequenceEdit_10.keySequence().toString() or self.REDO_HOT

    def set_default_settings(self):
        """Устанавливает стандартные настройки и сохраняет их в файл"""
        with open('.\\settings.txt', 'w') as f:
            f.write(default_settings)
        self.set_class_variable()

    def set_def_val_hotkeys(self):
        """Устанавливает значения горячих клавиш по умолчанию"""
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
        """Обновляет значения переменных класса из файла настроек"""
        with open('.\\settings.txt', 'r') as f:
            lines = f.readlines()
            self.SAVE_HOT, self.BRUSH_HOT, self.LINE_HOT,\
            self.CIRCLE_HOT,self.TRIANGLE_HOT, self.SQUARE_HOT,\
                self.STAR_MOT, self.ARROW_MOT, self.TEXT_HOT,\
                self.UNDO_HOT, self.REDO_HOT, self.ZOOM_IN, self.ZOOM_OUT = [
                line.strip() for line in lines]
        self.set_def_val_hotkeys()

    def closeEvent(self, event):
        """Сохраняет текущие настройки при закрытии окна"""
        with open('.\\settings.txt', 'w') as f:
            f.write('\n'.join([
                self.SAVE_HOT,
                self.BRUSH_HOT,
                self.LINE_HOT,
                self.CIRCLE_HOT,
                self.TRIANGLE_HOT,
                self.SQUARE_HOT,
                self.STAR_MOT,
                self.ARROW_MOT,
                self.TEXT_HOT,
                self.UNDO_HOT,
                self.REDO_HOT,
                self.ZOOM_IN,
                self.ZOOM_OUT
            ]))
