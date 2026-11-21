import tkinter as tk
from tkinter import messagebox


class leerarchivo:
    def __init__(self, ventana):
        self.ventana = ventana
        self.nombrearchivo = "C:\prueba.txt.txt"
        self.ventana.title("Leer archivo")
        self.ventana.geometry("480x380")

        self.etiquetaarchivo = tk.Label(ventana, text="Archivo = " + self.nombrearchivo)
        self.etiquetaarchivo.pack(pady=(15, 5))

        self.botonleer = tk.Button(ventana, text="Leer archivo", command=self.leer)
        self.botonleer.pack(pady=5)

        self.marcotexto = tk.Frame(ventana)
        self.marcotexto.pack(fill="both", expand=True, padx=15, pady=15)

        self.barra = tk.Scrollbar(self.marcotexto)
        self.barra.pack(side="right", fill="y")

        self.areatexto = tk.Text(self.marcotexto, state="disabled", yscrollcommand=self.barra.set)
        self.areatexto.pack(side="left", fill="both", expand=True)
        self.barra.config(command=self.areatexto.yview)

    def leer(self):
        try:
            with open(self.nombrearchivo, "r", encoding="utf-8") as archivo:
                contenido = archivo.read()
            self.areatexto.config(state="normal")
            self.areatexto.delete("1.0", tk.END)
            self.areatexto.insert(tk.END, contenido)
            self.areatexto.config(state="disabled")
        except (OSError, UnicodeDecodeError):
            messagebox.showerror("Error", "No se pudo leer el archivo.")


ventana = tk.Tk()
aplicacion = leerarchivo(ventana)
ventana.mainloop()