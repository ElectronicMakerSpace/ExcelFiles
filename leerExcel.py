import pandas as pd
import xlrd
import xlwt

archivo_excel = pd.read_excel('clavesoki.xlsx')
print(archivo_excel.columns)
#values = archivo_excel['Identificador'].values
#print(values)
cadena = "Starter Kit,Board&Shield,Sensor&Module,Relay Module,Display,Car Robot,For MICRO BIT,Servo,For Raspberry PI,Spare Part "
columnas = cadena.split(",")

df_seleccionados = archivo_excel[columnas]
print(df_seleccionados)

documento = xlrd.open_workbook("clavesoki.xlsx")
claves = documento.sheet_by_index(0)

#Guardamos la informacion de la celda (0,1) de la hoja de claves
#Los tipos de celda son: 0-Vacia, 1-Texto, 2-Numero, 3-Fecha, 4-Booleano, 5-Error
tipo_de_celda = claves.cell_type(0, 1)
print("Tipo de celda: " + str(tipo_de_celda))
 
contenido_celda = claves.cell_value(0,1)
print("Contenido de la celda: \"" + str(contenido_celda) + "\"")

if 'OKY' in contenido_celda:
    print(f'contenido_celda: {contenido_celda}, typo {type(contenido_celda)}')
else:
    print("NO OKI")

columnas_claves = claves.ncols
filas_claves = claves.nrows
print("claves tiene " + str(filas_claves) + " filas y " + str(columnas_claves) + " columnas")

#Mostramos el contenido de todas las filas de la hoja de libros
for i in range(10): #claves.ncols para el numero de columnas
    fila = claves.row(i) #claves.col(i) para mostrar las columnas
    print(fila)