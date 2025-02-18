from math import atan2, cos, sin, radians, sqrt

from PyQt6.QtCore import QPoint, QPointF, Qt
from PyQt6.QtGui import QBrush, QColor, QPainter, QPen, QPixmap, QPolygon, QFontMetrics


class ShapeMixin:
    def contains(self, point: QPointF) -> bool:
        """Проверяет, содержит ли фигура указанную точку."""
        raise NotImplementedError

    def move(self, dx: int, dy: int):
        """Перемещает фигуру на заданные координаты."""
        raise NotImplementedError


class BrushPoint(ShapeMixin):
    def __init__(self, x: int, y: int, color=QColor(0, 0, 0), pen_width=1):
        self.x = int(x)
        self.y = int(y)
        self.color = color
        self.pen_width = pen_width

    def draw(self, painter: QPainter):
        painter.setRenderHint(QPainter.RenderHint.Antialiasing, True)
        painter.setBrush(QBrush(self.color))
        painter.setPen(QPen(self.color, self.pen_width))
        painter.drawEllipse(self.x - 5, self.y - 5, 10, 10)

    def contains(self, point: QPointF) -> bool:
        return sqrt((point.x() - self.x) ** 2 + (point.y() - self.y) ** 2) <= 5


class Line(ShapeMixin):
    def __init__(self, sx: int, sy: int, ex: int, ey: int, color=QColor(0, 0, 0), pen_width=1, fill_color=None):
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

    def contains(self, point: QPointF) -> bool:
        # Простая проверка на принадлежность точки линии
        def distance_to_line(px, py, x1, y1, x2, y2):
            return abs((y2 - y1) * px - (x2 - x1) * py + x2 * y1 - y2 * x1) / sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)

        return distance_to_line(point.x(), point.y(), self.sx, self.sy, self.ex, self.ey) <= self.pen_width


class Circle(ShapeMixin):
    def __init__(self, cx: int, cy: int, x: int, y: int, color=QColor(0, 0, 0), pen_width=1, fill_color=None):
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

    def contains(self, point: QPointF) -> bool:
        radius = ((self.cx - self.x) ** 2 + (self.cy - self.y) ** 2) ** 0.5
        distance = ((point.x() - self.cx) ** 2 + (point.y() - self.cy) ** 2) ** 0.5
        return distance <= radius


class Triangle(ShapeMixin):
    def __init__(self, x1: int, y1: int, x2: int, y2: int, x3: int, y3: int, color=QColor(0, 0, 0), pen_width=1,
                 fill_color=None):
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

    def contains(self, point: QPointF) -> bool:
        def sign(p1, p2, p3):
            return (p1.x() - p3.x()) * (p2.y() - p3.y()) - (p2.x() - p3.x()) * (p1.y() - p3.y())

        b1 = sign(point, QPoint(self.x1, self.y1), QPoint(self.x2, self.y2)) < 0.0
        b2 = sign(point, QPoint(self.x2, self.y2), QPoint(self.x3, self.y3)) < 0.0
        b3 = sign(point, QPoint(self.x3, self.y3), QPoint(self.x1, self.y1)) < 0.0

        return (b1 == b2) and (b2 == b3)


class Square(ShapeMixin):
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

    def contains(self, point: QPointF) -> bool:
        return self.x <= point.x() <= self.x + self.width and self.y <= point.y() <= self.y + self.width


class Star(ShapeMixin):
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
            r = self.outer_radius if i % 2 == 0 else self.inner_radius
            x = self.x + r * cos(radians(angle))
            y = self.y - r * sin(radians(angle))
            points.append(QPointF(x, y))
            angle += 36
        painter.drawPolygon(points)

    def contains(self, point: QPointF) -> bool:
        # Проверка на принадлежность точки звезде через полигоны
        polygon = QPolygon([QPoint(int(p.x()), int(p.y())) for p in points])
        return polygon.containsPoint(point, Qt.FillRule.OddEvenFill)


class Arrow(ShapeMixin):
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

    def contains(self, point: QPointF) -> bool:
        # Проверка на принадлежность точки стрелке
        def distance_to_line(px, py, x1, y1, x2, y2):
            return abs((y2 - y1) * px - (x2 - x1) * py + x2 * y1 - y2 * x1) / sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)

        return distance_to_line(point.x(), point.y(), self.sx, self.sy, self.ex, self.ey) <= self.pen_width


class Text(ShapeMixin):
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

    def contains(self, point: QPointF) -> bool:
        # Проверка на принадлежность точки тексту
        metrics = QFontMetrics(self.font)
        rect = metrics.boundingRect(self.text)
        return rect.contains(point.x() - self.x, point.y() - self.y)


class Image(ShapeMixin):
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

    def contains(self, point: QPointF) -> bool:
        return self.x <= point.x() <= self.x + self.width and self.y <= point.y() <= self.y + self.height


class Eraser(ShapeMixin):
    def __init__(self, x, y, pen_with=1):
        self.x = int(x)
        self.y = int(y)
        self.pen_with = pen_with

    def draw(self, painter: QPainter):
        painter.setRenderHint(QPainter.RenderHint.Antialiasing, True)
        painter.setBrush(QBrush(QColor(240, 240, 240)))
        painter.setPen(QPen(QColor(240, 240, 240), self.pen_with))
        painter.drawEllipse(self.x, self.y, 10, 10)

    def contains(self, point: QPointF) -> bool:
        return sqrt((point.x() - self.x) ** 2 + (point.y() - self.y) ** 2) <= 5
