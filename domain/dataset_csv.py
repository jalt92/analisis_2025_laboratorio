import pandas as pd
from domain.dataset import Dataset

class DatasetCSV(Dataset):
    def __init__(self, fuente):
        super().__init__(fuente)

    def cargar_datos(self):
        try:
            df = pd.read_csv(self.fuente, dtype=str)
            self.datos = df
            print("CSV cargado")

            if self.validar_y_limpiar():
                print("Datos Validados y Limpiados")
                return True
        except Exception as e:
            print(f"Error cargando CSV: {e}")