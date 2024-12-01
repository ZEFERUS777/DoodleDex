import sys
from math import atan2, cos, sin, radians
from PyQt6.QtCore import QPoint, QPointF, Qt
from PyQt6.QtGui import QBrush, QColor, QPainter, QMouseEvent, QAction, QImage, QPixmap, QFont, QPen, QKeyEvent
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QFileDialog, QLabel, QVBoxLayout, QComboBox, \
    QColorDialog, QInputDialog


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


class Image:
    def __init__(self, x, y, image):
        self.x = int(x)
        self.y = int(y)
        self.image = image

    def draw(self, painter: QPainter):
        painter.drawImage(self.x, self.y, self.image)


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

    def paintEvent(self, event):
        painter = QPainter(self)
        for obj in self.objects:
            obj.draw(painter)

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
            self.drawing_text = True
            self.text_start_pos = event.position()
            self.text = ""
            self.objects.append(Text(self.text_start_pos.x(), self.text_start_pos.y(), self.text, self.current_font,
                                     self.current_color))
        elif self.instrument == "image" and self.current_image:
            self.objects.append(Image(event.position().x(), event.position().y(), self.current_image))
        self.update()

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

    def keyPressEvent(self, event: QKeyEvent):
        if self.drawing_text and event.key() != Qt.Key.Return and event.key() != Qt.Key.Enter:
            self.text += event.text()
            self.objects[-1].text = self.text
            self.update()
        elif self.drawing_text and (event.key() == Qt.Key.Return or event.key() == Qt.Key.Enter):
            self.drawing_text = False
            self.instrument = 'brush'
            self.update()

    def setBrush(self):
        self.instrument = 'brush'

    def setLine(self):
        self.instrument = 'line'

    def setCircle(self):
        self.instrument = 'circle'

    def setTriangle(self):
        self.instrument = 'triangle'

    def setSquare(self):
        self.instrument = 'square'

    def setStar(self):
        self.instrument = 'star'

    def setArrow(self):
        self.instrument = 'arrow'

    def setText(self):
        self.instrument = 'text'

    def setImage(self):
        self.instrument = 'image'

    def setColor(self):
        self.current_color = QColorDialog.getColor()

    def setFont(self):
        font, ok = QInputDialog.getfont(self, "Set Font", "Font", QFont("Arial"))
        if ok:
            self.current_font = font

    def setPenWidth(self, width):
        self.current_pen_width = width

    def setBrushStyle(self, style):
        self.current_brush_style = self.brush_styles[style]

    def clean(self):
        self.objects = []
        self.update()

    def undo(self):
        if self.objects:
            self.undo_stack.append(self.objects.pop())
            self.update()

    def redo(self):
        if self.undo_stack:
            self.objects.append(self.undo_stack.pop())
            self.update()

    def saveImage(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Save Image", "",
                                                   "JPEG Files (*.jpg);;PNG Files (*.png);;All Files (*)")
        if file_name:
            image = QImage(self.size(), QImage.Format.Format_ARGB32)
            painter = QPainter(image)
            self.paintEvent(None)
            painter.end()
            image.save(file_name)

    def openImage(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Image", "",
                                                   "JPEG Files (*.jpg);;PNG Files (*.png);;All Files (*)")
        if file_name:
            self.current_image = QImage(file_name)
