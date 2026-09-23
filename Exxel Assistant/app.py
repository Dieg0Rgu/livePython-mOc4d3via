import streamlit as st
import pandas as pd
import re
from rapidfuzz import fuzz

st.set_page_config(page_title="Excel Claudio")
st.title("Chatea con tus Datos(No Internet)")

@st.cache_data
def cargar_datos():
    return pd.DataFrame(
        {
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
    )
    
df = cargar_datos