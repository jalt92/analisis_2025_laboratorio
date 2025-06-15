import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from decouple import config



class DataSaver:
    def __init__(self):
        user = config('DB_USER')
        password = config('DB_PASSWORD')
        host = config('DB_HOST')
        database = config('DB_NAME')
        port = config('DB_PORT')

        url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
        self.engine = create_engine(url)

    def guardar_dataFrame(self, df, nombre_tabla):
        if df is None:
            print(f"No se puede guardar: datos vacios para {nombre_tabla}.")
            return
        
        if not isinstance(df, pd.DataFrame):
            print(f"Tipo invalido: se esperaba un DataFrame, se recibio {type(df)}.")
            return

        try:
            df.to_sql(nombre_tabla, con=self.engine, if_exists='replace', index=False)
            print(f"Datos Guardados en tabla: {nombre_tabla}.")

        except SQLAlchemyError as e:
            print(f"Error guardando datos: {e}.")