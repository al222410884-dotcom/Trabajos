import tkinter as tk
from tkinter import messagebox


def revisar_alumno():
    try:
        asistencia = float(campo_asistencia.get())
        promedio = float(campo_promedio.get())

        if asistencia < 0 or asistencia > 100:
            messagebox.showerror(
                "Valor incorrecto",
                "La asistencia debe estar entre 0 y 100."
            )
            return

        if promedio < 0 or promedio > 10:
            messagebox.showerror(
                "Valor incorrecto",
                "El promedio debe estar entre 0 y 10."
            )
            return

        proyecto = campo_proyecto.get().strip().lower() == "si"
        adeudos = campo_adeudos.get().strip().lower() == "si"
        autorizacion = campo_autorizacion.get().strip().lower() == "si"
        lista = campo_lista.get().strip().lower() == "si"

    except ValueError:
        messagebox.showerror(
            "Error",
            "Escribe números válidos en asistencia y promedio."
        )
        return

    # Proposiciones
    P = asistencia >= 80
    Q = promedio >= 8
    R = proyecto
    S = not adeudos
    T = autorizacion
    U = lista

    # Valores de las proposiciones
    datos = (
        f"P  Asistencia >= 80%       : {P}   ({asistencia}%)\n"
        f"Q  Promedio >= 8            : {Q}   ({promedio})\n"
        f"R  Proyecto entregado       : {R}\n"
        f"S  Sin adeudos              : {S}\n"
        f"T  Autorización especial    : {T}\n"
        f"U  Lista oficial             : {U}"
    )

    valores.config(text=datos)

    # Operaciones lógicas
    negacion = not P
    conjuncion = P and Q
    disyuncion = Q or T
    condicional = (not P) or Q
    bicondicional = P == Q

    # Expresión principal
    expresion = ((P and Q and R and S) or T) and U

    # Comprobación con la lista
    coincide = expresion == U

    operaciones = (
        f"¬P       = {negacion}\n"
        f"P ∧ Q    = {conjuncion}\n"
        f"Q ∨ T    = {disyuncion}\n"
        f"P → Q    = {condicional}\n"
        f"P ↔ Q    = {bicondicional}\n"
        f"((P ∧ Q ∧ R ∧ S) ∨ T) ∧ U = {expresion}"
    )

    calculos.config(text=operaciones)

    # Dictamen
    if expresion:
        dictamen.config(
            text="✓ ALUMNO AUTORIZADO",
            fg="#15803D"
        )
        detalle.config(
            text="El alumno cumple las condiciones para presentar."
        )
    else:
        dictamen.config(
            text="✕ ALUMNO NO AUTORIZADO",
            fg="#B91C1C"
        )
        detalle.config(
            text="El alumno no cumple todas las condiciones."
        )

    # Verificación
    if coincide:
        verificacion.config(
            text="La autorización coincide con la lista oficial.",
            fg="#2563EB"
        )
    else:
        verificacion.config(
            text="Advertencia: existe una diferencia con la lista oficial.",
            fg="#D97706"
        )


# ==========================================
# VENTANA PRINCIPAL
# ==========================================

ventana = tk.Tk()
ventana.title("Control de Examen")
ventana.geometry("540x760")
ventana.resizable(False, False)
ventana.configure(bg="#F1F5F9")


# ==========================================
# ENCABEZADO
# ==========================================

cabecera = tk.Frame(
    ventana,
    bg="#334155",
    height=95
)
cabecera.pack(fill="x")
cabecera.pack_propagate(False)

tk.Label(
    cabecera,
    text="CONTROL DE EXAMEN",
    font=("Arial", 18, "bold"),
    fg="white",
    bg="#334155"
).pack(pady=(18, 3))

tk.Label(
    cabecera,
    text="Evaluación mediante proposiciones lógicas",
    font=("Arial", 9),
    fg="#CBD5E1",
    bg="#334155"
).pack()


# ==========================================
# DATOS
# ==========================================

