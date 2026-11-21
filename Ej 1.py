import tkinter as tk

class pruebaexcepciones:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Prueba de excepciones")
        tk.Label(ventana, text="Numero 1:").grid(row=0, column=0, padx=5, pady=5)
        self.numero1 = tk.Entry(ventana)
        self.numero1.grid(row=0, column=1, padx=5, pady=5)
        tk.Label(ventana, text="Numero 2:").grid(row=1, column=0, padx=5, pady=5)
        self.numero2 = tk.Entry(ventana)
        self.numero2.grid(row=1, column=1, padx=5, pady=5)
        self.boton = tk.Button(ventana, text="Ejecutar", command=self.ejecutar)
        self.boton.grid(row=2, column=0, columnspan=2, pady=5)
        self.salida = tk.Text(ventana, width=45, height=14, state="disabled")
        self.salida.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    def limpiar(self):
        self.salida.config(state="normal")
        self.salida.delete("1.0", tk.END)
        self.salida.config(state="disabled")

    def mostrar(self, texto):
        self.salida.config(state="normal")
        self.salida.insert(tk.END, texto + "\n")
        self.salida.config(state="disabled")

    def ejecutar(self):
        self.limpiar()
        self.mostrar("Ingresando al primer try")
        try:
            dividendo = float(self.numero1.get())
            divisor = float(self.numero2.get())
            cociente = dividendo / divisor
            self.mostrar("Cociente: " + str(cociente))
            self.mostrar("Despues de la division")
        except ZeroDivisionError:
            self.mostrar("Division por cero")
        except ValueError:
            self.mostrar("Debe ingresar numeros validos")
        finally:
            self.mostrar("Ingresando al primer finally")

        self.mostrar("")
        self.mostrar("Ingresando al segundo try")
        try:
            objeto = None
            objeto.tostring()
            self.mostrar("Imprimiendo objeto")
        except ZeroDivisionError:
            self.mostrar("Division por cero")
        except Exception as e:
            self.mostrar("Ocurrio una excepcion: " + str(e))
        finally:
            self.mostrar("Ingresando al segundo finally")

ventana = tk.Tk()
aplicacion = pruebaexcepciones(ventana)
ventana.mainloop()