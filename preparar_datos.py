import pandas as pd
from funciones_limpieza import extraer_edad, quitar_angustia_si_hay_otras

def preparar_datos(df):
    # Extraer edad numérica
    df['Edad_num'] = df['Edad'].apply(extraer_edad)
    
    # Definir bins y etiquetas
    bins = [0, 5, 11, 17, 49, float('inf')]
    labels = ['0-5', '6-11', '12-17', '18-49', '50+']
    df['rango_edad'] = pd.cut(df['Edad_num'], bins=bins, labels=labels, right=True, include_lowest=True)

    # Reemplazar texto específico
    df['Lo que motiva la derivación es:'] = df['Lo que motiva la derivación es:'].str.replace(
        'Empeoramiento de un problema crónico. Violencia. Amenaza con tijeras.',
        'Empeoramiento de un problema crónico',
        regex=False
    )

    # Crear columnas de tiempo
    df['mes'] = df['Marca temporal'].dt.to_period('M')
    df['semana'] = df['Marca temporal'].dt.to_period('W')

    # Aplicar función para ajustar palabras clave
    df['palabras clave'] = df['palabras clave'].apply(quitar_angustia_si_hay_otras)

    # Cantidad de palabras clave
    df['cantidad_palabras_clave'] = df['palabras clave'].apply(lambda x: len(x.split('/')) if pd.notnull(x) else 0)

    return df