tk.Label(
    ventana,
    text="INFORMACIÓN DEL ALUMNO",
    font=("Arial", 11, "bold"),
    fg="#334155",
    bg="#F1F5F9"
).pack(anchor="w", padx=30, pady=(16, 7))


formulario = tk.Frame(
    ventana,
    bg="white",
    padx=20,
    pady=13
)
formulario.pack(
    padx=30,
    fill="x"
)


def crear_entrada(texto):
    tk.Label(
        formulario,
        text=texto,
        font=("Arial", 9, "bold"),
        fg="#475569",
        bg="white"
    ).pack(anchor="w")

    entrada = tk.Entry(
        formulario,
        font=("Arial", 10),
        relief="solid",
        bd=1
    )

    entrada.pack(
        fill="x",
        pady=(3, 7),
        ipady=2
    )

    return entrada


campo_asistencia = crear_entrada(
    "Asistencia (0 - 100)"
)

campo_promedio = crear_entrada(
    "Promedio (0 - 10)"
)

campo_proyecto = crear_entrada(
    "Proyecto entregado (si/no)"
)

campo_adeudos = crear_entrada(
    "¿Tiene adeudos? (si/no)"
)

campo_autorizacion = crear_entrada(
    "Autorización especial (si/no)"
)

campo_lista = crear_entrada(
    "¿Está en la lista oficial? (si/no)"
)


# ==========================================
# BOTÓN
# ==========================================

tk.Button(
    ventana,
    text="REALIZAR EVALUACIÓN",
    font=("Arial", 10, "bold"),
    bg="#0F766E",
    fg="white",
    activebackground="#115E59",
    activeforeground="white",
    relief="flat",
    padx=20,
    pady=8,
    command=revisar_alumno
).pack(pady=14)


# ==========================================
# PROPOSICIONES
# ==========================================

tk.Label(
    ventana,
    text="ESTADO DE LAS PROPOSICIONES",
    font=("Arial", 10, "bold"),
    fg="#334155",
    bg="#F1F5F9"
).pack()


valores = tk.Label(
    ventana,
    text=(
        "P  Asistencia >= 80%       : --\n"
        "Q  Promedio >= 8            : --\n"
        "R  Proyecto entregado       : --\n"
        "S  Sin adeudos               : --\n"
        "T  Autorización especial     : --\n"
        "U  Lista oficial              : --"
    ),
    font=("Consolas", 8),
    justify="left",
    bg="white",
    fg="#475569",
    padx=18,
    pady=9
)
valores.pack(
    padx=30,
    fill="x",
    pady=(4, 9)
)


# ==========================================
# OPERACIONES
# ==========================================

tk.Label(
    ventana,
    text="CÁLCULOS LÓGICOS",
    font=("Arial", 10, "bold"),
    fg="#334155",
    bg="#F1F5F9"
).pack()


calculos = tk.Label(
    ventana,
    text="Sin datos para calcular.",
    font=("Consolas", 8),
    justify="left",
    bg="white",
    fg="#475569",
    padx=18,
    pady=9
)
calculos.pack(
    padx=30,
    fill="x",
    pady=(4, 10)
)


# ==========================================
# RESULTADO
# ==========================================

dictamen = tk.Label(
    ventana,
    text="ESPERANDO EVALUACIÓN",
    font=("Arial", 12, "bold"),
    fg="#64748B",
    bg="#F1F5F9"
)
dictamen.pack(pady=(2, 3))


detalle = tk.Label(
    ventana,
    text="Ingresa la información para obtener el dictamen.",
    font=("Arial", 9),
    fg="#64748B",
    bg="#F1F5F9"
)
detalle.pack()


verificacion = tk.Label(
    ventana,
    text="",
    font=("Arial", 9, "italic"),
    bg="#F1F5F9"
)
verificacion.pack(pady=(5, 0))


# Fórmula principal
tk.Label(
    ventana,
    text="Expresión: ((P ∧ Q ∧ R ∧ S) ∨ T) ∧ U",
    font=("Arial", 9, "italic"),
    fg="#64748B",
    bg="#F1F5F9"
).pack(side="bottom", pady=12)


ventana.mainloop()