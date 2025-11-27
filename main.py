from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Menu con PySide')
        etiqueta = QLabel('Etiqueta')
        etiqueta.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(etiqueta)

        barra = QToolBar('Barra de Herramientas')
        self.addToolBar(barra)

        boton_accion = QAction('Boton', self)
        barra.addAction(boton_accion)

        self.setStatusBar(QStatusBar(self))
        boton_accion.setStatusTip('Boton de la barra')

        boton_accion.triggered.connect(self.clik_barra)
        boton_accion.setCheckable(True)

    def clik_barra(self, s):
        print(f'Prueba de click {s}')


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()