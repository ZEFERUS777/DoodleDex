import sys
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QColorDialog

from tools.canvas import Canvas
from windows.hotkey_selection_window import HotKey


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.canvas = Canvas()
        self.h = HotKey()
        self.setCentralWidget(self.canvas)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('DoodleDex')
        self.setGeometry(100, 100, 800, 600)

        # Apply styles
        self.setStyleSheet("""
                QMainWindow {
                    background-color: #f0f0f0;
                }
                
                QMenuBar {
                    background-color: #333;
                    color: #fff;
                    border-bottom: 1px solid #444;
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
                    border: 1px solid #444;
                }
                
                QMenu::item {
                    background-color: transparent;
                }
                
                QMenu::item:selected {
                    background-color: #555;
                }
                
                
                QPushButton {
                    background-color: #333;
                    color: #fff;
                    border: none;
                    padding: 5px 15px;
                    margin: 2px;
                    border-radius: 5px;
                }
                
                QPushButton:hover {
                    background-color: #555;
                }
                
                QPushButton:pressed {
                    background-color: #444;
                }
                
                QColorDialog {
                    background-color: #333;
                    color: #fff;
                    border: none;
                }
                
                QColorDialog::button-box {
                    background-color: #333;
                    border-top: 1px solid #444;
                }
                
                QColorDialog::button-box QPushButton {
                    background-color: #333;
                    color: #fff;
                    border: none;
                    padding: 5px 15px;
                }
                
                QColorDialog::button-box QPushButton:hover {
                    background-color: #555;
                }
                
                QColorDialog::button-box QPushButton:pressed {
                    background-color: #444;
                }
                
                QFileDialog {
                    background-color: #f0f0f0;
                    color: #000;
                }
                
                QFileDialog::item {
                    padding: 5px;
                }
                
                QFileDialog::item:selected {
                    background-color: #ddd;
                }
        """)

        # File menu
        menubar = self.menuBar()
        self.file_menu = menubar.addMenu('File')

        self.save_action = QAction('Save', self)
        self.save_action.setIcon(QIcon('icons/save_as_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.svg'))
        self.save_action.setShortcut(self.h.SAVE_HOT)
        self.save_action.triggered.connect(self.canvas.saveImage)
        self.file_menu.addAction(self.save_action)

        self.open_action = QAction('Open', self)
        self.open_action.setIcon(QIcon('icons/open_in_browser_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.svg'))
        self.open_action.triggered.connect(self.canvas.openImage)
        self.file_menu.addAction(self.open_action)

        self.exit_action = QAction('Exit', self)
        self.exit_action.triggered.connect(self.close)
        self.file_menu.addAction(self.exit_action)

        # Tools menu
        self.tools_menu = menubar.addMenu('Tools')

        self.brush_action = QAction('Brush', self)
        self.brush_action.setIcon(QIcon('icons/brush_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.svg'))
        self.brush_action.setShortcut(self.h.BRUSH_HOT)
        self.brush_action.triggered.connect(self.canvas.setBrush)
        self.tools_menu.addAction(self.brush_action)

        self.line_action = QAction('Line', self)
        self.line_action.setIcon(QIcon('icons/diagonal_line_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.svg'))
        self.line_action.setShortcut(self.h.LINE_HOT)
        self.line_action.triggered.connect(self.canvas.setLine)
        self.tools_menu.addAction(self.line_action)

        self.circle_action = QAction('Circle', self)
        self.circle_action.setIcon(QIcon('icons/animation_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.svg'))
        self.circle_action.setShortcut(self.h.CIRCLE_HOT)
        self.circle_action.triggered.connect(self.canvas.setCircle)
        self.tools_menu.addAction(self.circle_action)

        self.triangle_action = QAction('Triangle', self)
        self.triangle_action.setIcon(QIcon('icons/change_history_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.svg'))
        self.triangle_action.setShortcut(self.h.TRIANGLE_HOT)
        self.triangle_action.triggered.connect(self.canvas.setTriangle)
        self.tools_menu.addAction(self.triangle_action)

        self.square_action = QAction('Square', self)
        self.square_action.setIcon(QIcon('icons/check_box_outline_blank_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.svg'))
        self.square_action.setShortcut(self.h.SQUARE_HOT)
        self.square_action.triggered.connect(self.canvas.setSquare)
        self.tools_menu.addAction(self.square_action)

        self.star_action = QAction('Star', self)
        self.star_action.setIcon(QIcon('icons/star_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.svg'))
        self.star_action.setShortcut(self.h.STAR_MOT)
        self.star_action.triggered.connect(self.canvas.setStar)
        self.tools_menu.addAction(self.star_action)

        self.arrow_action = QAction('Arrow', self)
        self.arrow_action.setIcon(QIcon('icons/arrow_forward_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.svg'))
        self.arrow_action.setShortcut(self.h.ARROW_MOT)
        self.arrow_action.triggered.connect(self.canvas.setArrow)
        self.tools_menu.addAction(self.arrow_action)

        self.text_action = QAction('Text', self)
        self.text_action.setIcon(QIcon('icons/text_fields_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.svg'))
        self.text_action.setShortcut(self.h.TEXT_HOT)
        self.text_action.triggered.connect(self.canvas.setText)
        self.tools_menu.addAction(self.text_action)

        self.image_action = QAction('Image', self)
        self.image_action.setIcon(QIcon('icons/open_in_browser_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.svg'))
        self.image_action.triggered.connect(self.canvas.setImage)
        self.tools_menu.addAction(self.image_action)

        # Fill menu
        self.fill_menu = menubar.addMenu('Fill')

        self.fill_action = QAction('Set Fill Color', self)
        self.fill_action.setIcon(QIcon('icons/format_paint_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.svg'))
        self.fill_action.triggered.connect(self.setfill)
        self.fill_menu.addAction(self.fill_action)

        # Color menu
        color_menu = menubar.addMenu('Color')

        color_action = QAction('Set Color', self)
        color_action.setIcon(QIcon('icons/palette_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.svg'))
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

        self.undo_action = QAction('Undo', self)
        self.undo_action.setShortcut(self.h.UNDO_HOT)
        self.undo_action.setIcon(QIcon('icons/undo_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.svg'))
        self.undo_action.triggered.connect(self.canvas.undo)
        edit_menu.addAction(self.undo_action)

        self.redo_action = QAction('Redo', self)
        self.redo_action.setShortcut(self.h.REDO_HOT)
        self.redo_action.setIcon(QIcon('icons/redo_24dp_E8EAED_FILL0_wght400_GRAD0_opsz24.svg'))
        self.redo_action.triggered.connect(self.canvas.redo)
        edit_menu.addAction(self.redo_action)

        clear_action = QAction('Clear', self)
        clear_action.triggered.connect(self.canvas.clean)
        edit_menu.addAction(clear_action)

        # View menu
        view_menu = menubar.addMenu('View')

        self.zoom_in_action = QAction('Zoom In', self)
        self.zoom_in_action.setShortcut(self.h.ZOOM_IN)
        self.zoom_in_action.triggered.connect(self.canvas.zoomIn)
        view_menu.addAction(self.zoom_in_action)

        self.zoom_out_action = QAction('Zoom Out', self)
        self.zoom_out_action.setShortcut(self.h.ZOOM_OUT)
        self.zoom_out_action.triggered.connect(self.canvas.zoomOut)
        view_menu.addAction(self.zoom_out_action)

        reset_zoom_action = QAction('Reset Zoom', self)
        reset_zoom_action.triggered.connect(self.canvas.resetZoom)
        view_menu.addAction(reset_zoom_action)

        setting_menu = menubar.addMenu('Setting')

        setting_action = QAction('Setting', self)
        setting_menu.addAction(setting_action)
        setting_action.triggered.connect(self.open_hotkey_window)

    # Reinitialize UI to apply new shortcuts
    def open_hotkey_window(self):
        self.h.show()
        self.h.apply_btn.clicked.connect(self.reinit_hot)

    def reinit_hot(self):
        self.undo_action.setShortcut(self.h.UNDO_HOT)
        self.redo_action.setShortcut(self.h.REDO_HOT)
        self.triangle_action.setShortcut(self.h.TRIANGLE_HOT)
        self.square_action.setShortcut(self.h.SQUARE_HOT)
        self.star_action.setShortcut(self.h.STAR_MOT)
        self.arrow_action.setShortcut(self.h.ARROW_MOT)
        self.text_action.setShortcut(self.h.TEXT_HOT)
        self.brush_action.setShortcut(self.h.BRUSH_HOT)
        self.zoom_in_action.setShortcut(self.h.ZOOM_IN)
        self.zoom_out_action.setShortcut(self.h.ZOOM_OUT)
        self.line_action.setShortcut(self.h.LINE_HOT)
        self.circle_action.setShortcut(self.h.CIRCLE_HOT)
        self.h.close()

    def setfill(self):
        color = QColorDialog.getColor()
        self.canvas.setFillColor(color)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
