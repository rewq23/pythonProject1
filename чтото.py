import sys
import requests
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic
from PyQt5.QtCore import Qt

SCREEN_SIZE = [600, 450]
COEFF_SCALING = 2


class NoMapException(BaseException):
    pass


class Example(QWidget):
    static_uri = 'http://static-maps.yandex.ru/1.x/'


def __init__(self):
    super().__init__()
    uic.loadUi('ui.ui', self)
    self.coords = [37.530887, 55.7031181]
    self.scale = 0.002
    self.map_type = 'map'
    self.getImage(self.coords, self.scale)


def getImage(self, coords, scale):
    map_request = "http://static-maps.yandex.ru/1.x/?ll=37.530887,55.703118&spn=0.002,0.002&l=map"
    # response = requests.get(map_request)
    params = {
        'll': ','.join(map(str, coords)),
        'spn': f'{scale},{scale}',
        'l': self.map_type
    }
    response = requests.get(self.static_uri, params=params)

    if not response:
        raise NoMapException

    self.map = response.content
    self.pixmap = QPixmap()
    self.pixmap.loadFromData(self.map, 'PNG')
    self.image.setPixmap(self.pixmap)


def keyPressEvent(self, a0):
    if a0.key() in (Qt.Key_PageUp, Qt.Key_PageDown):
        if a0.key() == Qt.Key_PageUp:
            new_scale = self.scale / COEFF_SCALING
        else:
            new_scale = self.scale * COEFF_SCALING
        try:
            self.getImage(self.coords, new_scale)
        except NoMapException:
            pass
        else:
            self.scale = new_scale


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
