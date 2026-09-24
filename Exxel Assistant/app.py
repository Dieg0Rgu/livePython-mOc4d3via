import streamlit as st
import pandas as pd
import re
from rapidfuzz import fuzz


# ==========================================
# CONFIGURACIÓN
# ==========================================

st.set_page_config(page_title="Excel Claudio")
st.title("Chatea con tus Datos (No Internet)")


# ==========================================
# CARGAR DATOS
# ==========================================

@st.cache_data
def cargar_datos():
    return pd.DataFrame(
        {
            "Productos": [
                # =========================
                # LAPTOPS
                # =========================
                "Laptop HP Pavilion",
                "Laptop Dell XPS",
                "Laptop Lenovo ThinkPad",
                "Laptop ASUS VivoBook",
                "Laptop Acer Aspire 5",
                "Laptop Lenovo IdeaPad 3",
                "Laptop HP Envy",
                "Laptop Dell Inspiron",
                "Laptop ASUS TUF Gaming",
                "Laptop MSI Modern 14",
                "Laptop Acer Nitro 5",
                "Laptop Lenovo Legion 5",

                # =========================
                # TECLADOS
                # =========================
                "Teclado Mecanico Razer",
                "Teclado de membrana",
                "Teclado Mecanico Logitech",
                "Teclado Mecanico Corsair",
                "Teclado Mecanico Redragon",
                "Teclado Inalambrico Logitech",
                "Teclado Inalambrico Microsoft",
                "Teclado Gaming HyperX",
                "Teclado Gaming ASUS",
                "Teclado Ergonomico Microsoft",
                "Teclado Compacto Keychron",
                "Teclado RGB Redragon",

                # =========================
                # MOUSE
                # =========================
                "Mouse Logitech",
                "Mouse Logitech MX Master 3",
                "Mouse Logitech G502",
                "Mouse Razer DeathAdder",
                "Mouse Razer Basilisk",
                "Mouse Corsair Harpoon",
                "Mouse Redragon Gaming",
                "Mouse HyperX Pulsefire",
                "Mouse Microsoft Bluetooth",
                "Mouse ASUS TUF Gaming",
                "Mouse SteelSeries Rival 3",
                "Mouse Inalambrico HP",

                # =========================
                # MONITORES
                # =========================
                "Monitor LG 24",
                "Monitor Samsung 24",
                "Monitor ASUS 27",
                "Monitor Acer 24",
                "Monitor Dell 27",
                "Monitor Lenovo 24",
                "Monitor LG UltraWide 29",
                "Monitor Samsung Odyssey 27",
                "Monitor ASUS TUF Gaming 27",
                "Monitor AOC Gaming 24",
                "Monitor MSI Optix 27",
                "Monitor ViewSonic 24",

                # =========================
                # AUDIFONOS
                # =========================
                "Audifonos Logitech",
                "Audifonos Razer Kraken",
                "Audifonos HyperX Cloud",
                "Audifonos Corsair HS55",
                "Audifonos Sony WH-1000XM5",
                "Audifonos JBL Tune",
                "Audifonos ASUS Gaming",
                "Audifonos SteelSeries Arctis",
                "Audifonos Xiaomi Redmi Buds",
                "Audifonos Samsung Galaxy Buds",

                # =========================
                # WEBCAMS
                # =========================
                "Webcam Logitech C270",
                "Webcam Logitech C920",
                "Webcam Logitech Brio",
                "Webcam Razer Kiyo",
                "Webcam Microsoft LifeCam",
                "Webcam HP HD 4310",
                "Webcam ASUS Full HD",
                "Webcam Anker PowerConf",
                "Webcam Creative Live Cam",
                "Webcam NexiGo Full HD",

                # =========================
                # MICROFONOS
                # =========================
                "Microfono HyperX QuadCast",
                "Microfono Blue Yeti",
                "Microfono Razer Seiren",
                "Microfono Fifine USB",
                "Microfono Logitech Blue Snowball",
                "Microfono Corsair Elgato Wave",
                "Microfono Rode NT USB",
                "Microfono Audio Technica AT2020",
                "Microfono Maono USB",
                "Microfono Trust Gaming",

                # =========================
                # ALFOMBRILLAS
                # =========================
                "Alfombrilla Logitech",
                "Alfombrilla Razer Gigantus",
                "Alfombrilla Corsair MM300",
                "Alfombrilla HyperX Fury",
                "Alfombrilla Redragon Gaming",
                "Alfombrilla SteelSeries QcK",
                "Alfombrilla ASUS TUF",
                "Alfombrilla RGB Gaming",
                "Alfombrilla XXL Gamer",
                "Alfombrilla Ergonomica",

                # =========================
                # PARLANTES
                # =========================
                "Parlantes Logitech Z120",
                "Parlantes Logitech Z623",
                "Parlantes Creative Pebble",
                "Parlantes Razer Nommo",
                "Parlantes JBL Gaming",
                "Parlantes Trust Gaming",
                "Parlantes Edifier R1280",
                "Parlantes Sony Bluetooth",
                "Parlantes Xiaomi",
                "Parlantes ASUS Gaming",

                # =========================
                # ALMACENAMIENTO
                # =========================
                "SSD Kingston 480GB",
                "SSD Kingston 1TB",
                "SSD Samsung 980 1TB",
                "SSD WD Blue 1TB",
                "SSD Crucial 500GB",
                "Disco Duro Seagate 1TB",
                "Disco Duro WD 2TB",
                "Disco Externo Toshiba 1TB",
                "Memoria USB Kingston 64GB",
                "Memoria USB SanDisk 128GB",

                # =========================
                # ACCESORIOS
                # =========================
                "Hub USB Anker",
                "Hub USB UGREEN",
                "Adaptador USB Bluetooth",
                "Adaptador USB WiFi",
                "Cable HDMI 2 Metros",
                "Cable HDMI 5 Metros",
                "Cable USB C",
                "Cargador USB C 65W",
                "Base Refrigerante Laptop",
                "Soporte para Monitor"
            ],

            "Precios": [
                # LAPTOPS
                850, 1200, 950, 700, 650, 580,
                1100, 750, 1300, 800, 1050, 1400,

                # TECLADOS
                120, 15, 100, 140, 70, 45,
                35, 80, 90, 65, 110, 75,

                # MOUSE
                45, 95, 110, 80, 90, 55,
                40, 65, 35, 60, 70, 30,

                # MONITORES
                200, 180, 300, 170, 350, 190,
                400, 450, 380, 220, 410, 210,

                # AUDIFONOS
                60, 100, 90, 75, 280, 80,
                95, 150, 55, 120,

                # WEBCAMS
                35, 90, 180, 100, 65, 50,
                75, 110, 60, 55,

                # MICROFONOS
                150, 130, 120, 60, 70, 140,
                180, 160, 65, 50,

                # ALFOMBRILLAS
                25, 35, 40, 30, 28, 32,
                30, 45, 50, 20,

                # PARLANTES
                30, 120, 45, 150, 100, 60,
                130, 90, 55, 110,

                # ALMACENAMIENTO
                45, 80, 90, 75, 50, 60,
                100, 65, 20, 25,

                # ACCESORIOS
                35, 30, 15, 20, 18, 25,
                12, 45, 35, 40
            ]
        }
    )


