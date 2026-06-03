#:kivy 2.0

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
import subprocess
import os
import threading
import json
from pathlib import Path

# Configurar tamaño de ventana
Window.size = (720, 1000)

class SuiteOptimizacionApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.setup_android_paths()
        
    def setup_android_paths(self):
        """Configura rutas para Android/Termux/Desktop"""
        try:
            # Intenta usar rutas Android
            from android.storage import primary_external_storage_path
            self.ruta_base = primary_external_storage_path()
        except ImportError:
            # Fallback para Termux/Desktop
            home = os.path.expanduser("~")
            self.ruta_base = os.path.join(home, "Documents", "SuiteOptimizacion")
        
        self.ruta_marcas = os.path.join(self.ruta_base, "marcas")
        self.adb_local = os.path.join(self.ruta_base, "adb")
        
        # Crear directorios si no existen
        os.makedirs(self.ruta_marcas, exist_ok=True)
        os.makedirs(self.ruta_base, exist_ok=True)

    def build(self):
        """Construye la interfaz Kivy"""
        root = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Título
        titulo = Label(text='ENGINEERING ANDROID SUITE v4.2', size_hint_y=0.08, 
                      font_size='20sp', bold=True)
        root.add_widget(titulo)
        
        # Layout principal (filtros + monitor)
        main_layout = GridLayout(cols=2, spacing=10, size_hint_y=0.85)
        
        # --- FRAME FILTROS (izquierda) ---
        filtros_layout = BoxLayout(orientation='vertical', spacing=8, size_hint_x=0.4)
        
        # Fabricante
        filtros_layout.add_widget(Label(text='1. Fabricante:', size_hint_y=0.06, bold=True))
        marcas = self.obtener_marcas()
        self.spinner_marca = Spinner(text=marcas[0] if marcas else 'Sin marcas',
                                     values=marcas,
                                     size_hint_y=0.08)
        self.spinner_marca.bind(text=self.actualizar_modelos)
        filtros_layout.add_widget(self.spinner_marca)
        
        # Modelo
        filtros_layout.add_widget(Label(text='2. Modelo Técnico:', size_hint_y=0.06, bold=True))
        self.spinner_modelo = Spinner(text='Selecciona Marca', values=['Selecciona Marca'],
                                      size_hint_y=0.08)
        self.spinner_modelo.bind(text=self.actualizar_niveles)
        filtros_layout.add_widget(self.spinner_modelo)
        
        # Nivel
        filtros_layout.add_widget(Label(text='3. Nivel de Perfil:', size_hint_y=0.06, bold=True))
        self.spinner_nivel = Spinner(text='Selecciona Modelo', values=['Selecciona Modelo'],
                                     size_hint_y=0.08)
        filtros_layout.add_widget(self.spinner_nivel)
        
        # Botón ejecutar
        btn_ejecutar = Button(text='▶ Lanzar Perfil', size_hint_y=0.1, background_color=(0.1, 0.3, 0.5, 1))
        btn_ejecutar.bind(on_press=self.ejecutar_script_nivel)
        filtros_layout.add_widget(btn_ejecutar)
        
        main_layout.add_widget(filtros_layout)
        
        # --- FRAME MONITOR (derecha) ---
        monitor_layout = BoxLayout(orientation='vertical', spacing=8, size_hint_x=0.6)
        monitor_layout.add_widget(Label(text='Monitor de Hardware ADB', size_hint_y=0.06, bold=True))
        
        # Textbox de salida
        self.textbox_consola = TextInput(multiline=True, readonly=True, 
                                        font_size='10sp', size_hint_y=0.75)
        monitor_layout.add_widget(self.textbox_consola)
        
        # Botón escaneo ADB
        btn_adb = Button(text='🔄 Escanear ADB', size_hint_y=0.1, background_color=(0.0, 0.5, 0.0, 1))
        btn_adb.bind(on_press=self.verificar_adb)
        monitor_layout.add_widget(btn_adb)
        
        main_layout.add_widget(monitor_layout)
        root.add_widget(main_layout)
        
        # Status bar
        self.status_label = Label(text='Aplicación inicializada.', size_hint_y=0.07, 
                                 font_size='11sp', italic=True)
        root.add_widget(self.status_label)
        
        # Inicializar
        if marcas and marcas[0] != 'Sin marcas':
            self.actualizar_modelos(marcas[0])
        
        return root

    def obtener_marcas(self):
        """Lee carpetas de marcas disponibles"""
        try:
            if os.path.exists(self.ruta_marcas):
                marcas = [f for f in os.listdir(self.ruta_marcas) 
                         if os.path.isdir(os.path.join(self.ruta_marcas, f))]
                return marcas if marcas else ['Sin marcas']
            return ['Sin marcas']
        except:
            return ['Error leyendo marcas']

    def actualizar_modelos(self, spinner, texto):
        """Actualiza lista de modelos según marca seleccionada"""
        ruta_modelos = os.path.join(self.ruta_marcas, texto)
        if os.path.exists(ruta_modelos):
            modelos = [f for f in os.listdir(ruta_modelos)
                      if os.path.isdir(os.path.join(ruta_modelos, f))]
            if modelos:
                self.spinner_modelo.values = modelos
                self.spinner_modelo.text = modelos[0]
                self.actualizar_niveles(self.spinner_modelo, modelos[0])
            else:
                self.spinner_modelo.values = ['Sin modelos']
                self.spinner_modelo.text = 'Sin modelos'
        else:
            self.spinner_modelo.values = ['Ruta inexistente']
            self.spinner_modelo.text = 'Ruta inexistente'

    def actualizar_niveles(self, spinner, texto):
        """Actualiza lista de niveles según modelo seleccionado"""
        marca = self.spinner_marca.text
        ruta_niveles = os.path.join(self.ruta_marcas, marca, texto)
        if os.path.exists(ruta_niveles):
            niveles = [f.replace('.bat', '') for f in os.listdir(ruta_niveles) 
                      if f.endswith('.bat')]
            if niveles:
                self.spinner_nivel.values = niveles
                self.spinner_nivel.text = niveles[0]
            else:
                self.spinner_nivel.values = ['Sin perfiles']
                self.spinner_nivel.text = 'Sin perfiles'

    def ejecutar_script_nivel(self, instance):
        """Ejecuta el script .bat del nivel seleccionado"""
        marca = self.spinner_marca.text
        modelo = self.spinner_modelo.text
        nivel = self.spinner_nivel.text
        
        archivo_bat = os.path.join(self.ruta_marcas, marca, modelo, f"{nivel}.bat")
        
        if os.path.exists(archivo_bat):
            self.status_label.text = f"▶ Procesando: {nivel}..."
            self.textbox_consola.text = f"[INICIANDO] {nivel}\n{'='*40}\n"
            
            thread = threading.Thread(target=self._ejecutar_en_background, 
                                     args=(archivo_bat, nivel))
            thread.daemon = True
            thread.start()
        else:
            self.textbox_consola.text = f"[ERROR] Archivo no encontrado: {archivo_bat}"
            self.status_label.text = "Error: Perfil no existe"

    def _ejecutar_en_background(self, archivo_bat, nivel):
        """Ejecuta script en background y captura output"""
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
            codigo_retorno = proceso.returncode
            
            if codigo_retorno == 0:
                self._actualizar_consola(f"\n✓ {nivel} completado exitosamente.")
                self.status_label.text = f"✓ {nivel} finalizado."
            else:
                self._actualizar_consola(f"\n✗ Error: Código {codigo_retorno}")
                self.status_label.text = f"✗ Fallo en {nivel}"
                
        except Exception as e:
            self._actualizar_consola(f"\n[EXCEPCIÓN] {str(e)}")
            self.status_label.text = "Error en ejecución"

    def _actualizar_consola(self, texto):
        """Actualiza textbox desde background thread"""
        self.textbox_consola.text += texto + '\n'

    def verificar_adb(self, instance):
        """Verifica dispositivos ADB conectados"""
        self.status_label.text = "Escaneando ADB..."
        self.textbox_consola.text = "[ESCANEO ADB]\n" + "="*40 + "\n"
        
        thread = threading.Thread(target=self._escanear_adb)
        thread.daemon = True
        thread.start()

    def _escanear_adb(self):
        """Ejecuta escaneo ADB en background"""
        try:
            cmd_adb = self.adb_local if os.path.exists(self.adb_local) else "adb"
            resultado = subprocess.run([cmd_adb, "devices"], 
                                     capture_output=True, text=True, shell=True)
            
            lineas = resultado.stdout.strip().split("\n")
            dispositivos = 0
            
            for linea in lineas[1:]:
                if linea.strip():
                    partes = linea.split("\t")
                    if len(partes) == 2:
                        serial, estado = partes[0], partes[1]
                        estado_limpio = {
                            "device": "✓ LISTO",
                            "unauthorized": "⚠️ AUTORIZAR",
                            "offline": "✗ DESCONECTADO"
                        }.get(estado, estado.upper())
                        
                        self._actualizar_consola(f"ID: {serial}\nEstado: {estado_limpio}\n---")
                        dispositivos += 1
            
            if dispositivos == 0:
                self._actualizar_consola("No hay dispositivos conectados.")
                self.status_label.text = "Bus ADB vacío"
            else:
                self.status_label.text = f"✓ {dispositivos} dispositivo(s) detectado(s)"
                
        except Exception as e:
            self._actualizar_consola(f"[ERROR ADB] {str(e)}")
            self.status_label.text = "Error ADB"


class SuiteOptimizacionAndroid(SuiteOptimizacionApp):
    """Variante para Android con permisos específicos"""
    
    def request_android_permissions(self):
        """Solicita permisos necesarios en Android"""
        try:
            from android.permissions import request_permissions, Permission
            permissions = [
                Permission.INTERNET,
                Permission.READ_EXTERNAL_STORAGE,
                Permission.WRITE_EXTERNAL_STORAGE,
            ]
            request_permissions(permissions)
        except ImportError:
            pass  # No es Android


if __name__ == '__main__':
    app = SuiteOptimizacionApp()
    app.run()
