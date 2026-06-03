import customtkinter as ctk
import subprocess
import os
import urllib.request
import zipfile
import threading

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class SuiteOptimizacion(ctk.CTk):
    def __init__(self):
        super().__init__()

        ruta_del_script = os.path.dirname(os.path.abspath(__file__))
        self.ruta_marcas = os.path.join(ruta_del_script, "marcas")
        self.adb_local = os.path.join(ruta_del_script, "adb.exe")

        self.title("Suite de Optimización Profesional v4.2")
        self.geometry("750x580")
        self.resizable(False, False)

        self.label_titulo = ctk.CTkLabel(self, text="ENGINEERING ANDROID SUITE", font=ctk.CTkFont(size=24, weight="bold"))
        self.label_titulo.pack(pady=15)

        self.frame_operaciones = ctk.CTkFrame(self)
        self.frame_operaciones.pack(pady=10, padx=25, fill="both", expand=True)
        self.frame_operaciones.columnconfigure(0, weight=4)  
        self.frame_operaciones.columnconfigure(1, weight=5)  

        self.frame_filtros = ctk.CTkFrame(self.frame_operaciones, fg_color="transparent")
        self.frame_filtros.grid(row=0, column=0, pady=10, padx=15, sticky="nsew")

        self.label_marca = ctk.CTkLabel(self.frame_filtros, text="1. Fabricante:", font=ctk.CTkFont(size=13, weight="bold"))
        self.label_marca.pack(pady=(10, 2), anchor="w")
        
        marcas_disponibles = self.obtener_marcas()
        self.combo_marcas = ctk.CTkOptionMenu(self.frame_filtros, values=marcas_disponibles, command=self.actualizar_modelos)
        self.combo_marcas.pack(pady=5, fill="x")

        self.label_modelo = ctk.CTkLabel(self.frame_filtros, text="2. Modelo Técnico:", font=ctk.CTkFont(size=13, weight="bold"))
        self.label_modelo.pack(pady=(15, 2), anchor="w")
        
        self.combo_modelos = ctk.CTkOptionMenu(self.frame_filtros, values=["Selecciona Marca"], command=self.actualizar_niveles)
        self.combo_modelos.pack(pady=5, fill="x")

        self.label_nivel = ctk.CTkLabel(self.frame_filtros, text="3. Nivel de Perfil:", font=ctk.CTkFont(size=13, weight="bold"))
        self.label_nivel.pack(pady=(15, 2), anchor="w")
        
        self.combo_niveles = ctk.CTkOptionMenu(self.frame_filtros, values=["Selecciona Modelo"])
        self.combo_niveles.pack(pady=5, fill="x")

        self.btn_ejecutar = ctk.CTkButton(self.frame_filtros, text="Lanzar Perfil Seleccionado", fg_color="#1f538d", font=ctk.CTkFont(size=13, weight="bold"), command=self.ejecutar_script_nivel, height=45)
        self.btn_ejecutar.pack(pady=(25, 0), fill="x")

        self.frame_monitor = ctk.CTkFrame(self.frame_operaciones)
        self.frame_monitor.grid(row=0, column=1, pady=15, padx=15, sticky="nsew")

        self.label_monitor = ctk.CTkLabel(self.frame_monitor, text="Monitor de Hardware ADB", font=ctk.CTkFont(size=13, weight="bold"))
        self.label_monitor.pack(pady=(10, 5))

        self.lista_dispositivos = ctk.CTkTextbox(self.frame_monitor, height=180, font=ctk.CTkFont(family="Courier", size=12))
        self.lista_dispositivos.pack(pady=5, padx=15, fill="both", expand=True)
        self.lista_dispositivos.configure(state="disabled") 

        self.btn_escaneo = ctk.CTkButton(self.frame_monitor, text="🔄 Escanear Bus / Estado ADB", fg_color="green", hover_color="darkgreen", font=ctk.CTkFont(size=13, weight="bold"), command=self.verificar_y_listar_adb, height=40)
        self.btn_escaneo.pack(pady=15, padx=15, fill="x")

        self.status_label = ctk.CTkLabel(self, text="Consola unificada inicializada.", font=ctk.CTkFont(size=12, slant="italic"))
        self.status_label.pack(pady=10)

        self.verificar_y_descargar_adb_so(ruta_del_script)

        if marcas_disponibles and marcas_disponibles not in ["Sin marcas en la carpeta", "Crea la carpeta 'marcas'"]:
            self.combo_marcas.set(marcas_disponibles[0])
            self.actualizar_modelos(marcas_disponibles[0])
            
        self.verificar_y_listar_adb()

    def verificar_y_descargar_adb_so(self, ruta_base):
        if not os.path.exists(self.adb_local):
            self.status_label.configure(text="Infraestructura incompleta. Descargando ADB de Google...")
            self.update()
            try:
                url = "https://google.com"
                zip_path = os.path.join(ruta_base, "platform-tools.zip")
                urllib.request.urlretrieve(url, zip_path)
                
                with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                    for member in zip_ref.namelist():
                        filename = os.path.basename(member)
                        if filename in ["adb.exe", "AdbWinApi.dll", "AdbWinUsbApi.dll", "fastboot.exe"]:
                            source = zip_ref.open(member)
                            target = open(os.path.join(ruta_base, filename), "wb")
                            with source, target:
                                target.write(source.read())
                os.remove(zip_path)
                self.status_label.configure(text="¡Entorno ADB configurado de forma automática!")
            except Exception:
                self.status_label.configure(text="Error al auto-instalar ADB: No hay internet.")

    def verificar_y_listar_adb(self):
        self.lista_dispositivos.configure(state="normal")
        self.lista_dispositivos.delete("1.0", "end")
        
        cmd_adb = f'"{self.adb_local}"' if os.path.exists(self.adb_local) else "adb"
        
        try:
            resultado = subprocess.run([cmd_adb, "devices"], capture_output=True, text=True, shell=True)
            lineas = resultado.stdout.strip().split("\n")
            dispositivos_encontrados = 0
            
            for linea in lineas[1:]:
                if linea.strip():
                    partes = linea.split("\t")
                    if len(partes) == 2:
                        serial = partes[0]
                        estado_raw = partes[1]
                        
                        if estado_raw == "device":
                            estado_limpio = "AUTORIZADO / LISTO"
                        elif estado_raw == "unauthorized":
                            estado_limpio = "⚠️ SIN AUTORIZAR (Mira el móvil)"
                        elif estado_raw == "offline":
                            estado_limpio = "DESCONECTADO"
                        else:
                            estado_limpio = estado_raw.upper()
                            
                        self.lista_dispositivos.insert("end", f"ID: {serial}\nEstado: {estado_limpio}\n-------------------------------\n")
                        dispositivos_encontrados += 1
            
            if dispositivos_encontrados > 0:
                self.status_label.configure(text=f"Mapeo exitoso. {dispositivos_encontrados} terminal(es) listo(s).")
            else:
                self.lista_dispositivos.insert("end", "   [ No hay teléfonos conectados ]\n\nPasos obligatorios:\n1. Activa Depuración USB.\n2. Conecta el cable original.\n3. Presiona el botón verde de abajo.")
                self.status_label.configure(text="Aviso: Bus ADB vacío. Conecta un dispositivo.")
                
        except Exception as e:
            self.lista_dispositivos.insert("end", f"ERROR ADB:\nFalla crítica.\nDetalle: {str(e)}")
            self.status_label.configure(text="Error: Entorno ADB inaccesible.")
            
        self.lista_dispositivos.configure(state="disabled")

    def obtener_marcas(self):
        if os.path.exists(self.ruta_marcas):
            marcas = [f for f in os.listdir(self.ruta_marcas) if os.path.isdir(os.path.join(self.ruta_marcas, f))]
            return marcas if marcas else ["Sin marcas en la carpeta"]
        else:
            os.makedirs(self.ruta_marcas, exist_ok=True)
            return ["Crea la carpeta 'marcas'"]

    def actualizar_modelos(self, marca_seleccionada):
        ruta_modelos = os.path.join(self.ruta_marcas, marca_seleccionada)
        if os.path.exists(ruta_modelos):
            modelos = [f for f in os.listdir(ruta_modelos) if os.path.isdir(os.path.join(ruta_modelos, f))]
            if modelos:
                self.combo_modelos.configure(values=modelos)
                self.combo_modelos.set(modelos[0])
                self.actualizar_niveles(modelos[0])
            else:
                self.combo_modelos.configure(values=["Crea carpetas de Modelos"])
                self.combo_modelos.set("Crea carpetas de Modelos")
                self.combo_niveles.configure(values=["-"])
                self.combo_niveles.set("-")

    def actualizar_niveles(self, modelo_seleccionado):
        marca = self.combo_marcas.get()
        ruta_niveles = os.path.join(self.ruta_marcas, marca, modelo_seleccionado)
        if os.path.exists(ruta_niveles):
            niveles = [f.replace(".bat", "") for f in os.listdir(ruta_niveles) if f.endswith(".bat")]
            if niveles:
                self.combo_niveles.configure(values=niveles)
                self.combo_niveles.set(niveles[0])
            else:
                self.combo_niveles.configure(values=["Faltan archivos .bat"])
                self.combo_niveles.set("Faltan archivos .bat")

    def ejecutar_script_nivel(self):
        marca = self.combo_marcas.get()
        modelo = self.combo_modelos.get()
        nivel = self.combo_niveles.get()
        
        archivo_bat = os.path.join(self.ruta_marcas, marca, modelo, f"{nivel}.bat")
        
        if os.path.exists(archivo_bat):
            self.status_label.configure(text=f"▶ Procesando: {nivel}...")
            self.lista_dispositivos.configure(state="normal")
            self.lista_dispositivos.delete("1.0", "end")
            self.lista_dispositivos.insert("end", f"[INICIANDO] {nivel}\n{'='*40}\n")
            self.lista_dispositivos.configure(state="disabled")
            
            thread = threading.Thread(target=self._ejecutar_en_background, args=(archivo_bat, nivel))
            thread.daemon = True
            thread.start()
        else:
            self.status_label.configure(text="Error: Archivo de optimización ausente.")

    def _ejecutar_en_background(self, archivo_bat, nivel):
        try:
            proceso = subprocess.Popen(
                [archivo_bat],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                shell=True,
                bufsize=1
            )
            
            for linea in proceso.stdout:
                self._actualizar_consola(linea.rstrip())
            
            for linea in proceso.stderr:
                self._actualizar_consola(f"[ERROR] {linea.rstrip()}")
            
            proceso.wait()
            código_retorno = proceso.returncode
            
            if código_retorno == 0:
                self._actualizar_consola(f"\n✓ {nivel} completado exitosamente.")
                self.status_label.configure(text=f"✓ {nivel} finalizado.")
            else:
                self._actualizar_consola(f"\n✗ Error: Código de salida {código_retorno}")
                self.status_label.configure(text=f"✗ Fallo en {nivel}")
                
        except Exception as e:
            self._actualizar_consola(f"\n[EXCEPCIÓN] {str(e)}")
            self.status_label.configure(text="Error: No se pudo ejecutar el script.")

    def _actualizar_consola(self, texto):
        self.lista_dispositivos.configure(state="normal")
        self.lista_dispositivos.insert("end", texto + "\n")
        self.lista_dispositivos.see("end")
        self.lista_dispositivos.configure(state="disabled")
        self.update_idletasks()

if __name__ == "__main__":
    try:
        app = SuiteOptimizacion()
        app.mainloop()
    except Exception as e:
        print("\n=== CRASH DE SOFTWARE DETECTADO ===")
