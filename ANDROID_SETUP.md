# 📱 Suite Optimización en Android - Guía Completa

## 📋 Índice
1. [Opción 1: Ejecutar en Termux (Más fácil)](#opción-1-termux)
2. [Opción 2: Compilar APK (Recomendado)](#opción-2-apk)
3. [Estructura de carpetas requerida](#estructura)
4. [Solución de problemas](#troubleshooting)

---

## Opción 1: Termux

### ✅ Requisitos
- Termux instalado en Android
- Conexión a internet
- ~500 MB de espacio libre

### 📥 Instalación Rápida

```bash
# 1. Abre Termux y ejecuta:
bash termux-install.sh

# 2. Espera a que termine (5-10 minutos)

# 3. Verifica que todo esté bien:
pip list | grep kivy

# 4. Ejecuta la app:
cd ~/SuiteOptimizacion
python3 main.py
```

### 🎮 Uso en Termux
- La GUI aparecerá en pantalla completa
- Puedes minimizar con el botón "Back"
- Los logs aparecen en la terminal
- Ctrl+C para salir

### ⚠️ Limitaciones en Termux
- ADB requiere conexión a dispositivo remoto
- No hay acceso directo a rutas del sistema
- Usar `/storage/emulated/0/` para archivos

---

## Opción 2: APK Compilada

### ✅ Requisitos (en PC)
- Java JDK 11+ (https://www.oracle.com/java/technologies/downloads/)
- Android SDK (https://developer.android.com/studio)
- Python 3.9+
- Git

### 📥 Instalación Paso a Paso

#### Paso 1: Preparar entorno en PC
```bash
# En tu PC, instala Buildozer
pip install buildozer cython

# Instala dependencias del sistema (Windows PowerShell como Admin):
# Java JDK ya debe estar instalado

# Si usas WSL (Windows Subsystem for Linux):
sudo apt-get install build-essential libssl-dev libffi-dev
```

#### Paso 2: Compilar APK
```bash
# En la carpeta del proyecto
cd "c:\Users\elsa payo\Desktop\dante\suite op"

# Compilar (primera vez tarda 30-60 min)
buildozer android debug

# El APK se genera en: bin/suiteopt-4.2-debug.apk
```

#### Paso 3: Instalar en Android
```bash
# Opción A: Conéctar por USB y instalar directamente
adb install bin/suiteopt-4.2-debug.apk

# Opción B: Transferir archivo a Android manualmente
# - Copia el APK a tu teléfono
# - Abre el archivo APK para instalar
```

### 🎯 Ventajas del APK
- ✓ No necesita Python en el teléfono
- ✓ Mejor rendimiento
- ✓ Acceso a más permisos
- ✓ Se integra con el sistema Android
- ✓ Icono en el launcher

---

## Estructura de Carpetas Requerida

```
~/SuiteOptimizacion/                   (o /storage/emulated/0/SuiteOptimizacion/)
├── main.py                             # Aplicación Kivy
├── marcas/                             # Carpeta de perfiles
│   ├── Samsung/
│   │   ├── Galaxy S21/
│   │   │   ├── Nivel1.bat
│   │   │   ├── Nivel2.bat
│   │   │   └── Nivel3.bat
│   │   └── Galaxy A52/
│   │       └── Nivel1.bat
│   └── Xiaomi/
│       └── Redmi Note 10/
│           └── Optimizado.bat
├── adb                                 # (opcional) binario ADB local
└── logs/                               # (auto-creada) para registros
```

### 📂 Cómo estructurar tus perfiles
1. Crea carpeta: `marcas/TU_MARCA/TU_MODELO/`
2. Mete archivos `.bat` con nombres descriptivos
3. Cada `.bat` = un perfil disponible

---

## Troubleshooting

### ❌ "ImportError: No module named 'kivy'"
```bash
# En Termux:
pip install kivy

# En PC (para probar antes de compilar):
pip install kivy
```

### ❌ "ADB not found"
- Asegúrate de tener ADB en la ruta
- O copia `adb` a la carpeta de la app
- En Termux: `pkg install android-tools`

### ❌ "El APK no se genera"
```bash
# Limpia y reintenta
buildozer android clean
buildozer android debug

# Si falla, revisa: buildozer.spec
```

### ❌ "Permisos denegados en Android"
- Abre: Configuración → Aplicaciones → Suite Optimización
- Otorga permisos: Almacenamiento, Archivos

### ❌ "La app se cierra al iniciar"
- Revisa los logs: `adb logcat | grep kivy`
- Asegúrate de que `/marcas/` existe

---

## 🔧 Configuración Avanzada

### Modificar buildozer.spec
```ini
# Para cambiar nombre de app:
title = Mi Suite Personalizada

# Para cambiar versión:
version = 5.0

# Para añadir permisos:
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,ACCESS_FINE_LOCATION
```

### Variables de entorno en Termux
```bash
# Aumentar memoria disponible para Kivy
export KIVY_WINDOW=pygame

# Modo debug
export KIVY_LOG_MODE=PIPE
```

---

## 📊 Comparativa: Termux vs APK

| Aspecto | Termux | APK |
|--------|--------|-----|
| Instalación | 5-10 min | 30-60 min (primera vez) |
| Requisitos | Solo Termux | PC + Java + Android SDK |
| Rendimiento | Bueno | Excelente |
| Facilidad | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| Distribución | No | Sí (Google Play, etc) |
| Permisos | Limitados | Completos |

---

## 🚀 Próximos Pasos

### Para Termux (Recomendado si es tu primer intento):
1. Abre Termux
2. `bash termux-install.sh`
3. Copia tu carpeta `marcas/` a `~/SuiteOptimizacion/marcas/`
4. `python3 main.py`

### Para APK (Para producción):
1. Instala requisitos en PC
2. `buildozer android debug`
3. Instala el APK en tu teléfono
4. Copia carpeta `marcas/` a `/storage/emulated/0/SuiteOptimizacion/marcas/`

---

## 📞 Soporte

Si encuentras problemas:
- Revisa los logs de Termux (scroll arriba)
- En PC: `adb logcat | grep Python`
- Verifica que la estructura de carpetas sea correcta
- Asegúrate de permisos en Android

¡Listo! 🎉
