import tkinter as tk
from tkinter import messagebox


class programador:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos


class equipomaratonprogramacion:
    def __init__(self, nombreequipo, universidad, lenguajeprogramacion):
        self.nombreequipo = nombreequipo
        self.universidad = universidad
        self.lenguajeprogramacion = lenguajeprogramacion
        self.tamanoequipo = 0
        self.programadores = [None] * 3

    def estalleno(self):
        return self.tamanoequipo == len(self.programadores)

    def anadir(self, programador):
        if self.estalleno():
            raise Exception("El equipo esta completo. No se pudo agregar programador.")
        self.programadores[self.tamanoequipo] = programador
        self.tamanoequipo += 1

    @staticmethod
    def validarcampo(campo):
        if len(campo.strip()) == 0:
            raise Exception("El campo no puede estar vacio.")
        for c in campo:
            if c.isdigit():
                raise Exception("El nombre no puede tener digitos.")
        if len(campo) > 20:
            raise Exception("La longitud no debe ser superior a 20 caracteres.")


class interfazmaraton:
    def __init__(self, ventana):
        self.ventana = ventana
        self.equipo = None
        self.ventana.title("Maraton de programacion")

        self.marcoequipo = tk.LabelFrame(ventana, text="Datos del equipo", padx=10, pady=10)
        self.marcoequipo.pack(fill="x", padx=15, pady=(15, 10))

        tk.Label(self.marcoequipo, text="Nombre del equipo =").grid(row=0, column=0, sticky="e", pady=3)
        self.entradanombreequipo = tk.Entry(self.marcoequipo, width=25)
        self.entradanombreequipo.grid(row=0, column=1, padx=5)

        tk.Label(self.marcoequipo, text="Universidad =").grid(row=1, column=0, sticky="e", pady=3)
        self.entradauniversidad = tk.Entry(self.marcoequipo, width=25)
        self.entradauniversidad.grid(row=1, column=1, padx=5)

        tk.Label(self.marcoequipo, text="Lenguaje de programacion =").grid(row=2, column=0, sticky="e", pady=3)
        self.entradalenguaje = tk.Entry(self.marcoequipo, width=25)
        self.entradalenguaje.grid(row=2, column=1, padx=5)

        self.botoncrearequipo = tk.Button(self.marcoequipo, text="Crear equipo", command=self.crearequipo)
        self.botoncrearequipo.grid(row=3, column=0, columnspan=2, pady=(10, 0))

        self.marcointegrantes = tk.LabelFrame(ventana, text="Datos de los integrantes del equipo", padx=10, pady=10)
        self.marcointegrantes.pack(fill="x", padx=15, pady=10)

        tk.Label(self.marcointegrantes, text="Nombre del integrante =").grid(row=0, column=0, sticky="e", pady=3)
        self.entradanombreprogramador = tk.Entry(self.marcointegrantes, width=25, state="disabled")
        self.entradanombreprogramador.grid(row=0, column=1, padx=5)

        tk.Label(self.marcointegrantes, text="Apellidos del integrante =").grid(row=1, column=0, sticky="e", pady=3)
        self.entradaapellidosprogramador = tk.Entry(self.marcointegrantes, width=25, state="disabled")
        self.entradaapellidosprogramador.grid(row=1, column=1, padx=5)

        self.botonanadir = tk.Button(self.marcointegrantes, text="Anadir integrante", command=self.anadirintegrante, state="disabled")
        self.botonanadir.grid(row=2, column=0, columnspan=2, pady=(10, 0))

        self.marcoresumen = tk.LabelFrame(ventana, text="Equipo", padx=10, pady=10)
        self.marcoresumen.pack(fill="both", expand=True, padx=15, pady=(10, 15))

        self.etiquetaresumen = tk.Label(self.marcoresumen, text="Equipo no creado", justify="left")
        self.etiquetaresumen.pack(anchor="w")

        self.listaintegrantes = tk.Listbox(self.marcoresumen, height=6)
        self.listaintegrantes.pack(fill="both", expand=True, pady=(8, 0))

    def crearequipo(self):
        try:
            nombreequipo = self.entradanombreequipo.get()
            universidad = self.entradauniversidad.get()
            lenguaje = self.entradalenguaje.get()
            if len(nombreequipo.strip()) == 0 or len(universidad.strip()) == 0 or len(lenguaje.strip()) == 0:
                raise Exception("Debe completar todos los datos del equipo.")
            self.equipo = equipomaratonprogramacion(nombreequipo, universidad, lenguaje)
            self.entradanombreequipo.config(state="disabled")
            self.entradauniversidad.config(state="disabled")
            self.entradalenguaje.config(state="disabled")
            self.botoncrearequipo.config(state="disabled")
            self.entradanombreprogramador.config(state="normal")
            self.entradaapellidosprogramador.config(state="normal")
            self.botonanadir.config(state="normal")
            self.etiquetaresumen.config(text="Equipo: " + nombreequipo + "\nUniversidad: " + universidad + "\nLenguaje: " + lenguaje)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def anadirintegrante(self):
        try:
            nombreprogramador = self.entradanombreprogramador.get()
            equipomaratonprogramacion.validarcampo(nombreprogramador)
            apellidosprogramador = self.entradaapellidosprogramador.get()
            equipomaratonprogramacion.validarcampo(apellidosprogramador)
            nuevoprogramador = programador(nombreprogramador, apellidosprogramador)
            self.equipo.anadir(nuevoprogramador)
            self.listaintegrantes.insert(tk.END, str(self.equipo.tamanoequipo) + ". " + nombreprogramador + " " + apellidosprogramador)
            self.entradanombreprogramador.delete(0, tk.END)
            self.entradaapellidosprogramador.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Error", str(e))


ventana = tk.Tk()
aplicacion = interfazmaraton(ventana)
ventana.mainloop()