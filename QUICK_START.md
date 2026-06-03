# 🚀 Quick Start - Suite Optimización en Android

## 🎯 Elige tu camino

### 👉 **Opción 1: Termux (MÁS FÁCIL - 5 minutos)**

#### Paso 1: Instalar Termux
- Descarga **Termux** desde Google Play o F-Droid
- Abre la app

#### Paso 2: Ejecutar setup
```bash
cd ~
wget https://raw.githubusercontent.com/TU_REPO/termux-install.sh
bash termux-install.sh
```

O manualmente:
```bash
pkg update -y && pkg upgrade -y
pkg install -y python3 python3-pip
pip install kivy requests
mkdir -p ~/SuiteOptimizacion/marcas
cd ~/SuiteOptimizacion
```

#### Paso 3: Copiar archivos
- Descarga `main.py` a: `~/SuiteOptimizacion/`
- Copia tu carpeta `marcas/` a: `~/SuiteOptimizacion/marcas/`

#### Paso 4: Ejecutar
```bash
cd ~/SuiteOptimizacion
python3 main.py
```

✅ **¡Listo!** La app se abrirá en pantalla completa.

---

### 👉 **Opción 2: APK Compilado (RECOMENDADO - 1 hora)**

#### Requisitos en PC
- [Java JDK 11+](https://www.oracle.com/java/)
- [Python 3.9+](https://www.python.org/)
- Git (opcional)

#### Paso 1: Preparar PC
```bash
# Instalar herramientas de compilación
pip install buildozer cython

# En Windows, copia tu carpeta del proyecto
# En Linux/Mac: automático
```

#### Paso 2: Compilar
```bash
cd "C:\Users\tu_usuario\Desktop\dante\suite op"

# Primera vez tarda 30-60 minutos
buildozer android debug
```

#### Paso 3: Instalar en teléfono
```bash
# Conéctalo por USB con modo debug activado
adb install bin/suiteopt-4.2-debug.apk

# O: Copia el APK a tu teléfono y abre manualmente
```

#### Paso 4: Copiar datos
- Abre la app "Suite Optimización"
- Copia tu carpeta `marcas/` a: `/storage/emulated/0/SuiteOptimizacion/marcas/`

✅ **¡Listo!** La app está instalada en tu teléfono.

---

## 📋 Estructura de carpetas (Ejemplo)

```
~/SuiteOptimizacion/              (Termux)
o
/storage/emulated/0/SuiteOptimizacion/  (Dispositivo Android)

├── main.py
└── marcas/
    ├── Samsung/
    │   └── Galaxy S21/
    │       ├── Base.bat
    │       ├── Optimizado.bat
    │       └── Máximo.bat
    ├── Xiaomi/
    │   └── Redmi Note 10/
    │       └── Rendimiento.bat
    └── OnePlus/
        └── 9 Pro/
            └── Gaming.bat
```

### 🔑 Regla de oro
**Cada `.bat` = 1 perfil disponible en la app**

---

## ⚠️ Si algo falla

### Termux:
```bash
# Ver todos los errores
python3 main.py 2>&1 | tee debug.log

# Reinstalar Kivy
pip uninstall kivy -y
pip install kivy
```

### APK:
```bash
# Ver logs del dispositivo
adb logcat | grep Suite
# o
adb logcat | grep Python
```

---

## 🎮 Uso de la app

1. Abre **Suite Optimización**
2. Selecciona **Fabricante** (Samsung, Xiaomi, etc)
3. Selecciona **Modelo** (Galaxy S21, Redmi Note 10, etc)
4. Selecciona **Nivel** (Base, Optimizado, etc)
5. Presiona **"▶ Lanzar Perfil"**
6. ¡Observa el progreso en la consola!

---

## 📱 Compatibilidad

| Dispositivo | Opción | ¿Funciona? |
|-------------|--------|-----------|
| Android 10+ | Termux | ✅ Sí |
| Android 10+ | APK | ✅ Sí |
| Android 8-9 | Termux | ⚠️ Quizá |
| Android 8-9 | APK | ✅ Sí |
| Termux en Android | Ambas | ✅ Sí |

---

## 🆘 Necesitas ayuda?

**Para Termux:**
1. ¿Kivy no instala? → `pkg install build-essential libffi-dev`
2. ¿Permisos? → Configuración → Aplicaciones → Termux → Almacenamiento
3. ¿Lentitud? → Aumenta RAM disponible, cierra otras apps

**Para APK:**
1. ¿Falla compilación? → `buildozer android clean` y reintenta
2. ¿No se instala? → Activa USB Debug en el teléfono
3. ¿Se cierra al abrir? → Revisa permisos de almacenamiento

---

## 🎁 Bonus: Comandos útiles

```bash
# Termux - Listar dispositivos ADB
adb devices

# Termux - Transferir carpeta completa
scp -r marcas/ usuario@pc:/ruta/

# PC - Ver logs en tiempo real
adb logcat -v threadtime

# APK - Reinstalar
adb uninstall com.engineering.android.suiteopt
adb install bin/suiteopt-4.2-debug.apk
```

---

**¡Ya estás listo!** 🎉

Elige Termux para empezar rápido, o APK para una app profesional.
