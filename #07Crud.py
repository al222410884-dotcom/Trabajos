import os
import random
import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from pathlib import Path
from urllib.parse import quote_plus
from pymongo import MongoClient
from dotenv import load_dotenv

# ==========================================
# CONFIGURACIÓN DE BASE DE DATOS (MANTENIDA)
# ==========================================
# env_path = Path(__file__).resolve().parent / ".env"
# load_dotenv(dotenv_path=env_path)
# usuario_bd = os.getenv("MONGO_USER")
# contrasena_bd = quote_plus(os.getenv("MONGO_PASSWORD") or "")
# servidor_bd = os.getenv("MONGO_DB")
# nombre_bd = os.getenv("MONGO_DB_NAME")
# nombre_coleccion = os.getenv("MONGO_COLLECTION")

# if not all([usuario_bd, contrasena_bd, servidor_bd, nombre_bd, nombre_coleccion]):
#     raise ValueError("Faltan variables en el archivo .env")

# uri_mongo = f"mongodb+srv://{usuario_bd}:{contrasena_bd}@{servidor_bd}/"

# try:
#     cliente = MongoClient(uri_mongo, serverSelectionTimeoutMS=5000)
#     cliente.admin.command('ping')
#     base_datos = cliente[nombre_bd]
#     coleccion = base_datos[nombre_coleccion]
#     print(f"Conexión exitosa a la base de datos '{nombre_bd}', colección '{nombre_coleccion}'.")
# except Exception as error:
#     print(f"Error al conectar con MongoDB: {error}")
#     raise SystemExit(error)

class MockColeccion:
    def insert_one(self, doc): print("Simulado en Mongo: Insertado", doc)
    def update_one(self, filtro, cambio): print("Simulado en Mongo: Actualizado", cambio)
    def delete_one(self, filtro): print("Simulado en Mongo: Eliminado", filtro)
    def find(self): return []
coleccion = MockColeccion()


def calcular_diagnostico(oxigenacion, fc, pa):
    diagnosticos = []
    if oxigenacion <= 90 and fc >= 120:
        diagnosticos.append("Urgencia Respiratoria")
    elif oxigenacion <= 90:
        diagnosticos.append("Hipoxia Crítica")

    if pa >= 180 or pa < 90:
        diagnosticos.append("Crisis Presión")
    elif pa >= 140:
        diagnosticos.append("Hipertensión")

    if (fc >= 120 or fc < 60) and oxigenacion > 90:
        diagnosticos.append("Ritmo Irregular")

    if not diagnosticos:
        diagnosticos.append("Signos Estables")

    return " | ".join(diagnosticos[:2])


