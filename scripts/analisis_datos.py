# ==========================================
# analisis_datos.py
# ROL: Paco (Programador) | Issue: TPU4-5
# Escenario A - Análisis de Datos Climáticos
# Dataset: annual.csv (GISTEMP - anomalías de temperatura global)
# ==========================================

import pandas as pd
import os

# ---- 1. CARGA DE DATOS ----
# Usamos ruta relativa para garantizar reproducibilidad en Google Colab
ruta_archivo = os.path.join("datos", "annual.csv")

# Pandas lee el CSV y lo convierte en un DataFrame para operar fácilmente
df = pd.read_csv(ruta_archivo)

# ---- 2. CÁLCULOS ESTADÍSTICOS ----
# Usamos la columna "Mean" que contiene las anomalías de temperatura
promedio = df["Mean"].mean()
maxima = df["Mean"].max()
minima = df["Mean"].min()
cantidad_datos = len(df)

# ---- 3. RESULTADOS EN PANTALLA ----
print("--- RESULTADOS DEL CLIMA (annual.csv) ---")
print("Cantidad de registros analizados:", cantidad_datos)
print("Anomalía Promedio:", round(promedio, 4))
print("Anomalía Máxima Registrada:", maxima)
print("Anomalía Mínima Registrada:", minima)

# ---- 4. GRÁFICO ----
# Pandas tiene su propio método para graficar, usando matplotlib internamente
# Visualizamos la evolución temporal de las anomalías de temperatura
os.makedirs("resultados", exist_ok=True)

ax = df.plot(x="Year", y="Mean", figsize=(10, 5), color="steelblue", linewidth=1.5, legend=False)
ax.axhline(y=promedio, color="red", linestyle="--", label=f"Promedio: {round(promedio, 4)}")
ax.set_title("Evolución de Anomalías de Temperatura Global")
ax.set_xlabel("Año")
ax.set_ylabel("Anomalía de Temperatura (°C)")
ax.legend()

# Guardamos el gráfico en /resultados con ruta relativa
figura = ax.get_figure()
figura.savefig(os.path.join("resultados", "grafico_temperatura.png"))
print("Gráfico guardado en resultados/grafico_temperatura.png")

# ==========================================
# REVISIÓN P3 - Luis (QA) | Issue: TPU4-6
# - Verificado: no se exponen credenciales ni rutas absolutas
# - Verificado: gráfico guardado correctamente en /resultados
# - Sugerencia: agregar manejo de excepciones para archivo faltante
# ==========================================

# ==========================================
# REVISIÓN P3 - Luis (QA) | Issue: TPU4-6
# - Verificado: no se exponen credenciales ni rutas absolutas
# - Verificado: gráfico guardado correctamente en /resultados
# - Sugerencia: agregar manejo de excepciones para archivo faltante
# ==========================================
