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
        precio = st.number_input("Precio", min_value=0.0, step=0.5, format="%.2f")
        btn_registrar = st.form_submit_button("Registrar Venta")

        if btn_registrar:
            if not producto.strip():
                # QA: antes el formulario se quedaba en silencio si el producto era vacío
                st.error("El nombre del producto no puede estar vacío")
            else:
                df = cargar_datos()

                nuevo_id = 1 if df.empty else int(df["ID"].max()) + 1

                nueva_venta = pd.DataFrame([{
                    "ID": nuevo_id,
                    "PRODUCTO": producto.strip(),
                    "CANTIDAD": cantidad,
                    "PRECIO": precio,
                    "TOTAL": cantidad * precio
                }])

                df = pd.concat([df, nueva_venta], ignore_index=True)
                guardar_datos(df)

                st.success(f"Venta registrada con éxito. ID de venta: {nuevo_id}")

with tab2:
    st.header("Registro de ventas")
    df = cargar_datos()

    if df.empty:
        st.info("No hay ventas registradas todavía")
    else:
        st.dataframe(df, hide_index=True)

        # Resumen tipo "mostrar_ventas" de main.py
        c1, c2, c3 = st.columns(3)
        c1.metric("Ventas registradas", len(df))
        c2.metric("Unidades vendidas", f"{df['CANTIDAD'].sum():g}")
        c3.metric("Ingresos totales", f"${df['TOTAL'].sum():,.2f}")

# ---------------- Tab 3: Actualizar ----------------
with tab3:
    st.header("Actualizar venta")

    df_act = cargar_datos()

    if df_act.empty:
        st.info("No hay ventas registradas todavía")
    else:
        with st.form("form_actualizar"):
            id_actualizar = st.number_input("ID de la venta a actualizar", min_value=1, step=1)
            producto_nuevo = st.text_input("Producto")
            cantidad_nueva = st.number_input("Cantidad nueva", min_value=0.0, step=0.5)
            precio_nuevo = st.number_input("Precio nuevo", min_value=0.0, step=0.5, format="%.2f")
            btn_actualizar = st.form_submit_button("Actualizar venta")

            if btn_actualizar:
                if not producto_nuevo.strip():
                    st.error("El nombre del producto no puede estar vacío")
                elif id_actualizar not in df_act["ID"].values:
                    # Equivalente al "No se encontró un producto con ese ID" de main.py
                    st.error(f"No se encontró una venta con el ID {int(id_actualizar)}")
                else:
                    fila = df_act["ID"] == id_actualizar
                    df_act.loc[fila, "PRODUCTO"] = producto_nuevo.strip()
                    df_act.loc[fila, "CANTIDAD"] = cantidad_nueva
                    df_act.loc[fila, "PRECIO"] = precio_nuevo
                    df_act.loc[fila, "TOTAL"] = cantidad_nueva * precio_nuevo
                    guardar_datos(df_act)
                    st.success(f"La venta {int(id_actualizar)} fue actualizada correctamente")

# ---------------- Tab 4: Eliminar ----------------
with tab4:
    st.header("Eliminar venta")

    df_elim = cargar_datos()

    if df_elim.empty:
        st.info("No hay ventas registradas todavía")
    else:
        with st.form("form_eliminar"):
            id_eliminar = st.selectbox(
                "Selecciona la venta a eliminar",
                options=df_elim["ID"].tolist(),
                format_func=lambda id_: (
                    f"ID {int(id_)} - "
                    f"{df_elim.loc[df_elim['ID'] == id_, 'PRODUCTO'].iloc[0]}"
                )
            )
            btn_eliminar = st.form_submit_button("Eliminar venta")

            if btn_eliminar:
                if id_eliminar not in df_elim["ID"].values:
                    st.error(f"No se encontró una venta con el ID {int(id_eliminar)}")
                else:
                    # Equivalente al filtrado de eliminar_venta() en main.py
                    df_elim = df_elim[df_elim["ID"] != id_eliminar]
                    guardar_datos(df_elim)
                    st.success(f"Venta {int(id_eliminar)} eliminada")
