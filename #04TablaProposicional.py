import tkinter as tk
from tkinter import messagebox, scrolledtext
import ttg

def crear_tabla():
    try:
        cantidad = int(entrada.get())
        if cantidad < 1:
            messagebox.showerror("Error", "Debes ingresar un número mayor que 0.")
            return
        if cantidad > 10:
            messagebox.showwarning(
                "Advertencia", 
                "No se permiten más de 10 proposiciones porque la tabla puede ser demasiado grande."
            )
            return
    except ValueError:
        messagebox.showerror("Error", "Ingresa un número entero válido.")
        return

    # Genera variables (P, Q, R, S...)
    variables = [chr(80 + i) for i in range(cantidad)]
    
    # Crea expresiones lógicas válidas para ttg
    expresion_conjunta = " and ".join(variables)
    expresion_disyunta = " or ".join(variables)
    expresion_negada = f"not {variables[0]}"
    
    operaciones = [
        expresion_conjunta, 
        expresion_disyunta, 
        expresion_negada
    ]
    
    # Genera la tabla de verdad
    tabla_verdad = ttg.Truths(variables, operaciones, ints=False)
    
    # Limpia el cuadro de texto e inserta el resultado formateado
    resultado.delete("1.0", tk.END)
    resultado.insert(tk.END, str(tabla_verdad))

# Configuración de la interfaz gráfica
ventana = tk.Tk()
ventana.title("Tabla de Verdad")
ventana.geometry("650x540")
ventana.minsize(500, 400)

encabezado = tk.Label(
    ventana, text="TABLA DE VERDAD", font=("Arial", 14, "bold")
)
encabezado.pack(pady=(15, 10))

contenedor = tk.Frame(ventana)
contenedor.pack(fill="x", padx=25)

tk.Label(
    contenedor, text="Número de proposiciones:", font=("Arial", 10)
).pack(anchor="w")

entrada = tk.Entry(contenedor, font=("Arial", 11))
entrada.pack(fill="x", pady=6)

boton = tk.Button(
    ventana, 
    text="Crear tabla", 
    command=crear_tabla, 
    font=("Arial", 10, "bold"), 
    bg="#315A7D", 
    fg="white", 
    padx=15, 
    pady=6
)
boton.pack(pady=12)

tk.Label(
    ventana, text="Resultado:", font=("Arial", 10, "bold")
).pack(pady=(3, 5))

resultado = scrolledtext.ScrolledText(
    ventana, wrap=tk.NONE, font=("Courier New", 10), height=20
)
resultado.pack(padx=20, pady=(0, 20), fill="both", expand=True)

ventana.mainloop()
