"""Aplicacion Streamlit para la Funcionalidad 1 del proyecto ROE DuPont."""

import streamlit as st


def safe_division(numerator: float, denominator: float) -> float:
    """Retorna numerator/denominator si es valido, en caso contrario 0."""
    if denominator == 0:
        return 0.0
    return numerator / denominator


st.set_page_config(
    page_title="Analisis Financiero con el Modelo Dupont",
    page_icon="📊",
    layout="wide",
)

st.title("Análisis Financiero con el Modelo Dupont")
st.markdown(
    "Captura variables contables clave y calcula automaticamente los componentes "
    "del modelo DuPont junto con el ROE."
)

st.sidebar.header("Variables de entrada")
st.sidebar.info("Ajusta los valores usando los sliders para calcular los ratios financieros")
utilidad_neta = st.sidebar.slider(
    "Utilidad Neta",
    min_value=-1_000_000.0,
    max_value=1_000_000.0,
    value=120_000.0,
    step=10_000.0,
    format="%.2f",
)
ventas = st.sidebar.slider(
    "Ventas",
    min_value=0.0,
    max_value=5_000_000.0,
    value=1_200_000.0,
    step=50_000.0,
    format="%.2f",
)
activos_promedio = st.sidebar.slider(
    "Activos Promedio",
    min_value=0.0,
    max_value=5_000_000.0,
    value=2_000_000.0,
    step=50_000.0,
    format="%.2f",
)
patrimonio_promedio = st.sidebar.slider(
    "Patrimonio Promedio",
    min_value=0.0,
    max_value=5_000_000.0,
    value=800_000.0,
    step=50_000.0,
    format="%.2f",
)

margen_neto = safe_division(utilidad_neta, ventas)
rotacion_activos = safe_division(ventas, activos_promedio)
apalancamiento_financiero = safe_division(activos_promedio, patrimonio_promedio)
roe = margen_neto * rotacion_activos * apalancamiento_financiero

if ventas == 0 or activos_promedio == 0 or patrimonio_promedio == 0:
    st.warning(
        "Hay una o mas variables en cero. Para evitar divisiones invalidas, "
        "el calculo usa 0 en los componentes afectados."
    )

st.subheader("Resultados DuPont")

metric_col_1, metric_col_2, metric_col_3, metric_col_4 = st.columns(4)

metric_col_1.metric("Margen Neto", f"{margen_neto:.2%}")
metric_col_2.metric("Rotacion de Activos", f"{rotacion_activos:.2f}x")
metric_col_3.metric("Apalancamiento Financiero", f"{apalancamiento_financiero:.2f}x")
metric_col_4.metric("ROE", f"{roe:.2%}")

st.markdown("### Formula aplicada")
st.latex(
    r"ROE = \left(\frac{Utilidad\ Neta}{Ventas}\right)"
    r"\times \left(\frac{Ventas}{Activos\ Promedio}\right)"
    r"\times \left(\frac{Activos\ Promedio}{Patrimonio\ Promedio}\right)"
)
