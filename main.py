from os import path
from domain.dataset_csv import DatasetCSV
from domain.dataset_excel import DatasetExcel
from domain.dataset_api import DatasetAPI
from data.data_saver import DataSaver
# import sqlite3


# Rutas de Archivos
csv_path = path.join(path.dirname(__file__), "file\\series-tiempo-valores.csv")
excel_path = path.join(path.dirname(__file__), "file\\Ventas Tech-1.xlsx")

# Cargar y Transformar Datos CSV,Excel,etc.
csv = DatasetCSV(csv_path)
csv.cargar_datos()
csv.mostrar_resumen()

excel = DatasetExcel(excel_path)
excel.cargar_datos()

# api = DatasetAPI("https://apis.datos.gob.ar/georef/api/municipios?provincia=22&campos=id,nombre&max=100")
# api.cargar_datos()

#Guardar datos en db
db = DataSaver()
db.guardar_dataFrame(csv.datos, "series_tiempo_valores_csv")
db.guardar_dataFrame(excel.datos, "ventas_tech_xlsx")
# db.guardar_dataFrame(api.datos, "municipio_api")                    #no pude abrir el db desde la libreria sqlite y busco como ver desde la terminal para saber si quedaba guarado en la base de datos:
                                                                    # db_path = "db/guardado.db"
                                                                    # nombre_tabla = "series_tiempo_valores_csv" 

                                                                    # db = DataSaver(db_path)
                                                                    # db.guardar_dataFrame(csv.datos, nombre_tabla)

                                                                    # # Verificar qué tablas se crearon
                                                                    # conn = sqlite3.connect(db_path)
                                                                    # cursor = conn.cursor()

                                                                    # cursor.execute("SELECT name FROM sqlite_master WHERE type='table' OR type='view';")
                                                                    # tablas = cursor.fetchall()
                                                                    # print("Tablas en la base de datos:", tablas)

                                                                    # conn.close()


# Mostrar resultado final
#print(csv.datos)
#print(excel.datos)
#print(api.datos)