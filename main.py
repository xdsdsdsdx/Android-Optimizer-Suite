import streamlit as st
import psutil
import shutil
import os

# Configuración de la App móvil
st.set_page_config(page_title="Android Optimizer", page_icon="📱")

st.title("📱 Android Optimizer Suite")
st.markdown("---")

st.header("📊 Estado del Sistema Real")

# 1. MODIFICACIÓN INTEGRADA: Ruta del almacenamiento real de Android
ruta_celular = "/storage/emulated/0"
total, used, free = shutil.disk_usage(ruta_celular)
porcentaje_disco = (used / total) * 100

# 2. Cálculo de Memoria RAM
ram = psutil.virtual_memory()

# --- INTERFAZ GRÁFICA ---

# Sección de Almacenamiento
st.subheader("💾 Almacenamiento Interno del Teléfono")
st.progress(int(porcentaje_disco))
st.write(f"**Usado:** {used / (1024**3):.2f} GB de {total / (1024**3):.2f} GB ({porcentaje_disco:.1f}%)")
st.write(f"**Espacio Libre:** {free / (1024**3):.2f} GB")

st.markdown("---")

# Sección de Memoria RAM
st.subheader("🧠 Memoria RAM")
st.progress(int(ram.percent))
st.write(f"**En uso:** {ram.used / (1024**2):.0f} MB / **Total:** {ram.total / (1024**2):.0f} MB ({ram.percent}%)")

st.markdown("---")

# 3. FUNCIÓN DE OPTIMIZACIÓN REAL
if st.button("🚀 Ejecutar Optimización"):
    # Ruta típica de descargas para buscar basura pesada
    ruta_descargas = "/storage/emulated/0/Download"
    espacio_liberado = 0
    archivos_eliminados = 0
    
    if os.path.exists(ruta_descargas):
        for carpeta_raiz, subcarpetas, archivos in os.walk(ruta_descargas):
            for archivo in archivos:
                # Detectar archivos basura comunes o instaladores APK pesados
                if archivo.endswith(('.apk', '.tmp', '.log', '.temp')):
                    ruta_completa = os.path.join(carpeta_raiz, archivo)
                    try:
                        tamano = os.path.getsize(ruta_completa)
                        os.remove(ruta_completa)  # Borrado físico real
                        espacio_liberado += tamano
                        archivos_eliminados += 1
                    except Exception:
                        continue

    # Efecto de celebración si todo sale bien
    st.balloons()
    
    if archivos_eliminados > 0:
        megabytes_liberados = espacio_liberado / (1024**2)
        st.success(f"¡Optimización completada con éxito! Se eliminaron {archivos_eliminados} archivos basura, liberando {megabytes_liberados:.2f} MB en tu carpeta de Descargas.")
    else:
        st.success("¡Tu sistema ya estaba optimizado! No se encontraron archivos temporales o instaladores APK obsoletos.")


