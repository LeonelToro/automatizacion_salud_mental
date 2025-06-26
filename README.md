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
|--------|--------------------|
| [`1- categorias.py`](./1-%20categorias.py) | Define y organiza las categorías relevantes para el análisis de motivos. |
| [`2- configuración.py`](./2-%20configuración.py) | Contiene parámetros globales, paths y constantes utilizadas en todo el proyecto. |
| [`3- diccionario.py`](./3-%20diccionario.py) | Diccionario de términos clave asociados a cada categoría para el fuzzy matching. |
| [`4- enviar_mail.py`](./4-%20enviar_mail.py) | Script para configurar y enviar automáticamente los correos con los reportes. |
| [`5- funciones_limpieza.py`](./5-%20funciones_limpieza.py) | Funciones reutilizables para normalización y limpieza de texto. |
| [`6- graficos.py`](./6-%20graficos.py) | Generación de visualizaciones a partir de las métricas procesadas. |
| [`7- informe_pdf.py`](./7-%20informe_pdf.py) | Exportación del informe en formato PDF, incluyendo visualizaciones y tablas. |
| [`8- normalizacion.py`](./8-%20normalizacion.py) | Procesos para homogeneizar los textos del motivo de derivación. |
| [`9- pipe con pdf gh.py`](./9-%20pipe%20con%20pdf%20gh.py) | Script que ejecuta todo el pipeline completo e incluye la exportación a PDF. |
| [`10- Pipeline gh.py`](./10-%20Pipeline%20gh.py) | Pipeline principal del proyecto (sin PDF), orientado a la ejecución modular. |
| [`11- preparar_datos.py`](./11-%20preparar_datos.py) | Funciones para carga, filtrado y transformación inicial de los datos. |
| [`12- resumen.py`](./12-%20resumen.py) | Cálculo de métricas agregadas y preparación del contenido resumen del informe. |
| [`13- datos_ejemplo.csv`](./13-%20datos_ejemplo.csv) | Dataset de ejemplo simulado (sin datos sensibles), utilizado para pruebas. |
| [`14- grafico_pedidos_por_mes_2025-06-25.png`](./14-%20grafico_pedidos_por_mes_2025-06-25.png) | Visualización de la cantidad de derivaciones por mes. |
| [`15- top10_motivos_2025-06-25.png`](./15-%20top10_motivos_2025-06-25.png) | Gráfico con los 10 motivos de derivación más frecuentes. |

---

## 📊 Visualizaciones de ejemplo generadas por el pipeline


### Top 10 motivos de derivación

![Top 10 motivos de derivación](./15-%20top10_motivos_2025-06-25.png)

### Derivaciones por mes

![Gráfico de pedidos por mes](./14-%20grafico_pedidos_por_mes_2025-06-25.png)


