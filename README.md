# Suite Optimización - v4.2

Aplicación multiplataforma para gestionar perfiles de optimización de dispositivos Android.

## 🚀 Inicio Rápido

### Windows/Desktop
```bash
python interfaz.py  # Con CustomTkinter (original)
# o
python main.py      # Con Kivy (compatible con Android)
```

### Android - Termux
```bash
bash termux-install.sh
cd ~/SuiteOptimizacion
python3 main.py
```

### Android - APK Compilado
```bash
buildozer android debug
# Instalar bin/suiteopt-4.2-debug.apk en tu teléfono
```

---

## 📁 Estructura del Proyecto

```
suite op/
├── interfaz.py              # App original (CustomTkinter/Windows)
├── main.py                  # App Kivy (Multiplataforma)
├── requirements.txt         # Dependencias Python
├── buildozer.spec          # Configuración para compilar APK
├── termux-install.sh       # Script de instalación Termux
├── ANDROID_SETUP.md        # Guía completa Android
├── README.md               # Este archivo
└── marcas/                 # Tus perfiles de optimización
    ├── Samsung/
    │   ├── Galaxy S21/
    │   │   ├── Nivel1.bat
    │   │   └── Nivel2.bat
    └── Xiaomi/
        └── Redmi Note 10/
            └── Optimizado.bat
```

---

## 🎯 Características

✅ **Selección en cascada**: Marca → Modelo → Nivel  
✅ **Captura en tiempo real**: Stdout/Stderr de scripts en GUI  
✅ **Threading**: No bloquea la interfaz durante ejecución  
✅ **Monitoreo ADB**: Detecta dispositivos Android conectados  
✅ **Multiplataforma**: Windows, Linux, macOS, Android (Termux + APK)

---

## ⚙️ Instalación

### Opción 1: Windows/Desktop (Recomendado para desarrollo)
```bash
# Crear entorno virtual
python -m venv .venv
.\.venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar (CustomTkinter)
python interfaz.py
```

### Opción 2: Termux (en teléfono Android)
Ver: [ANDROID_SETUP.md - Opción 1: Termux](ANDROID_SETUP.md#opción-1-termux)

### Opción 3: APK (en teléfono Android)
Ver: [ANDROID_SETUP.md - Opción 2: APK](ANDROID_SETUP.md#opción-2-apk)

---

## 📋 Requisitos

### Desktop
- Python 3.9+
- Windows/Linux/macOS
- Dependencias en `requirements.txt`

### Termux
- Termux app (Google Play / F-Droid)
- ~500 MB espacio libre
- Conexión a internet

### APK Compilado
- PC con Python 3.9+
- Java JDK 11+
- Android SDK
- ~2 GB espacio libre
- ~30-60 min para compilación inicial

---

## 🎮 Uso

### Flujo básico
1. Selecciona **Fabricante** (marca del teléfono)
2. Selecciona **Modelo Técnico** (modelo específico)
3. Selecciona **Nivel de Perfil** (script a ejecutar)
4. Presiona **"Lanzar Perfil"**
5. Observa el progreso en el panel derecho

### Monitoreo ADB
- Presiona **"🔄 Escanear ADB"** para detectar dispositivos
- Muestra estado de conexión
- Valida autorización USB

---

## 📂 Estructura de Perfiles

Cada perfil es un archivo `.bat` en la carpeta de modelo:

```
marcas/
  MARCA/
    MODELO/
      PERFIL.bat      ← Archivo ejecutable
      OTRO_PERFIL.bat
```

**Ejemplo:**
```
marcas/
  Samsung/
    Galaxy S21/
      Base.bat
      Optimizado.bat
      Máximo.bat
```

---

## 🔧 Configuración Avanzada

### Cambiar tema de la app (CustomTkinter)
En `interfaz.py`:
```python
ctk.set_appearance_mode("light")  # o "dark"
ctk.set_default_color_theme("green")  # tema de color
```

### Cambiar permisos Android
En `buildozer.spec`:
```ini
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE
```

### Aumentar tamaño de consola
En `main.py`, busca `altura = 180` y aumenta el valor.

---

## 🐛 Solución de Problemas

| Problema | Solución |
|----------|----------|
| "No se encuentra el módulo kivy" | `pip install kivy` |
| "ImportError customtkinter" | Solo para `interfaz.py`: `pip install customtkinter` |
| "ADB not found" | Instala Android SDK o copia `adb.exe` a la carpeta |
| "Permisos denegados en Android" | Otorga permisos en Configuración → Aplicaciones |
| "La app se cierra al iniciar" | Revisa logs con `adb logcat` |
| "Scripts .bat no se ejecutan" | Verifica la ruta en `marcas/MARCA/MODELO/` |

Ver más: [ANDROID_SETUP.md - Troubleshooting](ANDROID_SETUP.md#troubleshooting)

---

## 📝 Notas Técnicas

### Diferencias: interfaz.py vs main.py
- **interfaz.py**: CustomTkinter (solo Windows/Linux/macOS)
- **main.py**: Kivy (Android + Desktop)

Usa `interfaz.py` para desarrollo en Windows, `main.py` para Android.

### Captura de procesos
Ambas versiones capturan:
- ✓ Salida estándar (stdout)
- ✓ Errores (stderr)
- ✓ Códigos de retorno
- ✓ Excepciones de ejecución

### Threading
- Los scripts se ejecutan en threads separados
- La GUI permanece responsiva
- Las actualizaciones son thread-safe

---

## 🎨 Personalización

### Cambiar colores en Kivy (main.py)
En la clase `SuiteOptimizacionApp`, modifica:
```python
btn_ejecutar.background_color = (0.1, 0.3, 0.5, 1)  # RGBA
btn_adb.background_color = (0.0, 0.5, 0.0, 1)       # Verde
```

### Cambiar icono del APK
Añade `icon.png` (512x512) a la carpeta raíz y en `buildozer.spec`:
```ini
icon.filename = %(source.dir)s/icon.png
```

---

## 📞 Soporte

### Para errores en Desktop
1. Activa el venv: `.\.venv\Scripts\activate`
2. Ejecuta con logs: `python -u main.py`
3. Revisa los mensajes de error

### Para errores en Termux
```bash
# Revisa logs
python3 main.py 2>&1 | tee app.log

# Instala lo que falte
pip install NOMBRE_PAQUETE
```

### Para errores en APK
```bash
# Conecta por USB y revisa logs del dispositivo
adb logcat | grep -i "suite\|kivy\|python"
```

---

## 📄 Licencia

Proyecto educativo. Uso libre para optimización de dispositivos Android.

---

**Última actualización**: 2026-06-03  
**Versión**: 4.2  
**Estado**: ✅ Producción

