# coding:utf-8
from PyQt5.QtCore import QCoreApplication, QEvent, Qt
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QWidget

from ..utils.linux_utils import LinuxMoveResize
from .window_effect import UnixWindowEffect


class UnixFramelessWindow(QWidget):
    """ Frameless window for Unix system """

    BORDER_WIDTH = 5

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.windowEffect = UnixWindowEffect()

        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        QCoreApplication.instance().installEventFilter(self)

        self.resize(500, 500)

    def resizeEvent(self, e):
        super().resizeEvent(e)

    def setTitleBar(self, titleBar):
        """ set custom title bar

        Parameters
        ----------
        titleBar: TitleBar
            title bar
        """


    def eventFilter(self, obj, event):
        et = event.type()
        if et != QEvent.MouseButtonPress and et != QEvent.MouseMove:
            return False

        edges = Qt.Edges()
        pos = QMouseEvent(event).globalPos() - self.pos()
        if pos.x() < self.BORDER_WIDTH:
            edges |= Qt.LeftEdge
        if pos.x() >= self.width()-self.BORDER_WIDTH:
            edges |= Qt.RightEdge
        if pos.y() < self.BORDER_WIDTH:
            edges |= Qt.TopEdge
        if pos.y() >= self.height()-self.BORDER_WIDTH:
            edges |= Qt.BottomEdge

        # change cursor
        if et == QEvent.MouseMove and self.windowState() == Qt.WindowNoState:
            if edges in (Qt.LeftEdge | Qt.TopEdge, Qt.RightEdge | Qt.BottomEdge):
                self.setCursor(Qt.SizeFDiagCursor)
            elif edges in (Qt.RightEdge | Qt.TopEdge, Qt.LeftEdge | Qt.BottomEdge):
                self.setCursor(Qt.SizeBDiagCursor)
            elif edges in (Qt.TopEdge, Qt.BottomEdge):
                self.setCursor(Qt.SizeVerCursor)
            elif edges in (Qt.LeftEdge, Qt.RightEdge):
                self.setCursor(Qt.SizeHorCursor)
            else:
                self.setCursor(Qt.ArrowCursor)


        return super().eventFilter(obj, event)
