import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

DATA_DIR = Path("datos")
OUT_DIR = Path("reports/figures")
OUT_DIR.mkdir(parents=True, exist_ok=True)

COLS = {
    "categoria": "Categoría del producto",
    "precio": "Precio",
    "resena": "Calificación",
    "envio": "Costo de envío",
}

def _save(ax, name):
    plt.tight_layout()
    p = OUT_DIR / name
    plt.savefig(p)
    plt.close()
    print(f"[ok] {p}")

def cargar():
    archivos = {
        "Tienda A": DATA_DIR / "tienda_1.csv",
        "Tienda B": DATA_DIR / "tienda_2.csv",
        "Tienda C": DATA_DIR / "tienda_3.csv",
        "Tienda D": DATA_DIR / "tienda_4.csv",
    }
    dfs = []
    for tienda, path in archivos.items():
        df = pd.read_csv(path)
        df["tienda"] = tienda
        dfs.append(df)
    return pd.concat(dfs, ignore_index=True)

def grafico_ingresos_por_tienda(df):
    df["ingresos"] = df[COLS["precio"]]
    s = df.groupby("tienda")["ingresos"].sum().sort_values(ascending=False)
    ax = s.plot(kind="bar", title="Ingresos totales por tienda")
    ax.set_ylabel("Ingresos")
    _save(ax, "01_ingresos_por_tienda.png")

def grafico_top_categorias(df, top=10):
    df["ingresos"] = df[COLS["precio"]]
    s = (
        df.groupby(COLS["categoria"])["ingresos"]
        .sum()
        .sort_values(ascending=False)
        .head(top)
    )
    ax = s.plot(kind="bar", title=f"Top {top} categorías por ingresos")
    ax.set_ylabel("Ingresos")
    ax.set_xlabel("Categoría")
    _save(ax, "02_top_categorias.png")

def grafico_resenas(df):
    s = df[COLS["resena"]].value_counts().sort_index()
    ax = s.plot(kind="bar", title="Distribución de calificaciones")
    ax.set_xlabel("Puntuación")
    ax.set_ylabel("Cantidad")
    _save(ax, "03_distribucion_calificaciones.png")

def grafico_envio_promedio(df):
    s = df.groupby("tienda")[COLS["envio"]].mean().sort_values()
    ax = s.plot(kind="bar", title="Costo de envío promedio por tienda")
    ax.set_ylabel("Costo promedio")
    _save(ax, "04_envio_promedio.png")

def main():
    df = cargar()
    grafico_ingresos_por_tienda(df)
    grafico_top_categorias(df, top=10)
    grafico_resenas(df)
    grafico_envio_promedio(df)

if __name__ == "__main__":
    main()

