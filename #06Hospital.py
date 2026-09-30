import tkinter as tk
from tkinter import messagebox
import random

class AppValoracion:
    def __init__(self, ventana):
        self.root = ventana
        self.root.title("MedicalCheck - Sistema de Diagnóstico")
        self.root.geometry("540x720")
        self.root.configure(bg="#1E293B")  # Fondo azul oscuro moderno
        
        self.inicializar_interfaz()

    def inicializar_interfaz(self):
        # Título Principal Estilizado
        lbl_titulo = tk.Label(
            self.root, text="VALORACIÓN CLÍNICA", 
            font=("Segoe UI", 16, "bold"), bg="#1E293B", fg="#F8FAFC"
        )
        lbl_titulo.pack(pady=(20, 5))
        
        lbl_sub = tk.Label(
            self.root, text="Panel de captura de constantes vitales", 
            font=("Segoe UI", 9, "italic"), bg="#1E293B", fg="#94A3B8"
        )
        lbl_sub.pack(pady=(0, 15))

        # Contenedor Principal (Formulario)
        self.panel = tk.Frame(self.root, bg="#1E293B")
        self.panel.pack(fill="x", padx=30)

        # --- SECCIÓN 1: IDENTIFICACIÓN ---
        marco_id = tk.LabelFrame(self.panel, text=" Identificación del Paciente ", bg="#1E293B", fg="#38BDF8", font=("Segoe UI", 9, "bold"), padx=15, pady=10)
        marco_id.pack(fill="x", pady=5)

        tk.Label(marco_id, text="Nombre Completo:", bg="#1E293B", fg="#E2E8F0").grid(row=0, column=0, sticky="w", pady=2)
        self.txt_nombre = tk.Entry(marco_id, font=("Segoe UI", 10), bg="#334155", fg="white", insertbackground="white", bd=1, relief="flat")
        self.txt_nombre.grid(row=0, column=1, columnspan=5, sticky="ew", padx=(10, 0))
        marco_id.columnconfigure(1, weight=1)

        tk.Label(marco_id, text="Edad (años):", bg="#1E293B", fg="#E2E8F0").grid(row=1, column=0, sticky="w", pady=8)
        self.txt_edad = tk.Entry(marco_id, width=6, font=("Segoe UI", 10), bg="#334155", fg="white", bd=0)
        self.txt_edad.grid(row=1, column=1, sticky="w", padx=(10, 0))

        tk.Label(marco_id, text="Peso (kg):", bg="#1E293B", fg="#E2E8F0").grid(row=1, column=2, sticky="w", padx=(15, 0))
        self.txt_peso = tk.Entry(marco_id, width=6, font=("Segoe UI", 10), bg="#334155", fg="white", bd=0)
        self.txt_peso.grid(row=1, column=3, sticky="w", padx=(5, 0))

        tk.Label(marco_id, text="Estatura (m):", bg="#1E293B", fg="#E2E8F0").grid(row=1, column=4, sticky="w", padx=(15, 0))
        self.txt_estatura = tk.Entry(marco_id, width=6, font=("Segoe UI", 10), bg="#334155", fg="white", bd=0)
        self.txt_estatura.grid(row=1, column=5, sticky="w", padx=(5, 0))

        # --- SECCIÓN 2: CONSTANTES VITALES ---
        marco_vitales = tk.LabelFrame(self.panel, text=" Parámetros Biométricos ", bg="#1E293B", fg="#38BDF8", font=("Segoe UI", 9, "bold"), padx=15, pady=10)
        marco_vitales.pack(fill="x", pady=5)

        tk.Label(marco_vitales, text="SpO2 (%):", bg="#1E293B", fg="#E2E8F0").grid(row=0, column=0, sticky="w", pady=5)
        self.txt_oxigeno = tk.Entry(marco_vitales, width=6, font=("Segoe UI", 10), bg="#334155", fg="white", bd=0)
        self.txt_oxigeno.grid(row=0, column=1, sticky="w", padx=(10, 0))

        tk.Label(marco_vitales, text="Frecuencia (lpm):", bg="#1E293B", fg="#E2E8F0").grid(row=0, column=2, sticky="w", padx=(15, 0))
        self.txt_frecuencia = tk.Entry(marco_vitales, width=6, font=("Segoe UI", 10), bg="#334155", fg="white", bd=0)
        self.txt_frecuencia.grid(row=0, column=3, sticky="w", padx=(5, 0))

        tk.Label(marco_vitales, text="Presión (mmHg):", bg="#1E293B", fg="#E2E8F0").grid(row=0, column=4, sticky="w", padx=(15, 0))
        self.txt_presion = tk.Entry(marco_vitales, width=6, font=("Segoe UI", 10), bg="#334155", fg="white", bd=0)
        self.txt_presion.grid(row=0, column=5, sticky="w", padx=(5, 0))

        # --- SECCIÓN 3: AGENDA ---
        marco_agenda = tk.LabelFrame(self.panel, text=" Planificación de Consulta ", bg="#1E293B", fg="#38BDF8", font=("Segoe UI", 9, "bold"), padx=15, pady=10)
        marco_agenda.pack(fill="x", pady=5)

        tk.Label(marco_agenda, text="Agendar Cita? (s/n):", bg="#1E293B", fg="#E2E8F0").grid(row=0, column=0, sticky="w")
        self.txt_cita = tk.Entry(marco_agenda, width=5, font=("Segoe UI", 10), bg="#334155", fg="white", bd=0)
        self.txt_cita.grid(row=0, column=1, sticky="w", padx=(10, 0))

        tk.Label(marco_agenda, text="Fecha (dd/mm):", bg="#1E293B", fg="#E2E8F0").grid(row=0, column=2, sticky="w", padx=(20, 0))
        self.txt_fecha = tk.Entry(marco_agenda, width=10, font=("Segoe UI", 10), bg="#334155", fg="white", bd=0)
        self.txt_fecha.grid(row=0, column=3, sticky="w", padx=(5, 0))

        tk.Label(marco_agenda, text="Hora (hh:mm):", bg="#1E293B", fg="#E2E8F0").grid(row=0, column=4, sticky="w", padx=(20, 0))
        self.txt_hora = tk.Entry(marco_agenda, width=8, font=("Segoe UI", 10), bg="#334155", fg="white", bd=0)
        self.txt_hora.grid(row=0, column=5, sticky="w", padx=(5, 0))

        # Botón de Procesamiento
        btn_evaluar = tk.Button(
            self.root, text="PROCESAR VALORACIÓN", command=self.ejecutar_diagnostico,
            font=("Segoe UI", 10, "bold"), bg="#0284C7", fg="white",
            activebackground="#0369A1", activeforeground="white", relief="flat", cursor="hand2", padx=25, pady=8
        )
        btn_evaluar.pack(pady=15)

        # --- SECCIÓN DE REPORTES DE SALIDA ---
        self.lbl_info_paciente = tk.Label(self.root, text="", font=("Segoe UI", 10, "bold"), bg="#1E293B", fg="#F1F5F9")
        self.lbl_info_paciente.pack(pady=2)

        # Corregido: Se cambiaron los tamaños de fuente de 9.5 a enteros (9 y 10)
        self.lbl_diagnostico = tk.Label(self.root, text="Esperando datos...", font=("Segoe UI", 10), bg="#1E293B", fg="#FDA4AF", justify="center", wraplength=450)
        self.lbl_diagnostico.pack(pady=8)

        self.lbl_agenda_resumen = tk.Label(self.root, text="", font=("Segoe UI", 10), bg="#1E293B", fg="#94A3B8", justify="center", wraplength=450)
        self.lbl_agenda_resumen.pack(pady=5)

    def ejecutar_diagnostico(self):
        paciente_nom = self.txt_nombre.get().strip()

        if not paciente_nom:
            messagebox.showwarning("Campo Vacío", "Por favor ingrese el nombre del paciente.")
            return

        try:
            val_edad = int(self.txt_edad.get())
            val_peso = float(self.txt_peso.get())
            val_estat = float(self.txt_estatura.get())
            val_oxig = float(self.txt_oxigeno.get())
            val_frec = int(self.txt_frecuencia.get())
            val_pres = int(self.txt_presion.get())
        except ValueError:
            messagebox.showerror("Error de Formato", "Asegúrese de ingresar solo números válidos en los campos biométricos.")
            return

        alertas = []

        # Evaluación Sintomática
        if val_oxig <= 90:
            if val_frec >= 120:
                alertas.append("Oxigenación baja acompañada de frecuencia cardíaca elevada")
            else:
                alertas.append("Nivel de oxigenación por debajo del límite óptimo")
        elif val_frec >= 120 or val_frec < 60:
            alertas.append("Ritmo cardíaco fuera de los parámetros clínicos esperados")

        if val_pres >= 180:
            alertas.append("Presión arterial en rangos críticamente elevados")
        elif val_pres < 90:
            alertas.append("Presión arterial en niveles bajos")
        elif val_pres >= 140:
            alertas.append("Presión arterial moderadamente por encima del rango recomendado")

        if not alertas:
            alertas.append("Todas las constantes vitales se encuentran estables.")

        alertas = alertas[:2]

        # Actualizar Panel de Salida 1
        resumen_personal = f"FICHA: {paciente_nom.upper()} | {val_edad} Años | {val_peso} kg | {val_estat} m"
        self.lbl_info_paciente.config(text=resumen_personal)

        # Actualizar Panel de Salida 2
        diagnostico_texto = "SÍNTOMAS DETECTADOS:\n" + "\n".join(f"• {item}" for item in alertas)
        self.lbl_diagnostico.config(text=diagnostico_texto)

        # Gestión Automática de Citas
        opcion_cita = self.txt_cita.get().strip().lower()

        if opcion_cita == "s":
            val_fecha = self.txt_fecha.get().strip()
            val_hora = self.txt_hora.get().strip()

            if not val_fecha or not val_hora:
                self.lbl_agenda_resumen.config(text="⚠️ Error: Proporcione fecha y hora de la cita.", fg="#F59E0B")
                return

            lista_medicos = ["Dra. Elena Ramos", "Dr. Carlos Vaca", "Dra. Sofía Mendoza", "Dr. Mateo Silva"]
            # Corregido: Se asignaron las salas válidas en la lista
            lista_consultorios = [101, 102, 201, 305]

            medico_asignado = random.choice(lista_medicos)
            sala_asignada = random.choice(lista_consultorios)
            num_ticket = random.randint(1000, 9999)

            ticket_info = (
                f"=== COMPROBANTE DE CITA ===\n"
                f"Ticket: #{num_ticket}  |  Consultorio: {sala_asignada}\n"
                f"Asignado a: {medico_asignado}\n"
                f"Programación: {val_fecha} a las {val_hora} hs"
            )
            self.lbl_agenda_resumen.config(text=ticket_info, fg="#10B981")
        else:
            self.lbl_agenda_resumen.config(text="No se solicitó programación de citas médicas.", fg="#64748B")

if __name__ == "__main__":
    ventana_principal = tk.Tk()
    app = AppValoracion(ventana_principal)
    ventana_principal.mainloop()
