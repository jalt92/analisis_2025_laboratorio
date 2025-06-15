import pandas as pd
from abc import ABC, abstractmethod

class Dataset(ABC):
    def __init__(self, fuente):
        self.__fuente = fuente
        self.__datos = None

    @property
    def datos(self):
        return self.__datos

    @datos.setter
    def datos(self, value):
        self.__datos = value

    @property
    def fuente(self):
        return self.__fuente

    @abstractmethod
    def cargar_datos(self):
        pass

    def validar_y_limpiar(self):
                                try:
                                    self.__datos.columns = (
                                        self.__datos.columns.str.lower()
                                        .str.replace(" ", "_", regex=False)
                                        .str.replace("", "_")
                                    )

                                    self.__datos = self.__datos.drop_duplicates()
                                    self.__datos = self.__datos.copy()

                                    for col in self.__datos.select_dtypes(include="object").columns:
                                        self.__datos.loc[:, col] = self.__datos[col].astype(str).str.strip()

                                    print(" Validando tipos de datos...")

                                    # Solo si están definidos los tipos esperados
                                    if hasattr(self, '_tipos_esperados'):
                                        for columna, tipo in self._tipos_esperados.items():
                                            if columna not in self.__datos.columns:
                                                print(f"Columna '{columna}' no encontrada.")
                                                continue

                                            if tipo == "numero":
                                                self.__datos[columna] = pd.to_numeric(self.__datos[columna], errors='coerce')
                                            elif tipo == "texto":
                                                self.__datos[columna] = self.__datos[columna].astype(str)
                                            elif tipo == "fecha":
                                                self.__datos[columna] = pd.to_datetime(self.__datos[columna], errors='coerce')

                                    #solo si están definidos los campos obligatorios
                                    if hasattr(self, '_campos_obligatorios'):
                                        self.__datos = self.__datos.dropna(subset=self._campos_obligatorios)

                                    self.__datos = self.__datos.dropna()
                                    print("Limpieza y validación completa.\n")
                                    return True

                                except Exception as e:
                                    print(f"Error durante validación/limpieza: {e}")
                                    return False
    def mostrar_resumen(self):
        return print(self.datos.describe(include='all') if self.datos is not None else "no hay datos") #include, trae las columas que necesitemos