class ClinicaDataCenter:
    def __init__(self, ventana):
        self.root = ventana
        self.root.title("DataCenter Clínico - Gestión Hospitalaria")
        self.root.geometry("720x780")
        self.root.configure(bg="#F8FAFC")
        
        self.estilos = ttk.Style()
        self.estilos.theme_use("clam")
        self.estilos.configure("TLabelframe", background="#F8FAFC")
        self.estilos.configure("TLabelframe.Label", background="#F8FAFC", font=("Segoe UI", 9, "bold"), foreground="#0F172A")
        
        self.lista_documentos = []
        self.inicializar_interfaz()

    def inicializar_interfaz(self):
        banner = tk.Frame(self.root, bg="#0D9488", height=60)
        banner.pack(fill="x", side="top")
        banner.pack_propagate(False)
        
        lbl_titulo = tk.Label(
            banner, text="DATACENTER CLÍNICO - GESTIÓN MÉDICA", 
            font=("Segoe UI", 12, "bold"), bg="#0D9488", fg="white"
        )
        lbl_titulo.pack(pady=18, padx=25, anchor="w")

        cuerpo = tk.Frame(self.root, bg="#F8FAFC")
        cuerpo.pack(fill="both", expand=True, padx=25, pady=15)

        m_datos = ttk.LabelFrame(cuerpo, text=" Ficha de Identificación ")
        m_datos.pack(fill="x", pady=5)
        
        tk.Label(m_datos, text="ID / Folio:", bg="#F8FAFC", font=("Segoe UI", 9)).grid(row=0, column=0, sticky="w", padx=10, pady=6)
        self.txt_folio = tk.Entry(m_datos, font=("Segoe UI", 10), state="readonly", readonlybackground="#E2E8F0", bd=1, relief="solid")
        self.txt_folio.grid(row=0, column=1, sticky="w", padx=5)

        tk.Label(m_datos, text="Nombre Completo:", bg="#F8FAFC", font=("Segoe UI", 9)).grid(row=0, column=2, sticky="w", padx=15)
        self.txt_nombre = tk.Entry(m_datos, font=("Segoe UI", 10), bd=1, relief="solid", width=32)
        self.txt_nombre.grid(row=0, column=3, sticky="ew", padx=5)
        m_datos.columnconfigure(3, weight=1)

        tk.Label(m_datos, text="Edad (años):", bg="#F8FAFC").grid(row=1, column=0, sticky="w", padx=10, pady=8)
        self.txt_edad = tk.Entry(m_datos, font=("Segoe UI", 10), bd=1, relief="solid", width=10)
        self.txt_edad.grid(row=1, column=1, sticky="w", padx=5)

        tk.Label(m_datos, text="Peso (kg):", bg="#F8FAFC").grid(row=1, column=2, sticky="w", padx=15)
        self.txt_peso = tk.Entry(m_datos, font=("Segoe UI", 10), bd=1, relief="solid", width=10)
        self.txt_peso.grid(row=1, column=3, sticky="w", padx=5)

        tk.Label(m_datos, text="Talla (m):", bg="#F8FAFC").grid(row=1, column=2, sticky="w", padx=(180, 0))
        self.txt_talla = tk.Entry(m_datos, font=("Segoe UI", 10), bd=1, relief="solid", width=10)
        self.txt_talla.grid(row=1, column=3, sticky="w", padx=(240, 0))
        # --- CONTENEDOR 2: PARÁMETROS BIOMÉTRICOS ---
        m_vitales = ttk.LabelFrame(cuerpo, text=" Constantes Vitales ")
        m_vitales.pack(fill="x", pady=8)

        tk.Label(m_vitales, text="SpO2 (%):", bg="#F8FAFC").grid(row=0, column=0, sticky="w", padx=10, pady=8)
        self.txt_oxigenacion = tk.Entry(m_vitales, font=("Segoe UI", 10), bd=1, relief="solid", width=12)
        self.txt_oxigenacion.grid(row=0, column=1, padx=5)

        tk.Label(m_vitales, text="Frecuencia (lpm):", bg="#F8FAFC").grid(row=0, column=2, sticky="w", padx=20)
        self.txt_fc = tk.Entry(m_vitales, font=("Segoe UI", 10), bd=1, relief="solid", width=12)
        self.txt_fc.grid(row=0, column=3, padx=5)

        tk.Label(m_vitales, text="Presión (mmHg):", bg="#F8FAFC").grid(row=0, column=4, sticky="w", padx=20)
        self.txt_pa = tk.Entry(m_vitales, font=("Segoe UI", 10), bd=1, relief="solid", width=12)
        self.txt_pa.grid(row=0, column=5, padx=5)

        # --- BOTONERA FLOTANTE ---
        barra_herramientas = tk.Frame(cuerpo, bg="#F8FAFC")
        barra_herramientas.pack(fill="x", pady=10)

        btn_props = {"font": ("Segoe UI", 9, "bold"), "fg": "white", "relief": "flat", "cursor": "hand2", "bd": 0, "pady": 6, "padx": 12}
        
        btn_guardar = tk.Button(barra_herramientas, text="✚ Guardar Paciente", bg="#0D9488", activebackground="#0F766E", command=self.crear_registro, **btn_props)
        btn_guardar.pack(side="left", padx=3)
        
        btn_actualizar = tk.Button(barra_herramientas, text="📝 Actualizar", bg="#475569", activebackground="#334155", command=self.actualizar_registro, **btn_props)
        btn_actualizar.pack(side="left", padx=3)
        
        btn_eliminar = tk.Button(barra_herramientas, text="❌ Eliminar Registro", bg="#E11D48", activebackground="#BE123C", command=self.eliminar_registro, **btn_props)
        btn_eliminar.pack(side="left", padx=3)
        
        btn_limpiar = tk.Button(barra_herramientas, text="🧹 Limpiar", bg="#94A3B8", activebackground="#64748B", fg="#0F172A", font=("Segoe UI", 9, "bold"), relief="flat", cursor="hand2", pady=6, padx=12)
        btn_limpiar.pack(side="right", padx=3)

        # --- TABLA (TREEVIEW) ---
        lbl_seccion_tabla = tk.Label(cuerpo, text="HISTORIAL CLÍNICO EN TIEMPO REAL", font=("Segoe UI", 9, "bold"), bg="#F8FAFC", fg="#475569")
        lbl_seccion_tabla.pack(anchor="w", pady=(10, 4))

        tabla_contenedor = tk.Frame(cuerpo, bd=1, relief="solid")
        tabla_contenedor.pack(fill="both", expand=True)

        scroll_y = ttk.Scrollbar(tabla_contenedor, orient="vertical")
        
        self.tabla = ttk.Treeview(
            tabla_contenedor, 
            columns=("folio", "paciente", "diagnostico", "cita"), 
            show="headings", 
            yscrollcommand=scroll_y.set,
            height=8
        )
        scroll_y.config(command=self.tabla.yview)
        
        self.tabla.heading("folio", text="Folio")
        self.tabla.heading("paciente", text="Paciente")
        self.tabla.heading("diagnostico", text="Diagnóstico Clínico")
        self.tabla.heading("cita", text="Fecha de Cita")
        
        self.tabla.column("folio", width=70, anchor="center")
        self.tabla.column("paciente", width=180, anchor="w")
        self.tabla.column("diagnostico", width=220, anchor="w")
        self.tabla.column("cita", width=130, anchor="center")
        
        self.tabla.pack(side="left", fill="both", expand=True)
        scroll_y.pack(side="right", fill="y")
        
        self.tabla.bind("<<TreeviewSelect>>", self.cargar_datos_seleccion)

        # --- BARRA DE ESTADO INFERIOR ---
        self.lbl_estado = tk.Label(
            self.root, 
            text="● Sistema inicializado. Listo para consultas.", 
            font=("Segoe UI", 9), 
            bg="#EEF2F6", fg="#059669", 
            anchor="w", padx=20, pady=6
        )
        self.lbl_estado.pack(fill="x", side="bottom")

        self.leer_registros()

    def leer_registros(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        
        for doc in self.lista_documentos:
            self.tabla.insert("", "end", values=(doc.get("folio"), doc.get("nombre"), doc.get("diagnostico"), doc.get("cita")))

    def cargar_datos_seleccion(self, event):
        seleccion = self.tabla.selection()
        if not seleccion:
            return
        
        valores = self.tabla.item(seleccion, "values")
        folio_sel = int(valores[0])
        
        doc = next((d for d in self.lista_documentos if d.get("folio") == folio_sel), None)
        if doc:
            self.txt_folio.config(state="normal")
            self.txt_folio.delete(0, tk.END)
            self.txt_folio.insert(0, str(doc["folio"]))
            self.txt_folio.config(state="readonly")
            
            self.txt_nombre.delete(0, tk.END)
            self.txt_nombre.insert(0, doc["nombre"])
            
            self.txt_edad.delete(0, tk.END)
            self.txt_edad.insert(0, str(doc["edad"]))
            
            self.txt_peso.delete(0, tk.END)
            self.txt_peso.insert(0, str(doc["peso"]))
            
            self.txt_talla.delete(0, tk.END)
            self.txt_talla.insert(0, str(doc["talla"]))
            
            self.txt_oxigenacion.delete(0, tk.END)
            self.txt_oxigenacion.insert(0, str(doc["oxigenacion"]))
            
            self.txt_fc.delete(0, tk.END)
            self.txt_fc.insert(0, str(doc["fc"]))
            
            self.txt_pa.delete(0, tk.END)
            self.txt_pa.insert(0, str(doc["pa"]))

    def crear_registro(self):
        try:
            nombre = self.txt_nombre.get().strip() or "Paciente Anónimo"
            edad = int(self.txt_edad.get())
            peso = float(self.txt_peso.get())
            talla = float(self.txt_talla.get())
            oxigenacion = float(self.txt_oxigenacion.get())
            fc = int(self.txt_fc.get())
            pa = int(self.txt_pa.get())
        except ValueError:
            messagebox.showerror("Error de Validación", "Por favor introduce formatos numéricos correctos.")
            return

        diagnostico = calcular_diagnostico(oxigenacion, fc, pa)
        folio = random.randint(1000, 9999)

        cita_info = "Sin cita"
        if messagebox.askyesno("Evaluación", f"Diagnóstico: {diagnostico}\n\n¿Desea asignar una cita?"):
            fecha = simpledialog.askstring("Agenda", "Fecha (DD/MM/AAAA):")
            hora = simpledialog.askstring("Agenda", "Hora (HH:MM AM/PM):")
            if fecha and hora:
                cita_info = f"{fecha} - {hora}"

        documento = {
            "folio": folio, "nombre": nombre, "edad": edad, "peso": peso, "talla": talla,
            "oxigenacion": oxigenacion, "fc": fc, "pa": pa, "diagnostico": diagnostico, "cita": cita_info
        }

        try:
            coleccion.insert_one(documento)
            self.lista_documentos.append(documento)
            self.lbl_estado.config(text=f"● Paciente registrado con Folio: #{folio}", fg="#059669")
            self.limpiar_campos()
            self.leer_registros()
        except Exception as e:
            messagebox.showerror("Error BD", f"No se pudo guardar: {e}")

    def actualizar_registro(self):
        seleccion = self.tabla.selection()
        if not seleccion:
            messagebox.showwarning("Atención", "Por favor, selecciona un paciente de la lista para actualizar.")
            return

        try:
            folio_actual = int(self.txt_folio.get())
            nombre = self.txt_nombre.get().strip() or "Paciente Anónimo"
            edad = int(self.txt_edad.get())
            peso = float(self.txt_peso.get())
            talla = float(self.txt_talla.get())
            oxigenacion = float(self.txt_oxigenacion.get())
            fc = int(self.txt_fc.get())
            pa = int(self.txt_pa.get())
        except ValueError:
            messagebox.showerror("Error", "Verifica que los datos ingresados sean válidos.")
            return

        diagnostico = calcular_diagnostico(oxigenacion, fc, pa)

        try:
            coleccion.update_one({"folio": folio_actual}, {"$set": {
                "nombre": nombre, "edad": edad, "peso": peso, "talla": talla,
                "oxigenacion": oxigenacion, "fc": fc, "pa": pa, "diagnostico": diagnostico
            }})
            
            for doc in self.lista_documentos:
                if doc["folio"] == folio_actual:
                    doc["nombre"] = nombre
                    doc["edad"] = edad
                    doc["peso"] = peso
                    doc["talla"] = talla
                    doc["oxigenacion"] = oxigenacion
                    doc["fc"] = fc
                    doc["pa"] = pa
                    doc["diagnostico"] = diagnostico
                    break
            
            self.lbl_estado.config(text=f"● Registro #{folio_actual} actualizado correctamente.", fg="#0284C7")
            self.limpiar_campos()
            self.leer_registros()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo actualizar: {e}")

    def eliminar_registro(self):
        seleccion = self.tabla.selection()
        if not seleccion:
            messagebox.showwarning("Atención", "Selecciona el registro que deseas eliminar.")
            return

        valores = self.tabla.item(seleccion, "values")
        folio_eliminar = int(valores[0])

        if messagebox.askyesno("Confirmar", f"¿Estás seguro de que deseas eliminar permanentemente el folio #{folio_eliminar}?"):
            try:
                coleccion.delete_one({"folio": folio_eliminar})
                self.lista_documentos = [d for d in self.lista_documentos if d["folio"] != folio_eliminar]
                
                self.lbl_estado.config(text=f"● Registro #{folio_eliminar} borrado del sistema.", fg="#E11D48")
                self.limpiar_campos()
                self.leer_registros()
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo eliminar: {e}")

    def limpiar_campos(self):
        self.txt_folio.config(state="normal")
        self.txt_folio.delete(0, tk.END)
        self.txt_folio.config(state="readonly")
        for campo in (self.txt_nombre, self.txt_edad, self.txt_peso, self.txt_talla, self.txt_oxigenacion, self.txt_fc, self.txt_pa):
            campo.delete(0, tk.END)


if __name__ == "__main__":
    ventana_principal = tk.Tk()
    app = ClinicaDataCenter(ventana_principal)
    ventana_principal.mainloop()