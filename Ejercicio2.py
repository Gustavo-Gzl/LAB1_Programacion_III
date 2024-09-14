"""
Ejercicio #2
Construir un programa que muestre una ventana y que lea una clave secreta sin mostrar los caracteres que la componen.

Descripción del programa:
Este programa crea una ventana con un campo de entrada para que el usuario ingrese una clave secreta. 
Mientras se escriben los caracteres, estos no se muestran en la pantalla por razones de seguridad, 
gracias al uso de la función setEchoMode(QLineEdit.Password) y al finalizar la ejecucion de la clave secreta con ENTER
se cierra la ventana.

¿Qué problema resuelve?
Este programa resuelve el problema de la seguridad y privacidad al introducir información confidencial, 
como contraseñas o claves secretas. Al ocultar los caracteres mientras el usuario escribe, se protege 
la información de miradas indiscretas o accesos no deseados.
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt

class ClaveSecreta(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Clave Secreta')

        layout = QVBoxLayout()

        # Etiqueta para la clave secreta
        label = QLabel("Introduce la clave secreta:")
        layout.addWidget(label)

        # Campo de texto con ocultamiento de caracteres
        self.clave = QLineEdit(self)
        self.clave.setEchoMode(QLineEdit.Password)  # Oculta los caracteres
        layout.addWidget(self.clave)

        self.setLayout(layout)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.close()  # Cierra la ventana si se presiona Enter o Return

# Configuración de la ventana principal
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = ClaveSecreta()
    ventana.show()
    sys.exit(app.exec_())
