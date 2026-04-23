# Bitacora de Cambios - ROE DuPont Interactivo

Registro resumido de avances del proyecto, enfocado en cambios funcionales y aprendizajes de desarrollo.

---

## 2026-04-21 | Funcionalidad 1 - Ratios financieros basicos

**Descripcion del cambio**

- Se implemento la captura de 4 variables contables con `sliders`:
  - Utilidad Neta
  - Ventas
  - Activos Promedio
  - Patrimonio Promedio
- Se incorporo el calculo automatico de:
  - Margen Neto
  - Rotacion de Activos
  - Apalancamiento Financiero
  - ROE (modelo DuPont)
- Se agrego visualizacion clara de resultados con `st.metric`.
- Se incluyo validacion para divisiones por cero.
- Se ajusto la interfaz:
  - Titulo actualizado a "Analisis Financiero con el Modelo Dupont".
  - Variables de entrada movidas al menu lateral izquierdo.
  - Mensaje informativo destacado con `st.sidebar.info`.
  - Se retiro la seccion de vista rapida solicitada en ese momento.

**Aprendizaje asociado**

- En apps pedagogicas, la claridad visual (sidebar + metricas) mejora la comprension antes que agregar complejidad grafica.
- Validar casos borde (ej. denominadores en cero) evita errores y mejora la experiencia de usuario.

---

## 2026-04-21 | Funcionalidad 2 - Visualizacion 3D del Prisma ROE

**Descripcion del cambio**

- Se desarrollo la visualizacion 3D del prisma DuPont con Plotly (`Mesh3d`).
- Se agregaron aristas para reforzar lectura geometrica del volumen.
- Se configuraron ejes explicativos:
  - Margen Neto
  - Rotacion de Activos
  - Apalancamiento Financiero
- La visualizacion se actualiza dinamicamente segun los sliders de entrada.
- Se agrego mensaje de apoyo para escenarios con margen negativo.

**Aprendizaje asociado**

- Una visualizacion 3D educativa requiere equilibrio entre precision y legibilidad.
- La interpretacion mejora cuando se explicita como se mapea cada eje con el modelo financiero.

---

## 2026-04-21 | Funcionalidad 3 - Estados Financieros Simplificados

**Descripcion del cambio**

- Se implemento el Estado de Resultados simplificado en barras horizontales.
- Se aplico la logica contable solicitada:
  - `Ventas = Gastos + Utilidad Neta`
  - `Gastos = Ventas - Utilidad Neta`
- Se implemento el Balance General simplificado.
- Se ajusto el Balance para mostrarse en estructura apilada:
  - Columna 1: Activos
  - Columna 2: Patrimonio + Deuda
- Se incorporaron alertas cuando aparecen valores negativos por combinaciones extremas de entrada.

**Aprendizaje asociado**

- Definir identidades contables explicitas en el codigo facilita trazabilidad y revision funcional.
- Ajustar la estructura del grafico segun feedback de usuario mejora la interpretacion gerencial.

---

## 2026-04-21 | Aprendizajes de proceso (metodologia de trabajo)

**Descripcion del cambio**

- Se trabajo por iteraciones cortas, validando cada ajuste de UI y logica antes de continuar.
- Se priorizo cumplir primero requerimientos funcionales y luego ajustes de presentacion.

**Aprendizaje asociado**

- Cuando el modo agente no interpreta bien una solicitud o hace cambios fuera de alcance, conviene pasar temporalmente a un enfoque de consulta/validacion (Ask) para alinear requerimientos antes de seguir implementando.
- Confirmar cambios pequenos de forma incremental reduce retrabajo y acelera la convergencia con lo que espera el usuario final.

