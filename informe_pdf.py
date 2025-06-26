import os
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from PIL import Image

def generar_informe_pdf(df, diccionario_palabras, output_dir, fecha_hoy):
    pdf_path = os.path.join(output_dir, f"informe_salud_mental_{fecha_hoy}.pdf")

    with PdfPages(pdf_path) as pdf:
        # Página 1: Texto resumen simple
        fig, ax = plt.subplots(figsize=(8.5, 11))
        ax.axis('off')

        texto_resumen = (
            f"Informe Salud Mental - {fecha_hoy}\n\n"
            f"Cantidad total de registros analizados: {len(df)}\n"
            f"Cantidad de registros sin palabras clave: {df['palabras clave'].isna().sum()}\n"
            f"Cantidad promedio de palabras clave por registro: {df['cantidad_palabras_clave'].mean():.2f}\n"
            f"Cantidad total de categorías definidas: {len(diccionario_palabras)}\n\n"
            f"Listado de categorías y variantes:\n"
        )
        for clave, variantes in diccionario_palabras.items():
            texto_resumen += f"- {clave}: {', '.join(variantes)}\n"

        plt.text(0, 1, texto_resumen, verticalalignment='top', fontsize=10, family='monospace')
        pdf.savefig(fig)
        plt.close()

        # Agregar imágenes como páginas siguientes
        for filename in sorted(os.listdir(output_dir)):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                filepath = os.path.join(output_dir, filename)
                img = Image.open(filepath)
                # Crear figura con el tamaño de la imagen para que no distorsione
                fig, ax = plt.subplots(figsize=(img.width / 100, img.height / 100), dpi=100)
                ax.imshow(img)
                ax.axis('off')
                pdf.savefig(fig, bbox_inches='tight')
                plt.close(fig)

    print(f"Informe PDF guardado en: {pdf_path}")
