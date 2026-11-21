import math
import tkinter as tk
from tkinter import messagebox


class calculosnumericos:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Calculos numericos")
        self.etiquetavalor = tk.Label(ventana, text="Valor numerico =")
        self.etiquetavalor.pack(pady=(20, 5))

        self.entrada = tk.Entry(ventana, justify="center", width=25)
        self.entrada.pack(pady=5)

        self.marcobotones = tk.Frame(ventana)
        self.marcobotones.pack(pady=15)

        self.botonlogaritmo = tk.Button(self.marcobotones, text="Logaritmo neperiano", command=self.calcularlogaritmoneperiano)
        self.botonlogaritmo.grid(row=0, column=0, padx=5)

        self.botonraiz = tk.Button(self.marcobotones, text="Raiz cuadrada", command=self.calcularraizcuadrada)
        self.botonraiz.grid(row=0, column=1, padx=5)

        self.resultado = tk.Label(ventana, text="Resultado =")
        self.resultado.pack(pady=10)

    def calcularlogaritmoneperiano(self):
        try:
            valor = float(self.entrada.get())
            if valor <= 0:
                raise ArithmeticError("El valor debe ser un numero positivo")
            resultado = math.log(valor)
            self.resultado.config(text="Resultado = " + str(resultado))
        except ArithmeticError:
            messagebox.showerror("Error", "El valor debe ser un numero positivo para calcular el logaritmo")
        except ValueError:
            messagebox.showerror("Error", "El valor debe ser numerico para calcular el logaritmo")

    def calcularraizcuadrada(self):
        try:
            valor = float(self.entrada.get())
            if valor < 0:
                raise ArithmeticError("El valor debe ser un numero positivo")
            resultado = math.sqrt(valor)
            self.resultado.config(text="Resultado = " + str(resultado))
        except ArithmeticError:
            messagebox.showerror("Error", "El valor debe ser un numero positivo para calcular la raiz cuadrada")
        except ValueError:
            messagebox.showerror("Error", "El valor debe ser numerico para calcular la raiz cuadrada")


ventana = tk.Tk()
aplicacion = calculosnumericos(ventana)
ventana.mainloop()