df = cargar_datos()


# ==========================================
# BUSCADOR
# ==========================================

def buscar_en_excel(prompt, df_base):

    prompt_min = prompt.lower().strip()

    # Detectar si el usuario quiere precios altos
    palabras_caros = r"\b(caro|caros|cara|caras|mayor|mayores|mejor|mejores)\b"

    orden_asc = not bool(
        re.search(palabras_caros, prompt_min)
    )

    # Palabras que no necesitamos para buscar
    basura = (
        r"\b(quiero|quieres|muestrame|muéstrame|mostrar|"
        r"dame|dame los|dime|un|una|unos|unas|"
        r"el|la|los|las|producto|productos|"
        r"barato|baratos|barata|baratas|"
        r"caro|caros|cara|caras|"
        r"mayor|mayores|mejor|mejores)\b"
    )

    producto_buscado = re.sub(
        basura,
        "",
        prompt_min
    ).strip()

    # Limpiar espacios dobles
    producto_buscado = re.sub(
        r"\s+",
        " ",
        producto_buscado
    )

    if not producto_buscado:
        return (
            None,
            "Por favor dime qué producto específico estás buscando."
        )

    # Copiar DataFrame
    df_temp = df_base.copy()

    # ==========================================
    # CALCULAR SIMILITUD
    # ==========================================

    df_temp["Similitud"] = df_temp["Productos"].apply(
        lambda producto: fuzz.partial_ratio(
            producto_buscado,
            producto.lower()
        )
    )

    # ==========================================
    # FILTRAR RESULTADOS
    # ==========================================

    resultados = df_temp[
        df_temp["Similitud"] >= 40
    ].copy()

    if resultados.empty:
        return (
            None,
            f"No encontré nada parecido a '{producto_buscado}' "
            "en la base de datos."
        )

    # ==========================================
    # ORDENAR POR SIMILITUD
    # ==========================================

    resultados = resultados.sort_values(
        by=["Similitud", "Precios"],
        ascending=[False, orden_asc]
    )

    # Mostrar solamente los mejores resultados
    resultados = resultados.head(10)

    # Eliminar columna auxiliar
    resultados = resultados.drop(
        columns=["Similitud"]
    )

    if orden_asc:
        mensaje = (
            f"Encontré resultados para **{producto_buscado}**. "
            "Los productos están ordenados de menor a mayor precio."
        )
    else:
        mensaje = (
            f"Encontré resultados para **{producto_buscado}**. "
            "Los productos están ordenados de mayor a menor precio."
        )

    return resultados, mensaje


