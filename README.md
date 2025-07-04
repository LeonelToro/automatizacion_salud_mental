# Proyecto Automatizado de Análisis de Motivos de Derivación en Salud Mental

Este proyecto es una **solución completa y automatizada** desarrollada en **Python** para procesar, analizar y categorizar **motivos de derivación en salud mental** a partir de datos obtenidos de formularios. El objetivo es transformar **datos crudos** en **información útil y accionable**, facilitando la **gestión clínica** y la **toma de decisiones basadas en evidencia**.

Todo el flujo está estructurado como una **pipeline de análisis de datos**, que encadena módulos específicos para lectura, limpieza, categorización, visualización, exportación y envío de reportes. Esta organización permite que el proceso sea **repetible, eficiente y escalable**.

Además, el sistema automatiza la **generación de reportes** en múltiples formatos (**CSV, Excel, PDF, DOCX**), la **creación de visualizaciones claras y efectivas** para el análisis, y el **envío automático de estos informes por correo electrónico** a los stakeholders correspondientes, garantizando la **distribución eficiente y oportuna** de la información.

---

## Tecnologías y librerías utilizadas

El proyecto está construido principalmente con las siguientes librerías de Python:

- **pandas**: para manipulación y limpieza eficiente de datos tabulares.  
- **numpy**: para operaciones numéricas y soporte en análisis de datos.  
- **unicodedata y re**: para normalización y limpieza avanzada de textos.  
- **rapidfuzz**: para aplicar técnicas de comparación difusa (fuzzy matching) y detectar coincidencias aproximadas en texto. Esta técnica es clave para corregir posibles errores humanos en los formularios, que son obligatorios pero se completan bajo tiempos muy limitados por el personal.  
- **matplotlib y seaborn**: para la generación de gráficos y visualizaciones que facilitan la interpretación de resultados.  
- **os**: para manejo del sistema de archivos, rutas y gestión de directorios.  
- **datetime**: para el manejo preciso de fechas y tiempos, fundamental en la generación de archivos con marcas temporales.  
- **python-docx (Document)**: para la creación y manipulación de documentos Word (.docx) como parte de los reportes exportados.  
- **smtplib y email.message (EmailMessage)**: para automatizar el envío de correos electrónicos con los reportes generados.  

---

## Estructura y modulación del código

El código está modularizado en funciones y scripts que cumplen roles específicos y claros, facilitando la mantenibilidad y reutilización:

- **Lectura y preprocesamiento**: carga del dataset, limpieza de textos, normalización de datos.  
- **Categorización fuzzy con rapidfuzz**: aplicación de algoritmos de comparación difusa para asignar categorías a partir de variantes textuales, incluyendo la definición de umbrales y listas de términos clave para maximizar la precisión y mitigar errores de tipeo o variaciones en el lenguaje.  
- **Generación de métricas y visualizaciones**: cálculo de frecuencias, tendencias, y creación de gráficos descriptivos y visualizaciones claras para facilitar el análisis y la comunicación de resultados.  
- **Exportación, reporte y automatización**: creación de archivos CSV, Excel, PDF y Word con fechas actualizadas, y envío automático por mail para distribución inmediata a stakeholders.  

---

## Proceso automatizado y repetible

El flujo de trabajo está diseñado para ser completamente automatizado y programable, lo que permite:

- Ejecutar el análisis con un solo comando o script principal (`main.py`).  
- Generar reportes con marcas temporales, manteniendo un histórico ordenado.  
- Crear visualizaciones informativas y listas para presentar en informes.  
- Adaptar fácilmente a nuevos datasets sin modificar el código base, solo actualizando archivos de entrada.  
- Integrar con sistemas externos mediante envío automático de informes por correo.  

Este enfoque garantiza eficiencia, reducción de errores manuales y escalabilidad para futuras mejoras o ampliaciones.

---

---

## Contenido del repositorio

| Archivo | Descripción breve |
|---------|-------------------|
| [`categorias.py`](./categorias.py) | Define y organiza las categorías relevantes para el análisis de motivos. |
| [`configuracion.py`](./configuracion.py) | Contiene parámetros globales, paths y constantes utilizadas en todo el proyecto. |
| [`diccionario.py`](./diccionario.py) | Diccionario de términos clave asociados a cada categoría para el fuzzy matching. |
| [`enviar_mail.py`](./enviar_mail.py) | Script para configurar y enviar automáticamente los correos con los reportes. |
| [`funciones_limpieza.py`](./funciones_limpieza.py) | Funciones reutilizables para normalización y limpieza de texto. |
| [`graficos.py`](./graficos.py) | Generación de visualizaciones a partir de las métricas procesadas. |
| [`informe_pdf.py`](./informe_pdf.py) | Exportación del informe en formato PDF, incluyendo visualizaciones y tablas. |
| [`normalizacion.py`](./normalizacion.py) | Procesos para homogeneizar los textos del motivo de derivación. |
| [`pipe_con_pdf_gh.py`](./pipe_con_pdf_gh.py) | Script que ejecuta todo el pipeline completo e incluye la exportación a PDF. |
| [`pipeline_gh.py`](./pipeline_gh.py) | Pipeline principal del proyecto (sin PDF), orientado a la ejecución modular. |
| [`preparar_datos.py`](./preparar_datos.py) | Funciones para carga, filtrado y transformación inicial de los datos. |
| [`resumen.py`](./resumen.py) | Cálculo de métricas agregadas y preparación del contenido resumen del informe. |
| [`datos_ejemplo.csv`](./datos_ejemplo.csv) | Dataset de ejemplo simulado (sin datos sensibles), utilizado para pruebas. |
| [`grafico_pedidos_por_mes_2025_06_25.png`](./grafico_pedidos_por_mes_2025_06_25.png) | Visualización de la cantidad de derivaciones por mes. |
| [`top10_motivos_2025_06_25.png`](./top10_motivos_2025_06_25.png) | Gráfico con los 10 motivos de derivación más frecuentes. |

