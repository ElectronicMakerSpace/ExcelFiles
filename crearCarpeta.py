import os

directory = "Resultados"

if not os.path.exists(directory):
    os.makedirs(directory)
    print(f'Carpeta "{directory}" creada')
else:
    print(f'Carpeta "{directory}" Ya existe')