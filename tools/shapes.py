from math import atan2, cos, sin, radians

from PyQt6.QtCore import QPoint, QPointF
from PyQt6.QtGui import QBrush, QColor, QPainter, QPen, QPixmap, QPolygon


class BrushPoint:
    def __init__(self, x, y, color=QColor(0, 0, 0), pen_width=1):
        self.x = int(x)
        self.y = int(y)
        self.color = color
        self.pen_width = pen_width

    def draw(self, painter: QPainter):
        painter.setRenderHint(QPainter.RenderHint.Antialiasing, True)
        painter.setBrush(QBrush(self.color))
        painter.setPen(QPen(self.color, self.pen_width))
        painter.drawEllipse(self.x - 5, self.y - 5, 10, 10)


class Line:
    def __init__(self, sx, sy, ex, ey, color=QColor(0, 0, 0), pen_width=1, fill_color=None):
        self.sx = int(sx)
        self.sy = int(sy)
        self.ex = int(ex)
        self.ey = int(ey)
        self.color = color
        self.pen_width = pen_width
        self.fill_color = fill_color if fill_color else None

    def draw(self, painter: QPainter):
        painter.setRenderHint(QPainter.RenderHint.Antialiasing, True)
        painter.setBrush(QBrush(self.fill_color if self.fill_color else self.color))
        painter.setPen(QPen(self.color, self.pen_width))
        painter.drawLine(self.sx, self.sy, self.ex, self.ey)


class Circle:
    def __init__(self, cx, cy, x, y, color=QColor(0, 0, 0), pen_width=1, fill_color=None):
        self.cx = int(cx)
        self.cy = int(cy)
        self.x = int(x)
        self.y = int(y)
        self.color = color
        self.pen_width = pen_width
        self.fill_color = fill_color if fill_color else None

    def draw(self, painter: QPainter):
        painter.setRenderHint(QPainter.RenderHint.Antialiasing, True)
        painter.setBrush(QBrush(self.fill_color if self.fill_color else self.color))
        painter.setPen(QPen(self.color, self.pen_width))
        radius = int(((self.cx - self.x) ** 2 + (self.cy - self.y) ** 2) ** 0.5)
        painter.drawEllipse(self.cx - radius, self.cy - radius, 2 * radius, 2 * radius)


class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3, color=QColor(0, 0, 0), pen_width=1, fill_color=None):
        self.x1 = int(x1)
        self.y1 = int(y1)
        self.x2 = int(x2)
        self.y2 = int(y2)
        self.x3 = int(x3)
        self.y3 = int(y3)
        self.color = color
        self.pen_width = pen_width
        self.fill_color = fill_color if fill_color else color

    def draw(self, painter: QPainter):
        painter.setRenderHint(QPainter.RenderHint.Antialiasing, True)
        painter.setBrush(QBrush(QColor(self.fill_color if self.fill_color else self.color)))
        painter.setPen(QPen(self.color, self.pen_width))
        points = QPolygon([
            QPoint(self.x1, self.y1),
            QPoint(self.x2, self.y2),
            QPoint(self.x3, self.y3)
        ])
        painter.drawPolygon(points)


class Square:
    def __init__(self, x, y, width, color=QColor(0, 0, 0), pen_width=1, fill_color=None):
        self.x = int(x)
        self.y = int(y)
        self.width = int(width)
        self.color = color
        self.pen_width = pen_width
        self.fill_color = fill_color if fill_color else None

    def draw(self, painter: QPainter):
        painter.setRenderHint(QPainter.RenderHint.Antialiasing, True)
        painter.setBrush(QBrush(self.fill_color if self.fill_color else self.color))
        painter.setPen(QPen(self.color, self.pen_width))
        painter.drawRect(self.x, self.y, self.width, self.width)


class Star:
    def __init__(self, x, y, outer_radius, inner_radius, color=QColor(0, 0, 0), pen_width=1, fill_color=None):
        self.x = int(x)
        self.y = int(y)
        self.outer_radius = int(outer_radius)
        self.inner_radius = int(inner_radius)
        self.color = color
        self.pen_width = pen_width
        self.fill_color = fill_color if fill_color else None

    def draw(self, painter: QPainter):
        painter.setRenderHint(QPainter.RenderHint.Antialiasing, True)
        painter.setBrush(QBrush(self.fill_color if self.fill_color else self.color))
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
        painter.setRenderHint(QPainter.RenderHint.Antialiasing, True)
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
        except Exception as e:
            raise ValueError(f'Error drawing image: {e}')


class Eraser:
    def __init__(self, x, y, pen_with=1):
        self.x = int(x)
        self.y = int(y)
        self.pen_with = pen_with

    def draw(self, painter: QPainter):
        painter.setRenderHint(QPainter.RenderHint.Antialiasing, True)
        painter.setBrush(QBrush(QColor(240, 240, 240)))
        painter.setPen(QPen(QColor(240, 240, 240), self.pen_with))
        painter.drawEllipse(self.x, self.y, 10, 10)