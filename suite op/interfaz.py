import customtkinter as ctk
import subprocess
import os

# Configuración del estilo visual (Modo Oscuro y Azul Tecnológico)
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class SuiteOptimizacion(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configuración de la Ventana Principal
        self.title("Suite de Optimización Android PRO v1.0")
        self.geometry("500x550")
        self.resizable(False, False)

        # Título Superior
        self.label_titulo = ctk.CTkLabel(self, text="ANDROID OPTIMIZER", font=ctk.CTkFont(size=24, weight="bold"))
        self.label_titulo.pack(pady=20)

        self.label_sub = ctk.CTkLabel(self, text="Selecciona la marca del dispositivo conectado", font=ctk.CTkFont(size=14))
        self.label_sub.pack(pady=5)

        # Contenedor de Botones
        self.frame_botones = ctk.CTkFrame(self)
        self.frame_botones.pack(pady=20, padx=40, fill="both", expand=True)

        # Creación de Botones Modernos
        self.btn_moto = ctk.CTkButton(self.frame_botones, text="Optimizar Motorola", command=lambda: self.ejecutar_tweak("1"), height=40)
        self.btn_moto.pack(pady=10, padx=20, fill="x")

        self.btn_xiaomi = ctk.CTkButton(self.frame_botones, text="Optimizar Xiaomi / POCO", command=lambda: self.ejecutar_tweak("2"), height=40)
        self.btn_xiaomi.pack(pady=10, padx=20, fill="x")

        self.btn_samsung = ctk.CTkButton(self.frame_botones, text="Optimizar Samsung", command=lambda: self.ejecutar_tweak("3"), height=40)
        self.btn_samsung.pack(pady=10, padx=20, fill="x")

        self.btn_inf = ctk.CTkButton(self.frame_botones, text="Optimizar Infinix / Tecno", command=lambda: self.ejecutar_tweak("4"), height=40)
        self.btn_inf.pack(pady=10, padx=20, fill="x")

        # Botón de Estado / Conexión
        self.btn_check = ctk.CTkButton(self, text="Verificar Conexión ADB", fg_color="green", hover_color="darkgreen", command=lambda: self.ejecutar_tweak("5"), height=45)
        self.btn_check.pack(pady=20)

    def ejecutar_tweak(self, opcion):
        # Este método comunica la interfaz bonita con tu potente motor .bat anterior
        if os.path.exists("Suite_Optimizacion.bat"):
            # Llama al script enviando la opción automáticamente
            subprocess.Popen(f"echo {opcion} | Suite_Optimizacion.bat", shell=True)
        else:
            print("Error: No se encuentra el archivo Suite_Optimizacion.bat en esta carpeta.")

if __name__ == "__main__":
    app = SuiteOptimizacion()
    app.mainloop()
