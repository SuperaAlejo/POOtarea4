import ttkbootstrap as tb
from ttkbootstrap.constants import *
import numpy as np

class Figura:
    def area(self) -> float:
        pass

    def volumen(self) -> float:
        pass

class Cilindro(Figura):
    def __init__(self, radio, altura):
        self.radio = radio
        self.altura = altura

    def area(self):
        return 2 * np.pi * self.radio * (self.radio + self.altura)

    def volumen(self):
        return np.pi * self.radio**2 * self.altura

class Esfera(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 4 * np.pi * self.radio**2

    def volumen(self):
        return (4/3) * np.pi * self.radio**3

class Piramide(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base**2 + 2 * self.base * np.sqrt((self.base/2)**2 + self.altura**2)

    def volumen(self):
        return (1/3) * self.base**2 * self.altura

# ---------- VENTANAS ----------
class VentanaFigura:
    def __init__(self, titulo, campos, constructor, app):
        self.constructor = constructor
        self.campos = campos
        self.ventana = tb.Toplevel(title=titulo)
        self.ventana.geometry("300x300")
        self.ventana.resizable(False, False)
        self.entradas = {}

        self.ventana.columnconfigure(0, weight=1)
        self.ventana.columnconfigure(1, weight=1)

        tb.Label(self.ventana, text=f"Ingrese los parámetros de {titulo.lower()}", bootstyle="info",
                 wraplength=280, justify="center").grid(row=0, column=0, columnspan=2, padx=10, pady=20)

        for idx, campo in enumerate(campos):
            tb.Label(self.ventana, text=f"{campo} (cm):").grid(row=idx+1, column=0, sticky="e", padx=5, pady=5)
            entrada = tb.Entry(self.ventana, width=10)
            entrada.grid(row=idx+1, column=1, sticky="w", padx=5, pady=5)
            self.entradas[campo] = entrada

        self.resultado_volumen = tb.Label(self.ventana, text="", bootstyle="success")
        self.resultado_area = tb.Label(self.ventana, text="", bootstyle="success")
        self.resultado_volumen.grid(row=len(campos)+2, column=0, columnspan=2, pady=(20, 0))
        self.resultado_area.grid(row=len(campos)+3, column=0, columnspan=2, pady=(5, 10))

        calcular_btn = tb.Button(self.ventana, text="Calcular", width=15, bootstyle="success",
                                 command=self.calcular)
        calcular_btn.grid(row=len(campos)+1, column=0, columnspan=2, pady=10)

    def calcular(self):
        try:
            valores = [float(self.entradas[campo].get()) for campo in self.campos]
            figura = self.constructor(*valores)
            self.resultado_volumen.config(text=f"Volumen: {figura.volumen():.2f} cm³", bootstyle="success")
            self.resultado_area.config(text=f"Área: {figura.area():.2f} cm²", bootstyle="success")
        except ValueError:
            self.resultado_volumen.config(text="⚠️ Por favor ingresa valores válidos.", bootstyle="warning")
            self.resultado_area.config(text="")

# ---------- APLICACIÓN PRINCIPAL ----------
class Aplicacion:
    def __init__(self):
        self.app = tb.Window(themename="darkly")
        self.app.title("Calculadora de Volúmenes y Áreas")
        self.app.geometry("500x400")

        frame = tb.Frame(self.app, padding=20)
        frame.pack(anchor="n", pady=20)

        tb.Label(frame,
                 text="📐 Calculadora de Volúmenes y Áreas",
                 font=("Segoe UI", 18),
                 bootstyle="info").grid(row=0, column=0, columnspan=3, pady=(20, 30))

        tb.Separator(frame, bootstyle="secondary").grid(
            row=1, column=0, columnspan=3, sticky="ew", padx=10, pady=(0, 10))

        tb.Label(frame,
                 text="Selecciona una figura para calcular su volumen y área.",
                 wraplength=280, justify="center", bootstyle="info"
                 ).grid(row=2, column=0, columnspan=3, padx=10, pady=10)

        tb.Button(frame, text="Cilindro", bootstyle="primary", width=17,
                  command=lambda: VentanaFigura("Cilindro", ["Altura", "Radio"], Cilindro, self.app)
                  ).grid(column=0, row=3, padx=5, pady=10)

        tb.Button(frame, text="Esfera", bootstyle="primary", width=17,
                  command=lambda: VentanaFigura("Esfera", ["Radio"], Esfera, self.app)
                  ).grid(column=1, row=3, padx=5, pady=10)

        tb.Button(frame, text="Pirámide", bootstyle="primary", width=17,
                  command=lambda: VentanaFigura("Pirámide", ["Altura", "Base"], Piramide, self.app)
                  ).grid(column=2, row=3, padx=5, pady=10)

        tb.Button(frame, text="Cerrar aplicación", bootstyle="danger", command=self.app.destroy
                  ).grid(column=1, row=4, padx=10, pady=30)

    def ejecutar(self):
        self.app.mainloop()

if __name__ == "__main__":
    Aplicacion().ejecutar()
