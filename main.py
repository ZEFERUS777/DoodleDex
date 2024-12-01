import sys

from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow

from tools.tools import Canvas


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.canvas = Canvas()
        self.setCentralWidget(self.canvas)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Paint Application')
        self.setGeometry(100, 100, 800, 600)

        # Apply styles
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f0f0;
            }
            QMenuBar {
                background-color: #333;
                color: #fff;
            }
            QMenuBar::item {
                background-color: #333;
                color: #fff;
            }
            QMenuBar::item:selected {
                background-color: #555;
            }
            QMenu {
                background-color: #333;
                color: #fff;
            }
            QMenu::item {
                background-color: #333;
                color: #fff;
            }
            QMenu::item:selected {
                background-color: #555;
            }
            QPushButton {
                background-color: #333;
                color: #fff;
                border: none;
                padding: 5px 10px;
            }
            QPushButton:hover {
                background-color: #555;
            }
        """)

        # File menu
        menubar = self.menuBar()
        file_menu = menubar.addMenu('File')

        save_action = QAction('Save', self)
        save_action.triggered.connect(self.canvas.saveImage)
        file_menu.addAction(save_action)

        open_action = QAction('Open', self)
        open_action.triggered.connect(self.canvas.openImage)
        file_menu.addAction(open_action)

        exit_action = QAction('Exit', self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # Tools menu
        tools_menu = menubar.addMenu('Tools')

        brush_action = QAction('Brush', self)
        brush_action.triggered.connect(self.canvas.setBrush)
        tools_menu.addAction(brush_action)

        line_action = QAction('Line', self)
        line_action.triggered.connect(self.canvas.setLine)
        tools_menu.addAction(line_action)

        circle_action = QAction('Circle', self)
        circle_action.triggered.connect(self.canvas.setCircle)
        tools_menu.addAction(circle_action)

        triangle_action = QAction('Triangle', self)
        triangle_action.triggered.connect(self.canvas.setTriangle)
        tools_menu.addAction(triangle_action)

        square_action = QAction('Square', self)
        square_action.triggered.connect(self.canvas.setSquare)
        tools_menu.addAction(square_action)

        star_action = QAction('Star', self)
        star_action.triggered.connect(self.canvas.setStar)
        tools_menu.addAction(star_action)

        arrow_action = QAction('Arrow', self)
        arrow_action.triggered.connect(self.canvas.setArrow)
        tools_menu.addAction(arrow_action)

        text_action = QAction('Text', self)
        text_action.triggered.connect(self.canvas.setText)
        tools_menu.addAction(text_action)

        image_action = QAction('Image', self)
        image_action.triggered.connect(self.canvas.setImage)
        tools_menu.addAction(image_action)

        # Fill menu
        fill_menu = menubar.addMenu('Fill')

        fill_action = QAction('Set Fill Color', self)
        fill_action.triggered.connect(self.canvas.setFill)
        fill_menu.addAction(fill_action)

        # Color menu
        color_menu = menubar.addMenu('Color')

        color_action = QAction('Set Color', self)
        color_action.triggered.connect(self.canvas.setColor)
        color_menu.addAction(color_action)

        # Font menu
        font_menu = menubar.addMenu('Font')

        font_action = QAction('Set Font', self)
        font_action.triggered.connect(self.canvas.setFont)
        font_menu.addAction(font_action)

        # Pen Width menu
        pen_width_menu = menubar.addMenu('Pen Width')

        for width in [1, 2, 3, 4, 5]:
            action = QAction(f'{width}px', self)
            action.triggered.connect(lambda checked, w=width: self.canvas.setPenWidth(w))
            pen_width_menu.addAction(action)

        # Brush Style menu
        brush_style_menu = menubar.addMenu('Brush Style')

        for style in ['Solid', 'Dash', 'Dot', 'Dash Dot', 'Dash Dot Dot']:
            action = QAction(style, self)
            action.triggered.connect(lambda checked, s=style: self.canvas.setBrushStyle(s))
            brush_style_menu.addAction(action)

        # Edit menu
        edit_menu = menubar.addMenu('Edit')

        undo_action = QAction('Undo', self)
        undo_action.triggered.connect(self.canvas.undo)
        edit_menu.addAction(undo_action)

        redo_action = QAction('Redo', self)
        redo_action.triggered.connect(self.canvas.redo)
        edit_menu.addAction(redo_action)

        clear_action = QAction('Clear', self)
        clear_action.triggered.connect(self.canvas.clean)
        edit_menu.addAction(clear_action)

        # View menu
        view_menu = menubar.addMenu('View')

        zoom_in_action = QAction('Zoom In', self)
        zoom_in_action.triggered.connect(self.canvas.zoomIn)
        view_menu.addAction(zoom_in_action)

        zoom_out_action = QAction('Zoom Out', self)
        zoom_out_action.triggered.connect(self.canvas.zoomOut)
        view_menu.addAction(zoom_out_action)

        reset_zoom_action = QAction('Reset Zoom', self)
        reset_zoom_action.triggered.connect(self.canvas.resetZoom)
        view_menu.addAction(reset_zoom_action)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
