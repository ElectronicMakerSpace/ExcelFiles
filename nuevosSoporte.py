from colorama import init, Fore, Back, Style
from datetime import datetime
import requests, math
from tqdm import tqdm 
import xlrd, xlwt
from os import system
import os


def identificar_excel(archivos):
    archivos_excel = []
    for archivo in archivos:
        nombre_archivo, extension_archivo = os.path.splitext(archivo)
        #print(f'nombre_archivo: {nombre_archivo}, extension_archivo: {extension_archivo}, tipo: {type(extension_archivo)}')
        if extension_archivo == e_principal or extension_archivo == e_alterna:
            #print(f'Archivo a leer: {archivo}')
            archivos_excel.append(archivo)
    
    return archivos_excel

def crear_directorio(carpeta):
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)
        print(f'Carpeta "{carpeta}" creada')
        return carpeta
    else:
        print(f'Carpeta "{carpeta}" Ya existe')
        return carpeta

#directorio = crear_directorio("Resultados")
salida = "palabras.xlsx"

# Inicio de colores
init()

actual_dir = os.path.dirname(__file__)
archivos = os.listdir(actual_dir)
e_principal = '.xlsx'
e_alterna = '.xls'
contador = 1

# Buscando archivos de excel
excel = identificar_excel(archivos)
archivo = excel[1]

documento = xlrd.open_workbook(archivo)
claves = documento.sheet_by_index(0)

filas = claves.nrows
columnas = claves.ncols
print(f"{archivo} tiene " + str(filas) + " filas y " + str(columnas) + " columnas")

rango = (filas * columnas)

style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',num_format_str='#,##0.00')

wb = xlwt.Workbook()
ws = wb.add_sheet('Resultados Palabras')

for i in range(filas):
    for j in range(columnas):
        #print(f'{j},{i}')
        contenido_celda = claves.cell_value(j,i)

        if j == 0:
            ws.write(j, i, contenido_celda)

        if 'OKY' in contenido_celda:
            validacion = requests.get(f'https://www.agelectronica.com/?n={contenido_celda}')
            soup = BeautifulSoup(validacion.content, 'html.parser')
            
            resultados = soup.findAll("td", {"align": ["right"]})
            inicio, fin, paginas = num_paginas(resultados)
            #print(f'num_paginas: {paginas}')

            if paginas == 0:
                print(Fore.RED + f'\nLa clave: {contenido_celda} No esta en el Stock')
                #print(f'La clave: {contenido_celda} No esta en el Stock')
                ws.write(j, i, contenido_celda, style0)
            else:
                print(Fore.GREEN + f'\nLa clave: {contenido_celda} Ya esta en el Stock')
                #print(f'La clave: {contenido_celda} ya esta en el Stock')
                ws.write(j, i, contenido_celda)
            
            wb.save('Resultados/OKIData.xlsx')

        else:
            #print(Style.RESET_ALL)
            #print("Buscado clave...")
            pass

        print(Style.RESET_ALL)
        if contador in tqdm (range (rango), desc="Procesando Informacion..."):
            pass
            #time.sleep(0.1)
        #    contador += 1

        contador += 1

print(Back.BLUE + f'\nHemos Terminado, Examine su archivo: {archivo}.xlsx')
#print(f'Hemos Terminado, Examine su archivo.xlsx')
wb.save('OKIData.xlsx')