---

## 📊 Visualizaciones de ejemplo generadas por el pipeline


### Top 10 motivos de derivación

![Top 10 motivos de derivación](./top10_motivos_2025-06-25.png)

### Derivaciones por mes

![Gráfico de pedidos por mes](./grafico_pedidos_por_mes_2025-06-25.png)


# Automated Pipeline for Analyzing Mental Health Referral Reasons

This project is a **fully automated solution** developed in **Python** to process, analyze, and categorize **mental health referral reasons** based on data collected from forms. Its goal is to transform **raw data** into **useful and actionable information**, supporting **clinical management** and **evidence-based decision making**.

The entire workflow is structured as a **data analysis pipeline**, linking dedicated modules for reading, cleaning, categorization, visualization, exporting, and reporting. This architecture ensures the process is **repeatable, efficient, and scalable**.

Additionally, the system automates the **generation of reports** in multiple formats (**CSV, Excel, PDF, DOCX**), the **creation of clear and effective visualizations** for analysis, and the **automatic email delivery** of these reports to the relevant stakeholders, ensuring **timely and efficient information distribution**.

---

## Technologies and Libraries Used

The project is built primarily with the following Python libraries:

- **pandas**: for efficient tabular data manipulation and cleaning.  
- **numpy**: for numerical operations and data analysis support.  
- **unicodedata and re**: for advanced text normalization and cleaning.  
- **rapidfuzz**: for implementing fuzzy matching techniques to detect approximate text matches. This is key for handling possible human input errors in required forms often filled under tight time constraints.  
- **matplotlib and seaborn**: for generating charts and visualizations that enhance result interpretation.  
- **os**: for file system operations, path handling, and directory management.  
- **datetime**: for accurate date and time handling, essential for timestamped file generation.  
- **python-docx (Document)**: for creating and modifying Word documents (.docx) as part of the exported reports.  
- **smtplib and email.message (EmailMessage)**: for automating the sending of generated reports via email.  

---

## Code Structure and Modularity

The code is modularized into functions and scripts with clear, specific roles, improving maintainability and reusability:

- **Reading and preprocessing**: loading datasets, cleaning text, and data normalization.  
- **Fuzzy categorization using rapidfuzz**: applying fuzzy matching algorithms to assign categories based on textual variations, with configurable thresholds and keyword lists to enhance accuracy and reduce typos or language variation issues.  
- **Metrics and visualization generation**: computing frequencies and trends, and generating descriptive charts to facilitate analysis and communication of results.  
- **Export, reporting, and automation**: generating timestamped CSV, Excel, PDF, and Word files, and automatically sending them via email for immediate distribution to stakeholders.  

---

## Automated and Repeatable Process

The workflow is designed to be fully automated and schedulable, allowing for:

- Running the entire analysis with a single command or main script (`main.py`).  
- Generating timestamped reports and maintaining a clean historical log.  
- Producing informative visualizations ready for reporting.  
- Easily adapting to new datasets by updating only the input files.  
- Integration with external systems through automated email delivery.  

This approach ensures efficiency, reduces manual errors, and provides scalability for future improvements.

---

## Repository Contents

| File | Brief Description |
|---------|-------------------|
| [`categorias.py`](./categorias.py) | Defines and organizes relevant categories for referral analysis. |
| [`configuracion.py`](./configuracion.py) | Contains global parameters, paths, and constants used throughout the project. |
| [`diccionario.py`](./diccionario.py) | Keyword dictionary associated with each category for fuzzy matching. |
| [`enviar_mail.py`](./enviar_mail.py) | Script to configure and automatically send emails with the generated reports. |
| [`funciones_limpieza.py`](./funciones_limpieza.py) | Reusable functions for text normalization and cleaning. |
| [`graficos.py`](./graficos.py) | Generates visualizations from processed metrics. |
| [`informe_pdf.py`](./informe_pdf.py) | Exports the report in PDF format, including visualizations and tables. |
| [`normalizacion.py`](./normalizacion.py) | Processes to standardize referral reason texts. |
| [`pipe_con_pdf_gh.py`](./pipe_con_pdf_gh.py) | Script that runs the full pipeline including PDF export. |
| [`pipeline_gh.py`](./pipeline_gh.py) | Main pipeline script (without PDF), designed for modular execution. |
| [`preparar_datos.py`](./preparar_datos.py) | Functions for loading, filtering, and initial data transformation. |
| [`resumen.py`](./resumen.py) | Calculates aggregated metrics and prepares summary report content. |
| [`datos_ejemplo.csv`](./datos_ejemplo.csv) | Simulated example dataset (no sensitive data), used for testing. |
| [`grafico_pedidos_por_mes_2025_06_25.png`](./grafico_pedidos_por_mes_2025_06_25.png) | Visualization of referral requests per month. |
| [`top10_motivos_2025_06_25.png`](./top10_motivos_2025_06_25.png) | Chart showing the top 10 most frequent referral reasons. |

---

## 📊 Example Visualizations Generated by the Pipeline

### Top 10 Referral Reasons

![Top 10 Referral Reasons](./top10_motivos_2025-06-25.png)

