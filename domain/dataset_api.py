import requests
import pandas as pd
from domain.dataset import Dataset

class DatasetAPI(Dataset):
    def __init__(self, fuente):
        super().__init__(fuente)
        
    def cargar_datos(self):
        try: 
            response = requests.get(self.fuente)
            if response.status_code == 200: #url nos devolvio informacion
                df = pd.json_normalize (response.json())
                #verificar si es un lista
                def es_lista(x):
                    return isinstance(x, list)
                #preguntar si es una lista y transformarla a string
                def lista_a_string(x):
                    if isinstance(x, list):
                        return ', '.join(map(str, x)) #map sirve para transforma una funcion y los hace iterable y tranforma a "str",
                
                for col in df.columns:
                    if df[col].apply(es_lista).any():
                        df[col] = df[col].apply(lista_a_string)

                self.datos = df
                print("API cargada")

                if self.validar_y_limpiar():
                    print("Datos validados y limpiados desde API")
            else:
                print("Error al obtener datos de API")

        except Exception as e:
            print(f"Error API. {e}")