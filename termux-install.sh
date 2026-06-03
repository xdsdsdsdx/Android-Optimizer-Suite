#!/bin/bash

# Script de instalación para Termux
# Ejecutar con: bash termux-install.sh

echo "================================"
echo "Suite Optimización - Termux Setup"
echo "================================"
echo ""

# Actualizar paquetes
echo "[1/5] Actualizando paquetes de Termux..."
pkg update -y
pkg upgrade -y

# Instalar Python y dependencias
echo "[2/5] Instalando Python 3 y pip..."
pkg install -y python3 python3-pip

# Instalar dependencias de Kivy (específicas para Termux)
echo "[3/5] Instalando dependencias del sistema..."
pkg install -y libffi libssl-dev build-essential

# Instalar paquetes Python
echo "[4/5] Instalando paquetes Python..."
pip install --upgrade pip setuptools wheel
pip install kivy requests

# Crear estructura de directorios
echo "[5/5] Configurando directorios..."
mkdir -p ~/SuiteOptimizacion/marcas
cd ~/SuiteOptimizacion

# Descargar archivo main.py
echo ""
echo "✓ Instalación completada!"
echo ""
echo "Próximos pasos:"
echo "1. Descarga main.py a: ~/SuiteOptimizacion/"
echo "2. Copia tus carpetas de 'marcas' a: ~/SuiteOptimizacion/marcas/"
echo "3. Ejecuta: python3 main.py"
echo ""
echo "Nota: En Termux, la GUI se abrirá en modo gráfico."
echo "Si necesitas modo headless, usa: python3 main.py --headless"
