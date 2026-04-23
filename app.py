"""Aplicacion Streamlit para las funcionalidades 1, 2 y 3 de ROE DuPont."""

import plotly.graph_objects as go
import streamlit as st


def safe_division(numerator: float, denominator: float) -> float:
    """Retorna numerator/denominator si es valido, en caso contrario 0."""
    if denominator == 0:
        return 0.0
    return numerator / denominator


def build_dupont_prism(margen: float, rotacion: float, apalancamiento: float) -> go.Figure:
    """Construye un prisma 3D para visualizar la interaccion de factores DuPont."""
    x = max(margen, 0.0)
    y = max(rotacion, 0.0)
    z = max(apalancamiento, 0.0)

    vertices_x = [0, x, x, 0, 0, x, x, 0]
    vertices_y = [0, 0, y, y, 0, 0, y, y]
    vertices_z = [0, 0, 0, 0, z, z, z, z]

    fig = go.Figure()
    fig.add_trace(
        go.Mesh3d(
            x=vertices_x,
            y=vertices_y,
            z=vertices_z,
            i=[0, 0, 0, 1, 1, 2, 4, 4, 5, 6, 2, 3],
            j=[1, 2, 4, 2, 5, 3, 5, 6, 6, 7, 6, 7],
            k=[2, 3, 5, 3, 6, 7, 6, 7, 1, 5, 7, 4],
            opacity=0.45,
            color="#1f77b4",
            name="Prisma ROE",
            hovertemplate=(
                "Margen Neto: %{x:.2f}<br>"
                "Rotacion de Activos: %{y:.2f}<br>"
                "Apalancamiento Financiero: %{z:.2f}<extra></extra>"
            ),
        )
    )

    # Aristas para reforzar la lectura visual del prisma.
    edges = [
        (0, 1), (1, 2), (2, 3), (3, 0),
        (4, 5), (5, 6), (6, 7), (7, 4),
        (0, 4), (1, 5), (2, 6), (3, 7),
    ]
    for start, end in edges:
        fig.add_trace(
            go.Scatter3d(
                x=[vertices_x[start], vertices_x[end]],
                y=[vertices_y[start], vertices_y[end]],
                z=[vertices_z[start], vertices_z[end]],
                mode="lines",
                line=dict(color="#0b3d91", width=5),
                showlegend=False,
                hoverinfo="skip",
            )
        )

    fig.update_layout(
        title="Prisma 3D del Modelo DuPont",
        margin=dict(l=0, r=0, b=0, t=40),
        scene=dict(
            xaxis_title="Margen Neto",
            yaxis_title="Rotacion de Activos",
            zaxis_title="Apalancamiento Financiero",
            xaxis=dict(backgroundcolor="#f8fafc"),
            yaxis=dict(backgroundcolor="#f8fafc"),
            zaxis=dict(backgroundcolor="#f8fafc"),
            camera=dict(eye=dict(x=1.5, y=1.4, z=1.2)),
        ),
    )
    return fig


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

st.subheader("Visualizacion 3D del Prisma ROE")
st.markdown(
    "El prisma muestra como interactuan margen neto, rotacion de activos y "
    "apalancamiento financiero en la descomposicion del ROE."
)

if margen_neto < 0:
    st.info(
        "El margen neto es negativo. Para mantener una lectura geometrica clara, "
        "el prisma usa 0 en ese eje, pero el ROE mostrado conserva el calculo real."
    )

prisma_fig = build_dupont_prism(margen_neto, rotacion_activos, apalancamiento_financiero)
st.plotly_chart(prisma_fig, use_container_width=True)

st.subheader("Estados Financieros Simplificados")
st.markdown(
    "Se presentan un Estado de Resultados y un Balance General estimados a partir "
    "de las variables de entrada."
)

# Funcionalidad 3: Estado de Resultados con logica Ventas = Gastos + Utilidad Neta.
gastos_estimados = ventas - utilidad_neta

if gastos_estimados < 0:
    st.warning(
        "La utilidad neta supera a las ventas en el escenario actual. "
        "El valor de gastos se muestra negativo para mantener la identidad "
        "Ventas = Gastos + Utilidad Neta."
    )

estado_resultados_fig = go.Figure(
    go.Bar(
        x=[ventas, gastos_estimados, utilidad_neta],
        y=["Ventas", "Gastos", "Utilidad Neta"],
        orientation="h",
        marker_color=["#1f77b4", "#ff7f0e", "#2ca02c"],
        text=[f"${ventas:,.0f}", f"${gastos_estimados:,.0f}", f"${utilidad_neta:,.0f}"],
        textposition="auto",
    )
)
estado_resultados_fig.update_layout(
    title="Estado de Resultados Simplificado",
    xaxis_title="Monto",
    yaxis_title="Cuenta",
    template="plotly_white",
    height=360,
)

# Balance simplificado: Activos = Deuda + Patrimonio.
deuda_estimada = activos_promedio - patrimonio_promedio
if deuda_estimada < 0:
    st.warning(
        "El patrimonio promedio supera a los activos promedio en este escenario. "
        "La deuda estimada se muestra negativa para reflejar la identidad "
        "Activos = Deuda + Patrimonio."
    )

balance_general_fig = go.Figure()
balance_general_fig.add_trace(
    go.Bar(
        x=["Activos"],
        y=[activos_promedio],
        name="Activos",
        marker_color="#636efa",
        text=[f"${activos_promedio:,.0f}"],
        textposition="auto",
    )
)
balance_general_fig.add_trace(
    go.Bar(
        x=["Patrimonio + Deuda"],
        y=[patrimonio_promedio],
        name="Patrimonio",
        marker_color="#00cc96",
        text=[f"${patrimonio_promedio:,.0f}"],
        textposition="auto",
    )
)
balance_general_fig.add_trace(
    go.Bar(
        x=["Patrimonio + Deuda"],
        y=[deuda_estimada],
        name="Deuda",
        marker_color="#ef553b",
        text=[f"${deuda_estimada:,.0f}"],
        textposition="auto",
    )
)
balance_general_fig.update_layout(
    title="Balance General Simplificado",
    xaxis_title="Estructura",
    yaxis_title="Monto",
    barmode="stack",
    template="plotly_white",
    height=360,
)

chart_col_1, chart_col_2 = st.columns(2)
with chart_col_1:
    st.plotly_chart(estado_resultados_fig, use_container_width=True)

with chart_col_2:
    st.plotly_chart(balance_general_fig, use_container_width=True)
