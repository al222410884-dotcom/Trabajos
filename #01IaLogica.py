import tkinter as tk
from tkinter import messagebox


def comprobar_requisitos():
    try:
        porcentaje = float(caja_asistencia.get())
        calificacion = float(caja_promedio.get())
        entrega = caja_proyecto.get().strip().lower()

    except ValueError:
        messagebox.showerror(
            "Dato inválido",
            "Ingresa números válidos en asistencia y promedio."
        )
        return

    # Condiciones lógicas
    asistencia_ok = porcentaje >= 80
    promedio_ok = calificacion >= 8
    proyecto_ok = entrega == "si"

    resultado = asistencia_ok and promedio_ok and proyecto_ok

    # Mostrar condiciones
    estado_condiciones.config(
        text=
        f"Asistencia >= 80: {'Sí' if asistencia_ok else 'No'}\n"
        f"Promedio >= 8: {'Sí' if promedio_ok else 'No'}\n"
        f"Proyecto entregado: {'Sí' if proyecto_ok else 'No'}"
    )

    # Resultado
    if resultado:
        resultado_final.config(
            text="✓  REQUISITOS CUMPLIDOS",
            fg="#15803D"
        )
        detalle.config(
            text="El alumno puede presentar el examen final."
        )
    else:
        resultado_final.config(
            text="✕  REQUISITOS INCOMPLETOS",
            fg="#B91C1C"
        )
        detalle.config(
            text="El alumno no puede presentar el examen final."
        )


# Ventana principal
app = tk.Tk()
app.title("Evaluación Académica")
app.geometry("450x500")
app.resizable(False, False)
app.configure(bg="#E8EEF5")


# Encabezado
tk.Label(
    app,
    text="EVALUACIÓN ACADÉMICA",
    font=("Verdana", 16, "bold"),
    bg="#1E3A5F",
    fg="white",
    pady=15
).pack(fill="x")


tk.Label(
    app,
    text="Verificación de requisitos para examen final",
    font=("Arial", 9),
    bg="#E8EEF5",
    fg="#475569"
).pack(pady=(15, 8))


# Marco de información
marco = tk.Frame(
    app,
    bg="white",
    padx=20,
    pady=15
)
marco.pack(padx=30, fill="x")


# Asistencia
tk.Label(
    marco,
    text="Porcentaje de asistencia",
    font=("Arial", 10, "bold"),
    bg="white",
    fg="#334155"
).pack(anchor="w")

caja_asistencia = tk.Entry(
    marco,
    font=("Arial", 11)
)
caja_asistencia.pack(
    fill="x",
    pady=(5, 12)
)


# Promedio
tk.Label(
    marco,
    text="Promedio obtenido",
    font=("Arial", 10, "bold"),
    bg="white",
    fg="#334155"
).pack(anchor="w")

caja_promedio = tk.Entry(
    marco,
    font=("Arial", 11)
)
caja_promedio.pack(
    fill="x",
    pady=(5, 12)
)


# Proyecto
tk.Label(
    marco,
    text="Proyecto entregado (si/no)",
    font=("Arial", 10, "bold"),
    bg="white",
    fg="#334155"
).pack(anchor="w")

caja_proyecto = tk.Entry(
    marco,
    font=("Arial", 11)
)
caja_proyecto.pack(
    fill="x",
    pady=(5, 5)
)


# Botón
tk.Button(
    app,
    text="COMPROBAR REQUISITOS",
    command=comprobar_requisitos,
    font=("Arial", 10, "bold"),
    bg="#2563EB",
    fg="white",
    activebackground="#1D4ED8",
    activeforeground="white",
    relief="flat",
    padx=15,
    pady=8
).pack(pady=18)


# Sección de condiciones
tk.Label(
    app,
    text="CONDICIONES LÓGICAS",
    font=("Arial", 10, "bold"),
    bg="#E8EEF5",
    fg="#334155"
).pack()


estado_condiciones = tk.Label(
    app,
    text=(
        "Asistencia >= 80: --\n"
        "Promedio >= 8: --\n"
        "Proyecto entregado: --"
    ),
    font=("Arial", 10),
    justify="left",
    bg="white",
    fg="#475569",
    padx=20,
    pady=10
)
estado_condiciones.pack(pady=8)


# Resultado
resultado_final = tk.Label(
    app,
    text="ESPERANDO RESULTADO",
    font=("Arial", 12, "bold"),
    bg="#E8EEF5",
    fg="#64748B"
)
resultado_final.pack(pady=(8, 3))


detalle = tk.Label(
    app,
    text="Ingresa los datos y presiona el botón.",
    font=("Arial", 9),
    bg="#E8EEF5",
    fg="#64748B"
)
detalle.pack()


# Fórmula
tk.Label(
    app,
    text="P ∧ Q ∧ R",
    font=("Arial", 10, "italic"),
    bg="#E8EEF5",
    fg="#64748B"
).pack(side="bottom", pady=12)


app.mainloop()