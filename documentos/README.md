# Analisis Financiero con el Modelo Dupont

Aplicacion interactiva desarrollada con Streamlit y Plotly para ensenar, de forma visual y practica, como se descompone la rentabilidad financiera (ROE) mediante el modelo DuPont.

El proyecto esta orientado a aprendizaje tecnico-financiero: permite modificar variables contables clave y observar en tiempo real el impacto sobre los ratios, la representacion 3D del prisma DuPont y estados financieros simplificados.

## 1) Descripcion general y proposito

`Roe_Dupont` busca convertir el modelo DuPont en una experiencia didactica e interactiva.  
A partir de 4 variables de entrada:

- Utilidad Neta
- Ventas
- Activos Promedio
- Patrimonio Promedio

la app calcula los componentes del modelo y muestra salidas visuales para apoyar la interpretacion gerencial.

Objetivo pedagogico principal:

- Entender la relacion entre margen, eficiencia operativa y estructura financiera.
- Conectar ratios con una lectura contable simplificada (estado de resultados y balance).
- Practicar desarrollo incremental por funcionalidades/sprints.

## 2) Caracteristicas principales implementadas

Actualmente el proyecto incluye las tres funcionalidades definidas en `documentos/funcionalidades_proyecto`:

### Funcionalidad 1 - Ratios financieros DuPont

- Captura de variables mediante sliders en el menu lateral.
- Calculo automatico de:
  - Margen Neto
  - Rotacion de Activos
  - Apalancamiento Financiero
- Calculo de ROE como producto de los tres componentes.
- Visualizacion con metricas claras en pantalla.
- Manejo de divisiones por cero para evitar errores de ejecucion.

### Funcionalidad 2 - Visualizacion 3D del Prisma ROE

- Prisma 3D en Plotly (`Mesh3d`) que representa la interaccion de los 3 factores DuPont.
- Actualizacion dinamica al mover sliders.
- Ejes explicativos para reforzar interpretacion del modelo.

### Funcionalidad 3 - Estados Financieros Simplificados

- Estado de Resultados simplificado con barras horizontales.
- Logica aplicada: `Ventas = Gastos + Utilidad Neta`.
- Balance General simplificado con estructura apilada:
  - Columna 1: Activos
  - Columna 2: Patrimonio + Deuda
- Alertas cuando se generan escenarios no convencionales (por ejemplo, deuda o gastos negativos por combinacion de entradas).

## 3) Requisitos tecnicos

### Python

- Recomendado: Python 3.13 (entorno detectado del proyecto: `3.13.13`)
- Compatible esperado: Python 3.10+

### Librerias necesarias

Definidas en `documentos/requirements.txt`:

- `streamlit`
- `plotly`
- `numpy`
- `pandas`

## 4) Instalacion paso a paso

Desde la raiz del proyecto:

1. Crear entorno virtual:

```bash
python -m venv .venv
```

2. Activar entorno virtual:

- PowerShell (Windows):

```powershell
.\.venv\Scripts\Activate.ps1
```

- CMD (Windows):

```cmd
.\.venv\Scripts\activate.bat
```

3. Instalar dependencias:

```bash
python -m pip install --upgrade pip
python -m pip install -r documentos/requirements.txt
```

4. Ejecutar la aplicacion:

```bash
streamlit run app.py
```

5. Abrir en navegador la URL mostrada por Streamlit (normalmente `http://localhost:8501`).

## 5) Guia de uso con ejemplos basicos

1. En el panel lateral, ajusta:
   - Utilidad Neta
   - Ventas
   - Activos Promedio
   - Patrimonio Promedio
2. Revisa `Resultados DuPont`:
   - Margen Neto (%)
   - Rotacion de Activos (x)
   - Apalancamiento Financiero (x)
   - ROE (%)
3. Explora el `Prisma 3D` para observar el efecto conjunto de los tres factores.
4. Analiza los estados financieros simplificados para verificar coherencia contable.

Ejemplo rapido:

- Si aumentas `Utilidad Neta` manteniendo constantes las demas variables:
  - Sube Margen Neto.
  - Sube ROE.
  - Cambia la forma del prisma (eje de margen).

- Si aumentas `Activos Promedio` con ventas constantes:
  - Baja la Rotacion de Activos.
  - Puede aumentar el apalancamiento segun el patrimonio.
  - El efecto final en ROE depende de la combinacion total.

## 6) Estructura del proyecto

```text
Roe_Dupont/
|-- app.py
|-- README.md
|-- documentos/
|   |-- funcionalidades_proyecto
|   `-- requirements.txt
|-- .cursor/
|   `-- rules/
|       `-- ReglasProyecto.mdc
`-- .venv/  (entorno local, no versionar)
```

Archivos clave:

- `app.py`: aplicacion principal con funcionalidades 1, 2 y 3.
- `documentos/funcionalidades_proyecto`: especificacion funcional por sprints.
- `documentos/requirements.txt`: dependencias del proyecto.

## 7) Interpretacion pedagogica de resultados

Lectura sugerida para clase o autoaprendizaje:

- **Margen Neto**: mide que porcentaje de las ventas termina como utilidad.
- **Rotacion de Activos**: indica que tan eficientemente los activos generan ventas.
- **Apalancamiento Financiero**: refleja el grado de financiamiento relativo al patrimonio.
- **ROE**: resume rentabilidad para el accionista como efecto combinado de los tres factores.

Relaciones clave:

- Un ROE alto puede venir de mayor margen, mayor rotacion o mayor apalancamiento (o mezcla de los tres).
- El prisma 3D ayuda a visualizar esta interdependencia y evita analizar cada ratio de forma aislada.
- Los graficos de estado de resultados y balance permiten validar consistencia basica entre ratios y estructura contable.

## 8) Licencia y nota educativa

### Licencia

Actualmente este repositorio no define una licencia de software explicita.  
Si se desea distribuir o reutilizar formalmente, se recomienda agregar un archivo `LICENSE` (por ejemplo, MIT).

### Nota educativa

Este proyecto tiene fines pedagogicos.  
Su objetivo es apoyar el aprendizaje de analisis financiero con Python, Streamlit y Plotly, no sustituir modelos de valuacion o auditoria profesional.
