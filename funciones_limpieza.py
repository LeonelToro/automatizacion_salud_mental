import re
import pandas as pd

def extraer_edad(valor):
    if isinstance(valor, str):
        match = re.search(r'\d+', valor)
        if match:
            return int(match.group())
    elif isinstance(valor, (int, float)):
        return int(valor)
    return None

def quitar_angustia_si_hay_otras(palabras):
    if pd.isnull(palabras):
        return palabras
    claves = [k.strip() for k in palabras.split('/')]
    if 'angustia' in claves and len(claves) > 1:
        claves = [k for k in claves if k != 'angustia']
    return '/'.join(claves) if claves else None
