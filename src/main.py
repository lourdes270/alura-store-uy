import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# datos
DATA_DIR = Path("datos")

def cargar_datos():
    """
    Carga los 4 archivos CSV de las tiendas desde datos/
    y devuelve un diccionario de DataFrames.
    """
    files = {
        "tienda1": DATA_DIR / "tienda_1.csv",
        "tienda2": DATA_DIR / "tienda_2.csv",
        "tienda3": DATA_DIR / "tienda_3.csv",
        "tienda4": DATA_DIR / "tienda_4.csv",
    }

    dataframes = {name: pd.read_csv(path) for name, path in files.items()}

    # verifico
    for name, df in dataframes.items():
        print(f"👉 {name}: {df.shape[0]} filas, {df.shape[1]} columnas")
        print(df.head(), "\n")

    return dataframes

def main():
    datos = cargar_datos()
    # graficos 

if __name__ == "__main__":
    main()
