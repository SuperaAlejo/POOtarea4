import ttkbootstrap as tb
from ttkbootstrap.constants import *

class Estadisticas:
    @staticmethod
    def promedio(nums):
        return sum(nums) / len(nums)

    @staticmethod
    def desviacion_estandar(nums):
        prom = Estadisticas.promedio(nums)
        varianza = sum((x - prom) ** 2 for x in nums) / len(nums)
        return varianza ** 0.5

    @staticmethod
    def valor_mayor(nums):
        return max(nums)

    @staticmethod
    def valor_menor(nums):
        return min(nums)


class CalculadoraPromedioApp:
    def __init__(self):
        self.ventana = tb.Window(themename="darkly")
        self.ventana.title("Calculadora de Promedio")
        self.ventana.geometry("360x650")

        self.entradas = []
        self._crear_interfaz()

        self.ventana.mainloop()

    def _crear_interfaz(self):
        frame = tb.Frame(self.ventana, padding=20)
        frame.pack(anchor="n", pady=10)

        tb.Label(
            frame,
            text="📝 Calculadora de Promedio",
            font=("Segoe UI", 18),
            bootstyle="info",
            justify="center",
            wraplength=500
        ).grid(row=0, column=0, columnspan=3, pady=(20, 30))

        tb.Separator(frame, bootstyle="secondary").grid(
            row=1, column=0, columnspan=3, sticky="ew", padx=10, pady=(0, 10)
        )

        tb.Label(
            frame,
            text="Ingrese 5 notas para consultar el promedio, la desviación estándar, la mayor y menor nota.",
            wraplength=280,
            justify="center",
            bootstyle="info",
        ).grid(row=2, column=0, columnspan=2, padx=10, pady=30)

        for i in range(5):
            tb.Label(frame, text=f"Nota {i + 1}:").grid(row=i+3, column=0, padx=5, pady=5, sticky="e")
            entrada = tb.Entry(frame, bootstyle="dark", width=5)
            entrada.grid(row=i+3, column=1, padx=5, pady=5, sticky="w")
            self.entradas.append(entrada)

        tb.Button(frame, text="Calcular", command=self.calcular, bootstyle=SUCCESS, width=15).grid(row=8, column=0, pady=10, sticky="ew")
        tb.Button(frame, text="Limpiar", command=self.limpiar_campos, bootstyle="secondary", width=15).grid(row=8, column=1, pady=30, sticky="ew")

        self.promedioLabel = tb.Label(frame, text="", bootstyle="success")
        self.promedioLabel.grid(row=9, column=0, columnspan=2)

        self.desviacionLabel = tb.Label(frame, text="", bootstyle="success")
        self.desviacionLabel.grid(row=10, column=0, columnspan=2)

        self.valor_mayorLabel = tb.Label(frame, text="", bootstyle="success")
        self.valor_mayorLabel.grid(row=11, column=0, columnspan=2)

        self.valor_menorLabel = tb.Label(frame, text="", bootstyle="success")
        self.valor_menorLabel.grid(row=12, column=0, columnspan=2)

        # Ajustar columnas
        for col in range(2):
            frame.grid_columnconfigure(col, weight=1)

    def calcular(self):
        self.promedioLabel.config(bootstyle="success")
        if not all(entrada.get() for entrada in self.entradas):
            self._mostrar_mensaje("⚠️ Por favor completa todos los campos.", error=True)
            return

        try:
            nums = [float(entrada.get()) for entrada in self.entradas]
            prom = Estadisticas.promedio(nums)
            desv = Estadisticas.desviacion_estandar(nums)
            mayor = Estadisticas.valor_mayor(nums)
            menor = Estadisticas.valor_menor(nums)

            self.promedioLabel.config(text=f"Promedio: {round(prom, 2)}")
            self.desviacionLabel.config(text=f"Desviación estándar: {round(desv, 2)}")
            self.valor_mayorLabel.config(text=f"Mayor nota: {mayor}")
            self.valor_menorLabel.config(text=f"Menor nota: {menor}")
        except ValueError:
            self._mostrar_mensaje("⚠️ Por favor ingresa solo números.", error=True)

    def limpiar_campos(self):
        for entrada in self.entradas:
            entrada.delete(0, tb.END)
        self._mostrar_mensaje("")
        self.promedioLabel.config(text="")
        self.desviacionLabel.config(text="")
        self.valor_mayorLabel.config(text="")
        self.valor_menorLabel.config(text="")


    def _mostrar_mensaje(self, texto, error=False):
        estilo = "warning" if error else "success"
        self.promedioLabel.config(text=texto, bootstyle=estilo)
        self.desviacionLabel.config(text="" if error else self.desviacionLabel.cget("text"))
        self.valor_mayorLabel.config(text="" if error else self.valor_mayorLabel.cget("text"))
        self.valor_menorLabel.config(text="" if error else self.valor_menorLabel.cget("text"))


if __name__ == "__main__":
    CalculadoraPromedioApp()
