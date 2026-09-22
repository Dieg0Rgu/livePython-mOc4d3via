import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Gestión de ventas", page_icon = "🛒")
st.title("Sistema gestión de ventas")

ARCHIVO_EXCEL = "base_datos_ventas.xlsx"
COLUMNAS = ["ID", "PRODUCTO", "CANTIDAD", "PRECIO", "TOTAL"]

def inicializar_excel():
    if not os.path.exists(ARCHIVO_EXCEL):
        df = pd.DataFrame(columns=COLUMNAS)
        df.to_excel(ARCHIVO_EXCEL, index=False)

def cargar_datos():
    return pd.read_excel(ARCHIVO_EXCEL)


def guardar_datos(df):
    df.to_excel(ARCHIVO_EXCEL, index = False)

inicializar_excel()

tab1, tab2, tab3, tab4 = st.tabs(["Registrar", "Ver", "Actualizar", "Eliminar"])

with tab1:
    st.header("Nueva venta")

    with st.form("form_registro"):
        producto = st.text_input("Producto")
        cantidad = st.number_input("Cantidad", min_value=0.0, step = 0.5)
        precio = st.number_input("Precio", min_value=0)
        btn_registrar = st.form_submit_button("Registrar Venta")

        if btn_registrar and producto:
            df = cargar_datos()

            nuevo_id = 1 if df.empty else df["ID"].max() + 1

            nueva_venta = pd.DataFrame([{
                "ID" : nuevo_id,
                "PRODUCTO" : producto,
                "CANTIDAD" : cantidad,
                "PRECIO" : precio,
                "TOTAL" : cantidad * precio
            }])

            df = pd.concat([df, nueva_venta], ignore_index=True)
            guardar_datos(df)

            st.success(f"Venta registrada con éxito")

with tab2:
    st.header("Registro de ventas")
    df = cargar_datos()


    