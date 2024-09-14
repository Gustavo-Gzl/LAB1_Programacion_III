"""
ejercicio #1
Construir un programa que muestre una ventana en la cual aparezca su nombre completo y su edad centrados.

Descripción del programa:
Este programa muestra una ventana con el nombre completo y la edad de los integrantes del grupo, ambos centrados 
en la ventana. Utilizamos "QLabel" para mostrar el texto y un "QVBoxLayout" para organizar los elementos de manera vertical.

¿Qué problema resuelve?
El programa resuelve el problema de presentar información estática en una interfaz gráfica de manera simple y clara. 
"""


import sys
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

class VentanaNombreEdad(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Nombre y Edad Centrados')
        layout = QVBoxLayout()

        # Crear etiquetas con el nombre y la edad
        nombre = QLabel("Elmer Gustavo Gonzalez")
        edad = QLabel("28 años")

        # Centrar las etiquetas
        nombre.setAlignment(Qt.AlignCenter)
        edad.setAlignment(Qt.AlignCenter)

        # Agregar las etiquetas al layout
        layout.addWidget(nombre)
        layout.addWidget(edad)

        self.setLayout(layout)

# Configuración de la ventana principal
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaNombreEdad()
    ventana.show()
    sys.exit(app.exec_())


