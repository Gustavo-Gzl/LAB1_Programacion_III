import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QRadioButton, QComboBox, QPushButton, QMessageBox

# Aca se muestran los datos ingresados
def mostrar_datos():
    equipo = combo_equipos.currentText()  # Obtener equipo seleccionado
    if radio_4_4_2.isChecked():
        alineacion = "4-4-2"
    elif radio_4_3_3.isChecked():
        alineacion = "4-3-3"
    else:
        alineacion = "5-3-2"

    # Mostrar mensaje con los datos
    mensaje = f"Equipo: {equipo}\nAlineación: {alineacion}"
    QMessageBox.information(None, "Datos del equipo", mensaje)

# Ventana principal
class VentanaFutbol(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Combobox para seleccionar equipo
        layout.addWidget(QLabel("Seleccione su equipo:"))
        global combo_equipos
        combo_equipos = QComboBox()
        combo_equipos.addItems(["Barcelona", "Real Madrid", "Liverpool"])
        layout.addWidget(combo_equipos)

        # Radiobutton y aca se selecciona la alineación
        layout.addWidget(QLabel("Seleccione la alineación:"))
        global radio_4_4_2, radio_4_3_3, radio_5_3_2
        radio_4_4_2 = QRadioButton("4-4-2")
        radio_4_3_3 = QRadioButton("4-3-3")
        radio_5_3_2 = QRadioButton("5-3-2")
        radio_4_4_2.setChecked(True)
        layout.addWidget(radio_4_4_2)
        layout.addWidget(radio_4_3_3)
        layout.addWidget(radio_5_3_2)

        # para mostrar datos
        boton = QPushButton("Mostrar Datos")
        boton.clicked.connect(mostrar_datos)
        layout.addWidget(boton)

        self.setLayout(layout)
        self.setWindowTitle('Datos de Fútbol')
        self.show()

# Ejecutar aplicación
app = QApplication(sys.argv)
ventana = VentanaFutbol()
sys.exit(app.exec_())
