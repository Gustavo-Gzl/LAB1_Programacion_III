import tkinter as tk
from tkinter import messagebox

#  para mostrar los datos de la persona
def mostrar_datos():
    datos = {
        "Nombre": nombre.get(),
        "Apellido": apellido.get(),
        "Edad": edad.get(),
        "Género": genero.get(),
        "Dirección": direccion.get(),
        "Teléfono": telefono.get(),
        "Correo electrónico": correo.get(),
        "Ocupación": ocupacion.get(),
        "Nacionalidad": nacionalidad.get(),
        "Estado civil": estado_civil.get()
    }
    mensaje = "\n".join([f"{campo}: {valor}" for campo, valor in datos.items()])
    messagebox.showinfo("Datos de la Persona", mensaje)

# Crear ventana
ventana = tk.Tk()
ventana.title("Datos de una Persona")

# entradas de datos
def crear_entrada(fila, etiqueta):
    tk.Label(ventana, text=etiqueta).grid(row=fila, column=0, padx=5, pady=5)
    entrada = tk.Entry(ventana)
    entrada.grid(row=fila, column=1)
    return entrada

# Entradas para los 10 datos característicos
nombre = crear_entrada(0, "Nombre")
apellido = crear_entrada(1, "Apellido")
edad = crear_entrada(2, "Edad")
genero = crear_entrada(3, "Género")
direccion = crear_entrada(4, "Dirección")
telefono = crear_entrada(5, "Teléfono")
correo = crear_entrada(6, "Correo electrónico")
ocupacion = crear_entrada(7, "Ocupación")
nacionalidad = crear_entrada(8, "Nacionalidad")
estado_civil = crear_entrada(9, "Estado civil")

# Botón para mostrar los datos(los imprime y los muestra)
tk.Button(ventana, text="Mostrar Datos", command=mostrar_datos).grid(row=10, column=0, columnspan=2, pady=10)

# Ejecutar la ventana
ventana.mainloop()
