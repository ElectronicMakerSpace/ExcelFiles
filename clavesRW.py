from colorama import init, Fore, Back, Style
from bs4 import BeautifulSoup
from datetime import datetime
import requests, math
import pandas as pd
import xlrd, xlwt
from os import system

def num_paginas(resultados):
                #for resultado in resultados:
                sin_espacios = resultados[0].getText().strip().split()
                #print(f' Texto: {sin_espacios}, tipo{type(sin_espacios)}')
                inicio = int(sin_espacios[2])
                fin = int(sin_espacios[4])

                if inicio <=0 or fin <= 0:
                    paginas = 0
                else:
                    paginas = math.ceil(fin / inicio)

                #print(f'{inicio}, {fin} tipo inicio: {type(inicio)}')
                return inicio, fin, paginas

init()

documento = xlrd.open_workbook("clavesoki.xlsx")
claves = documento.sheet_by_index(0)

filas = claves.nrows
columnas = claves.ncols
#print("clavesoki tiene " + str(filas) + " filas y " + str(columnas) + " columnas")

style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',num_format_str='#,##0.00')

wb = xlwt.Workbook()
ws = wb.add_sheet('Resultados OKY')

for i in range(columnas):
    for j in range(filas):
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
                print(Fore.RED + f'La clave: {contenido_celda} No esta en el Stock')
                #print(f'La clave: {contenido_celda} No esta en el Stock')
                ws.write(j, i, contenido_celda, style0)
            else:
                print(Fore.GREEN + f'La clave: {contenido_celda} Ya esta en el Stock')
                #print(f'La clave: {contenido_celda} ya esta en el Stock')
                ws.write(j, i, contenido_celda)
            
            wb.save('OKIData.xlsx')

        else:
            pass

print(Back.GREEN + 'Hemos Terminado, Examine su archivo.xlsx')
#print(f'Hemos Terminado, Examine su archivo.xlsx')
wb.save('OKIData.xlsx')