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
        barra.setIconSize(QSize(16,16))

    #<--- Estilos en la paqueteria de QT del que prefieran --->

        #barra.setToolButtonStyle(Qt.ToolButtonFollowStyle)
        #barra.setToolButtonStyle(Qt.ToolButtonTextOnly)
        #barra.setToolButtonStyle(Qt.ToolButtonIconOnly)
        barra.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        #barra.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.addToolBar(barra)

    #<--- Boton Nuevo --->
        boton_nuevo = QAction(QIcon('Src/nuevo.png'),'Nuevo', self)
        barra.addAction(boton_nuevo)
        self.setStatusBar(QStatusBar(self))
        boton_nuevo.setStatusTip('Nuevo Archivo')
        boton_nuevo.triggered.connect(self.clik_barraNuevo)
        #boton_nuevo.setCheckable(True)

    # <--- Boton Guardar --->
        boton_guardar = QAction(QIcon('Src/guardar.png'),'Guardar', self)
        barra.addAction(boton_guardar)
        boton_guardar.setStatusTip('Guardar Archivo')
        boton_guardar.triggered.connect(self.clik_barraGuardar)

    # <--- Funcionalidades de cada boton --->
    def clik_barraGuardar(self, s):
        print(f'Guardando Arcvhivo... {s}')

    def clik_barraNuevo(self, s):
        print(f'Nuevo Archivo {s}')


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()