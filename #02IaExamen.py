import tkinter as tk
from tkinter import messagebox


def procesar_evaluacion():
    try:
        asistencia = float(campo_asistencia.get())
        promedio = float(campo_promedio.get())
        proyecto = campo_proyecto.get().strip().lower()
        permiso = campo_permiso.get().strip().lower()
        beca = campo_beca.get().strip().lower()

    except ValueError:
        messagebox.showerror(
            "Error de datos",
            "La asistencia y el promedio deben contener valores numéricos."
        )
        return

    # Proposiciones
    P = asistencia >= 80
    Q = promedio >= 8
    R = proyecto == "si"
    S = permiso == "si"
    B = beca == "si"

    # Mostrar valores de las proposiciones
    informacion = (
        f"P  Asistencia suficiente: {P}\n"
        f"Q  Promedio aprobatorio: {Q}\n"
        f"R  Proyecto entregado: {R}\n"
        f"S  Autorización especial: {S}\n"
        f"B  Cuenta con beca: {B}"
    )

    valores.config(text=informacion)

    # Operaciones de lógica proposicional
    negacion = not P
    conjuncion = P and Q
    disyuncion = Q or S
    condicional = (not P) or Q
    bicondicional = P == Q

    # Expresión principal
    expresion_final = P and Q and R

    operaciones = (
        f"¬P   Negación                 = {negacion}\n"
        f"P ∧ Q  Conjunción            = {conjuncion}\n"
        f"Q ∨ S  Disyunción             = {disyuncion}\n"
        f"P → Q  Condicional            = {condicional}\n"
        f"P ↔ Q  Bicondicional          = {bicondicional}\n"
        f"P ∧ Q ∧ R  Resultado lógico   = {expresion_final}"
    )

    resultado_logico.config(text=operaciones)

    # Resultado
    if expresion_final:
        resultado.config(
            text="AUTORIZADO PARA PRESENTAR EL EXAMEN",
            fg="#15803D"
        )
        descripcion.config(
            text="Las condiciones principales fueron cumplidas."
        )
    else:
        resultado.config(
            text="NO AUTORIZADO PARA PRESENTAR EL EXAMEN",
            fg="#B91C1C"
        )
        descripcion.config(
            text="No se cumplieron todas las condiciones requeridas."
        )


# ==============================
# VENTANA
# ==============================

ventana = tk.Tk()
ventana.title("Control de Autorización Académica")
ventana.geometry("520x700")
ventana.resizable(False, False)
ventana.configure(bg="#EEF2F7")


# ==============================
# ENCABEZADO
# ==============================

encabezado = tk.Frame(
    ventana,
    bg="#263B5A",
    height=90
)
encabezado.pack(fill="x")
encabezado.pack_propagate(False)

tk.Label(
    encabezado,
    text="CONTROL DE AUTORIZACIÓN",
    font=("Arial", 17, "bold"),
    bg="#263B5A",
    fg="white"
).pack(pady=(18, 3))

tk.Label(
    encabezado,
    text="Evaluación mediante lógica proposicional",
    font=("Arial", 9),
    bg="#263B5A",
    fg="#CBD5E1"
).pack()


# ==============================
# DATOS DEL ALUMNO
# ==============================

tk.Label(
    ventana,
    text="DATOS DEL ALUMNO",
    font=("Arial", 11, "bold"),
    bg="#EEF2F7",
    fg="#334155"
).pack(anchor="w", padx=30, pady=(18, 8))


formulario = tk.Frame(
    ventana,
    bg="white",
    padx=20,
    pady=15
)
formulario.pack(
    padx=30,
    fill="x"
)


def agregar_campo(texto):
    tk.Label(
        formulario,
        text=texto,
        font=("Arial", 9, "bold"),
        bg="white",
        fg="#475569"
    ).pack(anchor="w", pady=(2, 3))

    entrada = tk.Entry(
        formulario,
        font=("Arial", 10),
        relief="solid",
        bd=1
    )

    entrada.pack(
        fill="x",
        pady=(0, 8),
        ipady=3
    )

    return entrada


campo_asistencia = agregar_campo(
    "Asistencia (%)"
)

campo_promedio = agregar_campo(
    "Promedio"
)

campo_proyecto = agregar_campo(
    "Proyecto entregado (si/no)"
)

campo_permiso = agregar_campo(
    "Autorización especial (si/no)"
)

campo_beca = agregar_campo(
    "Cuenta con beca (si/no)"
)


# ==============================
# BOTÓN
# ==============================

tk.Button(
    ventana,
    text="PROCESAR EVALUACIÓN",
    font=("Arial", 10, "bold"),
    bg="#2563EB",
    fg="white",
    activebackground="#1D4ED8",
    activeforeground="white",
    relief="flat",
    padx=20,
    pady=8,
    command=procesar_evaluacion
).pack(pady=15)


# ==============================
# PROPOSICIONES
# ==============================

tk.Label(
    ventana,
    text="VALORES DE LAS PROPOSICIONES",
    font=("Arial", 10, "bold"),
    bg="#EEF2F7",
    fg="#334155"
).pack()


valores = tk.Label(
    ventana,
    text=(
        "P  Asistencia suficiente: --\n"
        "Q  Promedio aprobatorio: --\n"
        "R  Proyecto entregado: --\n"
        "S  Autorización especial: --\n"
        "B  Cuenta con beca: --"
    ),
    font=("Consolas", 9),
    justify="left",
    bg="white",
    fg="#475569",
    padx=20,
    pady=10
)
valores.pack(
    padx=30,
    fill="x",
    pady=(5, 10)
)


# ==============================
# OPERACIONES
# ==============================

tk.Label(
    ventana,
    text="OPERACIONES DE LÓGICA",
    font=("Arial", 10, "bold"),
    bg="#EEF2F7",
    fg="#334155"
).pack()


resultado_logico = tk.Label(
    ventana,
    text="Sin operaciones calculadas.",
    font=("Consolas", 9),
    justify="left",
    bg="white",
    fg="#475569",
    padx=20,
    pady=10
)
resultado_logico.pack(
    padx=30,
    fill="x",
    pady=(5, 10)
)


# ==============================
# RESULTADO
# ==============================

resultado = tk.Label(
    ventana,
    text="ESPERANDO EVALUACIÓN",
    font=("Arial", 11, "bold"),
    bg="#EEF2F7",
    fg="#64748B"
)
resultado.pack(pady=(2, 3))


descripcion = tk.Label(
    ventana,
    text="Ingresa los datos y procesa la evaluación.",
    font=("Arial", 9),
    bg="#EEF2F7",
    fg="#64748B"
)
descripcion.pack()


# Fórmula principal
tk.Label(
    ventana,
    text="Expresión principal:  P ∧ Q ∧ R",
    font=("Arial", 9, "italic"),
    bg="#EEF2F7",
    fg="#64748B"
).pack(side="bottom", pady=12)


ventana.mainloop()
