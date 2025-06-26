from datetime import datetime
import os

# Ruta del archivo original
RUTA_ARCHIVO_EXCEL = r"C:\Users\primo\Downloads\Pedido de atención SM - CeSAC 24 (respuestas).xlsx"
SHEET_NAME = "Respuestas de formulario 1"

# Ruta de salida
OUTPUT_DIR = r"C:\Users\primo\Desktop\Ciencia de Datos\Proyectos\Salud Mental\output"

# Fecha actual en formato YYYY-MM-DD
FECHA_HOY = datetime.now().strftime("%Y-%m-%d")

# Crear la carpeta de salida si no existe
os.makedirs(OUTPUT_DIR, exist_ok=True)