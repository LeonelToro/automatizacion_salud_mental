import re
from rapidfuzz import fuzz
from normalizacion import normalizar

def asignar_categorias(motivo, diccionario_palabras_norm, umbral=85):
    motivo_norm = normalizar(motivo)
    categorias = []

    for categoria, variantes in diccionario_palabras_norm.items():
        for variante in variantes:
            variante_norm = normalizar(variante)

            # Match exacto
            if re.search(rf'\b{re.escape(variante_norm)}\b', motivo_norm):
                categorias.append(categoria)
                break
            else:
                # Fuzzy match palabra por palabra
                for palabra_motivo in motivo_norm.split():
                    similitud = fuzz.ratio(variante_norm, palabra_motivo)
                    if similitud >= umbral:
                        categorias.append(categoria)
                        break
                else:
                    continue
                break

    return "/".join(sorted(set(categorias))) if categorias else None