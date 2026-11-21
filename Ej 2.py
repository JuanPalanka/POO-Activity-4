import tkinter as tk
from tkinter import messagebox
class Vendedor:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = 0
    def verificarEdad(self, edad):
        if edad < 18 and edad>0:
            raise ValueError("El vendedor debe ser mayor de 18 años.")
        if edad >= 0 and edad < 120:
            self.edad = edad
        else:
            raise ValueError("La edad no puede ser negativa ni mayor a 120.")
    def imprimir(self):
        return (
            f"Nombre del vendedor: {self.nombre}\n"
            f"Apellidos del vendedor: {self.apellidos}\n"
            f"Edad del vendedor: {self.edad}"
        )
def registrar_vendedor():
    nombre = entrada_nombre.get()
    apellidos = entrada_apellidos.get()
    edad_texto = entrada_edad.get()
    if not nombre or not apellidos or not edad_texto:
        messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")
        return
    try:
        edad = int(edad_texto)

        vendedor = Vendedor(nombre, apellidos)
        vendedor.verificarEdad(edad)

        messagebox.showinfo("Datos del vendedor", vendedor.imprimir())
    except ValueError as e:
        messagebox.showerror("Error", str(e))
ventana = tk.Tk()
ventana.title("Registro de Vendedor")
titulo = tk.Label(ventana, text="REGISTRO DE VENDEDOR")
titulo.pack(pady=20)
tk.Label(ventana, text="Nombre del vendedor:").pack()
entrada_nombre = tk.Entry(ventana, width=35)
entrada_nombre.pack(pady=5)
tk.Label(ventana, text="Apellidos del vendedor:").pack()
entrada_apellidos = tk.Entry(ventana, width=35)
entrada_apellidos.pack(pady=5)
tk.Label(ventana, text="Edad del vendedor:").pack()
entrada_edad = tk.Entry(ventana, width=35)
entrada_edad.pack(pady=5)
boton_registrar = tk.Button(
    ventana,
    text="Registrar vendedor",
    command=registrar_vendedor,
    bg="#AF4C4C",
    fg="white",
    font=("Arial", 10, "bold")
)
boton_registrar.pack(pady=20)
ventana.mainloop()