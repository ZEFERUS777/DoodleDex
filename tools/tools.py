from math import atan2, cos, sin, radians
from PyQt6.QtCore import QPoint, QPointF, Qt
from PyQt6.QtGui import QBrush, QColor, QPainter, QMouseEvent, QPixmap, QFont, QPen
from PyQt6.QtWidgets import QWidget, QFileDialog, QColorDialog, QInputDialog, QFontDialog, QMessageBox
import logging

# Настройка логирования
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


class BrushPoint:
    def __init__(self, x, y, color=QColor(0, 0, 0), pen_width=1):
        self.x = int(x)
        self.y = int(y)
        self.color = color
        self.pen_width = pen_width

    def draw(self, painter: QPainter):
        painter.setBrush(QBrush(self.color))
        painter.setPen(QPen(self.color, self.pen_width))
        painter.drawEllipse(self.x - 5, self.y - 5, 10, 10)
        logger.debug(f'Painting brush at ({self.x}, {self.y}) with color {self.color}')


class Line:
    def __init__(self, sx, sy, ex, ey, color=QColor(0, 0, 0), pen_width=1):
        self.sx = int(sx)
        self.sy = int(sy)
        self.ex = int(ex)
        self.ey = int(ey)
        self.color = color
        self.pen_width = pen_width

    def draw(self, painter: QPainter):
        painter.setBrush(QBrush(self.color))
        painter.setPen(QPen(self.color, self.pen_width))
        painter.drawLine(self.sx, self.sy, self.ex, self.ey)
        logger.debug(f'Painting line from ({self.sx}, {self.sy}) to ({self.ex}, {self.ey})')


class Circle:
    def __init__(self, cx, cy, x, y, color=QColor(0, 0, 0), pen_width=1):
        self.cx = int(cx)
        self.cy = int(cy)
        self.x = int(x)
        self.y = int(y)
        self.color = color
        self.pen_width = pen_width

    def draw(self, painter: QPainter):
        painter.setBrush(QBrush(self.color, Qt.BrushStyle.NoBrush))
        painter.setPen(QPen(self.color, self.pen_width))
        radius = int(((self.cx - self.x) ** 2 + (self.cy - self.y) ** 2) ** 0.5)
        painter.drawEllipse(self.cx - radius, self.cy - radius, 2 * radius, 2 * radius)
        logger.debug(f'Painting circle at ({self.cx}, {self.cy}) with radius {radius}')


class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3, color=QColor(0, 0, 0), pen_width=1):
        self.x1 = int(x1)
        self.y1 = int(y1)
        self.x2 = int(x2)
        self.y2 = int(y2)
        self.x3 = int(x3)
        self.y3 = int(y3)
        self.color = color
        self.pen_width = pen_width

    def draw(self, painter: QPainter):
        painter.setBrush(QBrush(self.color))
        painter.setPen(QPen(self.color, self.pen_width))
        points = [(self.x1, self.y1), (self.x2, self.y2), (self.x3, self.y3)]
        painter.drawPolygon([QPoint(x, y) for x, y in points])
        logger.debug(f'Painting triangle at ({self.x1}, {self.y1}), ({self.x2}, {self.y2}), ({self.x3}, {self.y3})')


class Square:
    def __init__(self, x, y, width, color=QColor(0, 0, 0), pen_width=1):
        self.x = int(x)
        self.y = int(y)
        self.width = int(width)
        self.color = color
        self.pen_width = pen_width

    def draw(self, painter: QPainter):
        painter.setBrush(QBrush(self.color))
        painter.setPen(QPen(self.color, self.pen_width))
        painter.drawRect(self.x, self.y, self.width, self.width)
        logger.debug(f'Painting square at ({self.x}, {self.y}) with width {self.width}')


class Star:
    def __init__(self, x, y, outer_radius, inner_radius, color=QColor(0, 0, 0), pen_width=1):
        self.x = int(x)
        self.y = int(y)
        self.outer_radius = int(outer_radius)
        self.inner_radius = int(inner_radius)
        self.color = color
        self.pen_width = pen_width

    def draw(self, painter: QPainter):
        painter.setBrush(QBrush(self.color))
        painter.setPen(QPen(self.color, self.pen_width))
        points = []
        angle = 0
        for i in range(10):
            if i % 2 == 0:
                r = self.outer_radius
            else:
                r = self.inner_radius
            x = self.x + r * cos(radians(angle))
            y = self.y - r * sin(radians(angle))
            points.append(QPoint(int(x), int(y)))
            angle += 36
        painter.drawPolygon(points)
        logger.debug(
            f'Painting star at ({self.x}, {self.y}) with outer radius {self.outer_radius} and inner radius {self.inner_radius}')


class Arrow:
    def __init__(self, sx, sy, ex, ey, color=QColor(0, 0, 0), pen_width=1):
        self.sx = int(sx)
        self.sy = int(sy)
        self.ex = int(ex)
        self.ey = int(ey)
        self.color = color
        self.pen_width = pen_width

    def draw(self, painter: QPainter):
        painter.setBrush(QBrush(self.color))
        painter.setPen(QPen(self.color, self.pen_width))
        painter.drawLine(self.sx, self.sy, self.ex, self.ey)
        angle = atan2(self.sy - self.ey, self.sx - self.ex)
        arrow_size = 10
        arrow_angle = radians(30)
        p1 = QPointF(self.ex + arrow_size * cos(angle + arrow_angle),
                     self.ey - arrow_size * sin(angle + arrow_angle))
        p2 = QPointF(self.ex + arrow_size * cos(angle - arrow_angle),
                     self.ey - arrow_size * sin(angle - arrow_angle))
        painter.drawPolygon([QPointF(self.ex, self.ey), p1, p2])
        logger.debug(f'Painting arrow from ({self.sx}, {self.sy}) to ({self.ex}, {self.ey})')


class Text:
    def __init__(self, x, y, text, font, color=QColor(0, 0, 0)):
        self.x = int(x)
        self.y = int(y)
        self.text = text
        self.font = font
        self.color = color

    def draw(self, painter: QPainter):
        painter.setPen(self.color)
        painter.setFont(self.font)
        painter.drawText(self.x, self.y, self.text)
        logger.debug(f'Painting text "{self.text}" at ({self.x}, {self.y})')


class Image:
    def __init__(self, x, y, path, width=100, height=100):
        self.x = int(x)
        self.y = int(y)
        self.path = path
        self.pixmap = QPixmap(self.path)
        self.width = width
        self.height = height
        self.scaled_pixmap = self.pixmap.scaled(self.width, self.height)

    def draw(self, painter: QPainter):
        try:
            painter.drawPixmap(self.x, self.y, self.scaled_pixmap)
            logger.debug(f'Painting image at ({self.x}, {self.y}) with size ({self.width}, {self.height})')
        except Exception as e:
            logger.error(f'Error drawing image: {e}')
            QMessageBox.critical(None, 'Ошибка', str(e))


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

    def paintEvent(self, event):
        painter = QPainter(self)

        # Рисовать фоновое изображение, если оно загружено
        if self.current_image:
            painter.drawPixmap(0, 0, self.current_image)
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
                self.objects.append(Text(event.position().x(), event.position().y(), text, self.current_font,
                                         self.current_color))
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
        self.current_image.scale(1.2, 1.2)
        self.update()
        logger.debug('Zooming in')

    def zoomOut(self):
        self.current_image.scale(0.8, 0.8)
        self.update()
        logger.debug('Zooming out')

    def resetZoom(self):
        self.resetTransform()
        self.update()
        logger.debug('Resetting zoom')

