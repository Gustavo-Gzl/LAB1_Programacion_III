"""
Ejercicio #3
Construir un programa que muestre una ventana a través de la cual se pueda leer su número de cédula y su nombre completo.
Descripción del programa:
Este programa presenta una ventana donde el usuario puede ingresar su número de cédula y su nombre completo. 
Usa dos campos de texto (QLineEdit) para capturar esta información y etiquetas (QLabel) para describir qué 
información se debe introducir. En este ejercicio capturamos los datos de los integrantes del grupo. y al finalizar 
la ejecucion de la clave secreta con ENTER se cierra la ventana. 

¿Qué problema resuelve?
El programa resuelve el problema de capturar información personal de manera clara y sencilla. 
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt

class VentanaCedulaNombre(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Leer Cédula y Nombre')

        layout = QVBoxLayout()

        # Etiqueta y campo para el número de cédula
        label_cedula = QLabel("Número de cédula:")
        layout.addWidget(label_cedula)
        self.cedula = QLineEdit(self)
        layout.addWidget(self.cedula)

        # Etiqueta y campo para el nombre completo
        label_nombre = QLabel("Nombre completo:")
        layout.addWidget(label_nombre)
        self.nombre = QLineEdit(self)
        layout.addWidget(self.nombre)

        self.setLayout(layout)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.close()  # Cierra la ventana si se presiona Enter o Return
        else:
            super().keyPressEvent(event)  

# Configuración de la ventana principal
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaCedulaNombre()
    ventana.show()
    sys.exit(app.exec_())

