import pandas as pd
import re
from rapidfuzz import fuzz

datos = {
    "Productos": ["Laptop HP Pavilion", "Laptop Dell XPS",
                   "Teclado Mecanico Razer", "Mouse Logitech", "Monitor LG 24",
                   "Teclado de membrana"],
    "Precios": [850, 1200, 120, 45, 200,15]              
}

df = pd.DataFrame(datos)

def asistente_excel(prompt, df_base):
    prompt = prompt.lower()

    orden_ascendente = True

    if re.search(r'\b(caro|caros|cara|mayor|mejor|mejores|mayores)\b', prompt):
        orden_ascendente = False

    palabras_a_borrar = r'\b(quiero|muestrame|un|una|unas|barato|baratos|caro|caras)\b'
    producto_buscado = re.sub(palabras_a_borrar, '', prompt).strip()

    