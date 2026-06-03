# 🚀 Acceso a GitHub + APK Personal en Termux/Android

## 📋 Objetivo
1. Acceder a tu repositorio GitHub desde Termux
2. Clonar Android-Optimizer-Suite
3. Compilar APK personal para uso exclusivo

---

## Fase 1: Setup Git en Termux ⚙️

### En tu Termux (5 minutos):

```bash
# 1. Actualizar paquetes
pkg update -y && pkg upgrade -y

# 2. Instalar Git
pkg install -y git

# 3. Configurar Git (reemplaza CON TUS DATOS)
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"

# 4. Verificar
git --version
```

---

## Fase 2: Autenticación GitHub 🔐

### Opción A: Token Personal (RECOMENDADO)

```bash
# 1. Ve a GitHub → Settings → Developer settings → Personal access tokens
# 2. Genera un nuevo token con:
#    - repo (acceso completo)
#    - workflow (opcional)
# 3. Cópialo

# En Termux:
git config --global credential.helper store

# Esto guardará tus credenciales localmente
```

### Opción B: SSH (MÁS SEGURO)

```bash
# Generar clave SSH
ssh-keygen -t ed25519 -C "tu@email.com"
# Presiona Enter 3 veces (sin contraseña para automatizar)

# Copiar clave pública
cat ~/.ssh/id_ed25519.pub

# 1. Ve a GitHub → Settings → SSH and GPG keys
# 2. Haz clic en "New SSH key"
# 3. Pega tu clave pública
# 4. Guarda

# Probar conexión
ssh -T git@github.com
# Debería decir: "Hi USERNAME! You've successfully authenticated..."
```

**Mi recomendación: Usa SSH (más seguro, no expone token)**

---

## Fase 3: Clonar Repositorio 📥

```bash
# 1. Crear carpeta para proyectos
mkdir -p ~/projects
cd ~/projects

# 2. Clonar tu repositorio (USA SSH)
git clone git@github.com:xdsdsdsdx/Android-Optimizer-Suite.git

# O si prefieres HTTPS:
git clone https://github.com/xdsdsdsdx/Android-Optimizer-Suite.git

# 3. Entrar a la carpeta
cd Android-Optimizer-Suite

# 4. Ver qué hay
ls -la
```

---

## Fase 4: Setup de Dependencias 📦

```bash
# 1. Instalar Python
pkg install -y python3 python3-pip

# 2. Instalar dependencias
pip install -r requirements.txt
# O manualmente:
pip install kivy requests

# 3. Verificar
python3 -c "import kivy; print(kivy.__version__)"
```

---

## Fase 5: Probar en Termux 🎮

```bash
# 1. Ejecutar la app
cd ~/projects/Android-Optimizer-Suite
python3 main.py

# Si funciona: ¡Excelente!
# Si falla: Ver logs para debugging

# Para ver más detalles:
python3 main.py 2>&1 | tee debug.log
```

---

## Fase 6: Compilar APK Personal 📱

### Opción A: DESDE TU PC (RECOMENDADO - Rápido)

```bash
# En tu Windows PC:

# 1. Instalar herramientas
pip install buildozer cython

# 2. Clonar en PC (opcional si ya tienes)
git clone https://github.com/xdsdsdsdx/Android-Optimizer-Suite.git
cd Android-Optimizer-Suite

# 3. Compilar
buildozer android debug

# 4. El APK está aquí:
# bin/Android-Optimizer-Suite-debug.apk
# o similar según buildozer.spec
```

### Opción B: DESDE TERMUX (Lento - 2-3 horas)

```bash
# En Termux (mucho más lento):

# 1. Instalar herramientas (esto tarda)
pip install buildozer cython

# 2. Compilar (prepárate: ~2 horas)
cd ~/projects/Android-Optimizer-Suite
buildozer android debug

# 3. Esperar... ☕️☕️☕️
```

---

## Fase 7: Firmar APK para Uso Personal 🔒

Si quieres que sea personal (no distribuible):

