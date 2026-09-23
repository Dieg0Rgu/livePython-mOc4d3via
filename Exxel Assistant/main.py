import pandas as pd
import re
from rapidfuzz import fuzz

datos = {
    "Productos": [
        "Laptop HP Pavilion",
        "Laptop Dell XPS",
        "Teclado Mecanico Razer",
        "Mouse Logitech",
        "Monitor LG 24",
        "Teclado de membrana"
    ],
    "Precios": [850, 1200, 120, 45, 200, 15]
}

df = pd.DataFrame(datos)


def asistente_excel(prompt, df_base):

    prompt = prompt.lower()

    orden_ascendente = True

    if re.search(r'\b(caro|caros|cara|mayor|mejor|mejores|mayores)\b', prompt):
        orden_ascendente = False

    palabras_a_borrar = r'\b(quiero|muestrame|un|una|unas|barato|baratos|caro|caras)\b'

    producto_buscado = re.sub(
        palabras_a_borrar,
        '',
        prompt
    ).strip()

    df_temp = df_base.copy()

    df_temp['Similitud'] = df_temp['Productos'].apply(
        lambda x: fuzz.WRatio(
            producto_buscado,
            str(x).lower()
        )
    )

    resultados = df_temp[
        df_temp['Similitud'] > 60
    ]

    resultados = resultados.sort_values(
        by="Precios",
        ascending=orden_ascendente
    )

    return resultados.drop(
        columns=['Similitud']
    )


while True:

    print("Hola, soy tu asistente, ¿en qué te puedo ayudar hoy?")

    entrada = input("-> ")

    if entrada.lower() == "salir":
        print("Hasta luego.")
        break

    resultado = asistente_excel(entrada, df)

    print(resultado)