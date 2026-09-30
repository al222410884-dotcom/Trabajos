import tkinter as tk
from tkinter import messagebox

def diagnosticar_dispositivo():

    usuario = entrada_usuario.get().strip()
    dispositivo = entrada_dispositivo.get().strip()

    if not usuario or not dispositivo:
        messagebox.showwarning("Atención", "Por favor ingresa tu nombre y el dispositivo a revisar.")
        return


    electricidad = entrada_electricidad.get().strip().lower() == "si"
    enciende = entrada_enciende.get().strip().lower() == "si"
    imagen = entrada_imagen.get().strip().lower() == "si"


    encabezado_analisis = f"[Analizando {dispositivo}...]"


    if not electricidad:
        diagnostico = "Diagnóstico: El equipo no está recibiendo corriente."
        solucion = (
            f"Solución: {usuario}, checa que el cable esté bien conectado a la pared y prueba en otro enchufe. "
            f"Si el cargador o cable está flojo o dañado, cámbialo. Revisa si en tu comunidad hay luz o solo es tu casa, "
            f"llama al CFE o algún otro electrico para un mejor diágnostico"
        )
    else:
        if not enciende:
            diagnostico = "Diagnóstico: Le llega energía, pero no arranca."
            solucion = (
                f"Solución: {usuario}, deja cargando el equipo unos 20 minutos por si la batería está totalmente vacía. "
                f"Mantén presionado el botón de encendido por 10 segundos para forzar el inicio. "
                f"Si sigue sin responder, llévalo a un técnico."
            )
        else:
            if not imagen:
                diagnostico = "Diagnóstico: El equipo prende (luces o sonido), pero la pantalla se queda en negro."
                solucion = (
                    f"Solución: {usuario}, sube el brillo al máximo por si está muy bajo. Si usas un cable o pantalla externa, "
                    f"asegúrate de que esté bien apretado. Apágalo y vuelve a encenderlo para ver si reacciona. "
                    f"Si lo anterior no funciona llevala con un técnico para un mejor diágnostico."
                )
            else:
                diagnostico = "Diagnóstico: Todo funciona de manera correcta."
                solucion = f"Solución: ¡Buenas noticias, {usuario}! Tu equipo recibe luz, enciende y da imagen sin problemas."


    etiqueta_analisis.config(text=encabezado_analisis)
    etiqueta_diagnostico.config(text=diagnostico)
    etiqueta_solucion.config(text=solucion)



ventana = tk.Tk()
ventana.title("Diagnóstico Técnico de Dispositivos")
ventana.geometry("520x680")
ventana.resizable(False, False)


titulo = tk.Label(
    ventana,
    text="SISTEMA DE DIAGNÓSTICO TÉCNICO",
    font=("Arial", 11, "bold"),
    pady=8
)
titulo.pack()

subtitulo = tk.Label(
    ventana,
    text="Responde las preguntas para analizar el estado de tu equipo.",
    font=("Arial", 9, "italic")
)
subtitulo.pack(pady=(0, 6))


marco_entradas = tk.Frame(ventana, padx=20)
marco_entradas.pack(fill="x")


tk.Label(marco_entradas, text="Por favor, dime tu nombre:", anchor="w").pack(fill="x")
entrada_usuario = tk.Entry(marco_entradas)
entrada_usuario.pack(fill="x", pady=(0, 4))


tk.Label(marco_entradas, text="¿Qué dispositivo estamos revisando hoy?:", anchor="w").pack(fill="x")
entrada_dispositivo = tk.Entry(marco_entradas)
entrada_dispositivo.pack(fill="x", pady=(0, 4))


tk.Label(marco_entradas, text="¿Tiene electricidad? (si/no):", anchor="w").pack(fill="x")
entrada_electricidad = tk.Entry(marco_entradas)
entrada_electricidad.pack(fill="x", pady=(0, 4))


tk.Label(marco_entradas, text="¿Enciende? (si/no):", anchor="w").pack(fill="x")
entrada_enciende = tk.Entry(marco_entradas)
entrada_enciende.pack(fill="x", pady=(0, 4))


tk.Label(marco_entradas, text="¿Muestra imagen? (si/no):", anchor="w").pack(fill="x")
entrada_imagen = tk.Entry(marco_entradas)
entrada_imagen.pack(fill="x", pady=(0, 8))


boton_diagnostico = tk.Button(
    ventana,
    text="Obtener Diagnóstico",
    font=("Arial", 10, "bold"),
    bg="#2B5B84",
    fg="white",
    padx=10,
    pady=4,
    command=diagnosticar_dispositivo
)
boton_diagnostico.pack(pady=8)


tk.Label(ventana, text="--- REPORTE TÉCNICO ---", font=("Arial", 9, "bold")).pack(pady=(4, 2))

etiqueta_analisis = tk.Label(ventana, text="[Esperando datos...]", font=("Arial", 9, "italic"), fg="#555555")
etiqueta_analisis.pack()

etiqueta_diagnostico = tk.Label(
    ventana, 
    text="", 
    font=("Arial", 9, "bold"), 
    fg="#003366", 
    wraplength=480, 
    justify="center"
)
etiqueta_diagnostico.pack(pady=(4, 2))

etiqueta_solucion = tk.Label(
    ventana, 
    text="", 
    font=("Arial", 9), 
    wraplength=480, 
    justify="left"
)
etiqueta_solucion.pack(padx=20, pady=4)

etiqueta_despedida = tk.Label(
    ventana, 
    text="", 
    font=("Arial", 9, "bold"), 
    fg="#2E7D32"
)
etiqueta_despedida.pack(pady=(6, 4))

ventana.mainloop()