```bash
# En PC:

# 1. Crear keystore personal (una sola vez)
keytool -genkey -v -keystore my-key.keystore -keyalg RSA -keysize 2048 -validity 10000

# Te pedirá datos:
# Contraseña: pon algo seguro
# Nombre, organización, etc: lo que quieras

# 2. Firmar el APK
jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 \
  -keystore my-key.keystore \
  bin/Android-Optimizer-Suite-debug.apk my-key

# 3. Ya está firmado y listo
```

---

## Fase 8: Instalar en Tu Android 📲

```bash
# Opción A: Por USB (desde PC)

# 1. Conecta teléfono por USB
# 2. Activa "Depuración USB" en Configuración → Opciones de desarrollo

# En PC (PowerShell):
adb install "ruta\al\apk\Android-Optimizer-Suite-debug.apk"

# Opción B: Transferir manualmente

# 1. Copia el APK a una carpeta en tu teléfono
# 2. Abre con un gestor de archivos
# 3. Toca el APK para instalar
```

---

## 🔄 Flujo Completo (Recomendado)

```
TERMUX:
  ✅ 1. pkg install git
  ✅ 2. git clone repo
  ✅ 3. pip install deps
  ✅ 4. python3 main.py (test)
  
PC:
  ✅ 5. buildozer android debug
  ✅ 6. Firmar APK (opcional)
  
ANDROID:
  ✅ 7. adb install APK
  ✅ 8. Usar app
```

**Tiempo total:**
- Termux setup: 10 min
- PC compilación: 30-60 min
- Instalación: 5 min
- **Total: ~1 hora**

---

## 🐛 Troubleshooting

### ❌ "fatal: not a git repository"
```bash
cd ~/projects/Android-Optimizer-Suite
```

### ❌ "ModuleNotFoundError: No module named 'kivy'"
```bash
pip install kivy
# Si falla, instala dependencias del sistema primero:
pkg install -y libffi libssl-dev build-essential
pip install kivy
```

### ❌ "ImportError: No module named 'buildozer'"
```bash
pip install buildozer cython
```

### ❌ "Permission denied" al instalar APK
```bash
# En Android: Settings → Apps → Unknown sources (activar)
# O usar: adb install -r (reinstalar)
adb install -r bin/Android-Optimizer-Suite-debug.apk
```

### ❌ "Java not found" (compilación en PC)
```bash
# Instalar Java JDK 11+:
# https://www.oracle.com/java/technologies/downloads/
# Verificar:
java -version
```

---

## 💾 Mantener tu Repositorio Sincronizado

```bash
# En Termux o PC, dentro de la carpeta:

# Ver cambios
git status

# Actualizar desde GitHub
git pull

# Hacer cambios y guardar
git add .
git commit -m "Mi cambio"
git push
```

---

## 🔐 Seguridad: Proteger tus Credenciales

```bash
# NUNCA hacer commit de:
# - Archivos con tokens
# - Claves SSH
# - Contraseñas

# En .gitignore agregar:
echo "*.keystore" >> .gitignore
echo ".env" >> .gitignore
echo "credentials" >> .gitignore

git add .gitignore
git commit -m "Add gitignore"
```

---

## 📱 Usar tu App Personal en Android

Una vez instalada:

1. Abre "Suite Optimización" en tu launcher
2. Copia tu carpeta `marcas/` a: `/storage/emulated/0/SuiteOptimizacion/marcas/`
3. ¡Disfruta!

Para actualizaciones futuras:
- Modifica código en Termux o PC
- `git push` a GitHub
- Recompila cuando sea necesario
- Reinstala APK

---

## 🎁 Bonus: Automatizar Compilación

En PC, crear archivo `build.bat`:

```batch
@echo off
pip install buildozer cython
buildozer android clean
buildozer android debug
echo APK generado en: bin/Android-Optimizer-Suite-debug.apk
pause
```

Luego solo haz doble clic en `build.bat` para compilar.

---

**¿Preguntas? Revisa:**
- QUICK_START.md
- ANDROID_SETUP.md
- README.md

**¡Listo para comenzar! 🚀**
