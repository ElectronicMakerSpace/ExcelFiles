import os

actual_dir = os.path.dirname(__file__)
archivos = os.listdir(actual_dir)

e_principal = '.xlsx'
e_alterna = '.xls'

def identificar_excel(archivos):
    archivos_excel = []
    for archivo in archivos:
        nombre_archivo, extension_archivo = os.path.splitext(archivo)
        #print(f'nombre_archivo: {nombre_archivo}, extension_archivo: {extension_archivo}, tipo: {type(extension_archivo)}')
        if extension_archivo == e_principal or extension_archivo == e_alterna:
            #print(f'Archivo a leer: {archivo}')
            archivos_excel.append(archivo)
    
    return archivos_excel

print(identificar_excel(archivos))