# ==========================================
# HISTORIAL DEL CHAT
# ==========================================

if "mensajes" not in st.session_state:

    st.session_state.mensajes = [
        {
            "role": "assistant",
            "content": (
                "Hola, soy Sophia 👋\n\n"
                "Puedes preguntarme por productos, precios, "
                "laptops, teclados, mouse, monitores, etc."
            )
        }
    ]


# ==========================================
# MOSTRAR HISTORIAL
# ==========================================

for mensaje in st.session_state.mensajes:

    with st.chat_message(mensaje["role"]):

        st.markdown(
            mensaje["content"]
        )

        if "data" in mensaje:

            st.dataframe(
                mensaje["data"],
                use_container_width=True,
                hide_index=True
            )


# ==========================================
# INPUT DEL CHAT
# ==========================================

if prompt := st.chat_input(
    "Escribe tu búsqueda aquí..."
):

    # ======================================
    # MOSTRAR MENSAJE DEL USUARIO
    # ======================================

    with st.chat_message("user"):

        st.markdown(prompt)

    st.session_state.mensajes.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    # ======================================
    # BUSCAR
    # ======================================

    df_resultado, respuesta_texto = buscar_en_excel(
        prompt,
        df
    )

    # ======================================
    # MOSTRAR RESPUESTA
    # ======================================

    with st.chat_message("assistant"):

        st.markdown(
            respuesta_texto
        )

        if df_resultado is not None:

            st.dataframe(
                df_resultado,
                use_container_width=True,
                hide_index=True
            )

    # ======================================
    # GUARDAR RESPUESTA EN HISTORIAL
    # ======================================

    mensaje_asistente = {
        "role": "assistant",
        "content": respuesta_texto
    }

    if df_resultado is not None:

        mensaje_asistente["data"] = df_resultado

    st.session_state.mensajes.append(
        mensaje_asistente
    )