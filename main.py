import sys
from random import randint
from PyQt5 import uic
from PyQt5.QtCore import Qt, QPoint
from UI import Ui_Form
from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtGui import QPainter, QBrush, QPen, QColor, QPolygon


class MyWidget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def draw_flag(self, qp):
        n = randint(2, 9)
        for i in range(n):
            qp.setBrush(QColor(randint(1, 255), randint(1, 255), randint(1, 255)))
            r = randint(20, 200)
            qp.drawEllipse(randint(1, 600), randint(1, 300), r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
