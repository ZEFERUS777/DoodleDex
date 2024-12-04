import logging
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QPainter, QPen, QPixmap, QFont, QMouseEvent
from PyQt6.QtWidgets import QWidget, QFileDialog, QColorDialog, QInputDialog, QFontDialog, QMessageBox
from tools.shapes import BrushPoint, Line, Circle, Triangle, Square, Star, Arrow, Text, Image

# Настройка логирования
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


class Canvas(QWidget):
    def __init__(self):
        super().__init__()
        self.objects = []
        self.instrument = 'brush'
        self.undo_stack = []
        self.current_color = QColor(0, 0, 0)
        self.current_font = QFont("Arial", 12)
        self.current_image = None
        self.drawing_text = False
        self.text_start_pos = None
        self.text = ""
        self.current_pen_width = 1
        self.brush_styles = {
            "Solid": Qt.PenStyle.SolidLine,
            "Dash": Qt.PenStyle.DashLine,
            "Dot": Qt.PenStyle.DotLine,
            "Dash Dot": Qt.PenStyle.DashDotLine,
            "Dash Dot Dot": Qt.PenStyle.DashDotDotLine
        }
        self.current_brush_style = self.brush_styles["Solid"]
        self.fill_color = QColor(255, 255, 255)  # Default fill color is white
        self.zoom_factor = 1.0

    def paintEvent(self, event):
        painter = QPainter(self)

        # Рисовать фоновое изображение, если оно загружено
        if self.current_image:
            scaled_image = self.current_image.scaled(self.current_image.size() * self.zoom_factor,
                                                     Qt.AspectRatioMode.KeepAspectRatio)
            painter.drawPixmap(0, 0, scaled_image)
            logger.debug('Drawing background image')

        # Рисовать все объекты
        for obj in self.objects:
            obj.draw(painter)
        logger.debug('Drawing all objects')

    def mousePressEvent(self, event: QMouseEvent):
        if self.instrument == "brush":
            self.objects.append(
                BrushPoint(event.position().x(), event.position().y(), self.current_color, self.current_pen_width))
        elif self.instrument == "line":
            self.objects.append(
                Line(event.position().x(), event.position().y(), event.position().x(), event.position().y(),
                     self.current_color, self.current_pen_width))
        elif self.instrument == "circle":
            self.objects.append(
                Circle(event.position().x(), event.position().y(), event.position().x(), event.position().y(),
                       self.current_color, self.current_pen_width))
        elif self.instrument == "triangle":
            self.objects.append(
                Triangle(event.position().x(), event.position().y(), event.position().x(), event.position().y(),
                         event.position().x(), event.position().y(), self.current_color, self.current_pen_width))
        elif self.instrument == "square":
            self.objects.append(
                Square(event.position().x(), event.position().y(), 0, self.current_color, self.current_pen_width))
        elif self.instrument == "star":
            self.objects.append(
                Star(event.position().x(), event.position().y(), 0, 0, self.current_color, self.current_pen_width))
        elif self.instrument == "arrow":
            self.objects.append(
                Arrow(event.position().x(), event.position().y(), event.position().x(), event.position().y(),
                      self.current_color, self.current_pen_width))
        elif self.instrument == "text":
            text, ok = QInputDialog.getText(self, 'Text', 'Enter text:')
            if ok and text:
                self.objects.append(
                    Text(event.position().x(), event.position().y(), text, self.current_font, self.current_color))
        elif self.instrument == "image_p":
            path, _ = QFileDialog.getOpenFileName(self, 'Open Image', '', 'Image Files (*.png *.jpg *.bmp)')
            width, _ = QInputDialog.getInt(self, 'Enter width', 'Enter width')
            height, okay = QInputDialog.getInt(self, 'Enter height', 'Enter height')
            if okay:
                self.objects.append(Image(event.position().x(), event.position().y(), path, width=width, height=height))
        self.update()
        logger.debug(f'Mouse press event at ({event.position().x()}, {event.position().y()})')

    def mouseMoveEvent(self, event: QMouseEvent):
        if self.instrument == "brush":
            self.objects.append(
                BrushPoint(event.position().x(), event.position().y(), self.current_color, self.current_pen_width))
        elif self.instrument == "line":
            self.objects[-1].ex = int(event.position().x())
            self.objects[-1].ey = int(event.position().y())
        elif self.instrument == "circle":
            self.objects[-1].x = int(event.position().x())
            self.objects[-1].y = int(event.position().y())
        elif self.instrument == "triangle":
            self.objects[-1].x2 = int(event.position().x())
            self.objects[-1].y2 = int(event.position().y())
            self.objects[-1].x3 = int(event.position().x() + 50)
            self.objects[-1].y3 = int(event.position().y() + 50)
        elif self.instrument == "square":
            self.objects[-1].width = int(abs(event.position().x() - self.objects[-1].x))
        elif self.instrument == "star":
            self.objects[-1].outer_radius = int(abs(event.position().x() - self.objects[-1].x))
            self.objects[-1].inner_radius = int(abs(event.position().y() - self.objects[-1].y))
        elif self.instrument == "arrow":
            self.objects[-1].ex = int(event.position().x())
            self.objects[-1].ey = int(event.position().y())
        self.update()
        logger.debug(f'Mouse move event at ({event.position().x()}, {event.position().y()})')

    def setBrush(self):
        self.instrument = 'brush'
        logger.debug('Setting instrument to brush')

    def setLine(self):
        self.instrument = 'line'
        logger.debug('Setting instrument to line')

    def setCircle(self):
        self.instrument = 'circle'
        logger.debug('Setting instrument to circle')

    def setTriangle(self):
        self.instrument = 'triangle'
        logger.debug('Setting instrument to triangle')

    def setSquare(self):
        self.instrument = 'square'
        logger.debug('Setting instrument to square')

    def setStar(self):
        self.instrument = 'star'
        logger.debug('Setting instrument to star')

    def setArrow(self):
        self.instrument = 'arrow'
        logger.debug('Setting instrument to arrow')

    def setText(self):
        self.instrument = 'text'
        logger.debug('Setting instrument to text')

    def setImage(self):
        self.instrument = 'image_p'
        logger.debug('Setting instrument to image')

    def setColor(self):
        self.current_color = QColorDialog.getColor()
        logger.debug(f'Setting color to {self.current_color}')

    def setFill(self):
        self.fill_color = QColorDialog.getColor()
        logger.debug(f'Setting fill color to {self.fill_color}')

    def setFont(self):
        font, ok = QFontDialog.getFont(self)
        if ok:
            self.current_font = font
            logger.debug(f'Setting font to {self.current_font}')

    def setPenWidth(self, width):
        self.current_pen_width = width
        logger.debug(f'Setting pen width to {self.current_pen_width}')

    def setBrushStyle(self, style):
        self.current_brush_style = self.brush_styles[style]
        logger.debug(f'Setting brush style to {style}')

    def clean(self):
        self.objects = []
        self.update()
        logger.debug('Cleaning canvas')

    def undo(self):
        if self.objects:
            self.undo_stack.append(self.objects.pop())
            self.update()
            logger.debug('Undoing last action')

    def redo(self):
        if self.undo_stack:
            self.objects.append(self.undo_stack.pop())
            self.update()
            logger.debug('Redoing last action')

    def saveImage(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Save Image", "",
                                                   "JPEG Files (*.jpg);;PNG Files (*.png);;All Files (*)")
        if file_name:
            pixmap = QPixmap(self.size())
            self.render(pixmap)
            pixmap.save(file_name)
            logger.debug(f'Saving image to {file_name}')

    def openImage(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Image", "",
                                                   "JPEG Files (*.jpg);;PNG Files (*.png);;All Files (*)")
        if file_name:
            # Очистить все предыдущие объекты
            self.objects = []

            # Загрузить изображение и масштабировать его до размеров окна
            self.current_image = QPixmap(file_name).scaled(self.size(), Qt.AspectRatioMode.KeepAspectRatio)

            # Обновить холст
            self.update()
            logger.debug(f'Opening image from {file_name}')

    def zoomIn(self):
        self.zoom_factor *= 1.2
        self.update()
        logger.debug('Zooming in')

    def zoomOut(self):
        self.zoom_factor /= 1.2
        self.update()
        logger.debug('Zooming out')

    def resetZoom(self):
        self.zoom_factor = 1.0
        self.update()
        logger.debug('Resetting zoom')
