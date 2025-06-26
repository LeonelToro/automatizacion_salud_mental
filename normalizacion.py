import pandas as pd
import unicodedata

def normalizar(texto):
    if pd.isnull(texto):
        return ""
    texto = str(texto).lower()
    return unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('utf-8')

def normalizar_diccionario(diccionario):
    return {
        categoria: [normalizar(v) for v in variantes]
        for categoria, variantes in diccionario.items()
    }
