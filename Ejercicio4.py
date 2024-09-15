import tkinter as tk
from tkinter import messagebox

# Esta funcion muestra los datos de las mascotas
def mostrar_datos():
    mascotas = [
        {"Nombre": nombre1.get(), "Raza": raza1.get(), "Edad": edad1.get()},
        {"Nombre": nombre2.get(), "Raza": raza2.get(), "Edad": edad2.get()}
    ]
    mensaje = "\n".join([f"Mascota {i+1}: {m}" for i, m in enumerate(mascotas)])
    messagebox.showinfo("Datos de las Mascotas", mensaje)

# ventana de tk ventana
ventana = tk.Tk()
ventana.title("Datos de Mascotas")

# de datosaqui es la aentrada de datos
def crear_entrada(fila, etiqueta):
    tk.Label(ventana, text=etiqueta).grid(row=fila, column=0)
    entrada = tk.Entry(ventana)
    entrada.grid(row=fila, column=1)
    return entrada

# Datos para dos mascotas
nombre1, raza1, edad1 = crear_entrada(0, "Nombre Mascota 1"), crear_entrada(1, "Raza"), crear_entrada(2, "Edad")
nombre2, raza2, edad2 = crear_entrada(3, "Nombre Mascota 2"), crear_entrada(4, "Raza"), crear_entrada(5, "Edad")

# Botón para mostrar los datos
tk.Button(ventana, text="Mostrar Datos", command=mostrar_datos).grid(row=6, column=0, columnspan=2)

ventana.mainloop()
