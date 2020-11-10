from tqdm import tqdm 
import time, sys 

def update_progress(progress):
    barLength = 10 # Modify this to change the length of the progress bar
    status = ""
    if isinstance(progress, int):
        progress = float(progress)
    if not isinstance(progress, float):
        progress = 0
        status = "error: progress var must be float\r\n"
    if progress < 0:
        progress = 0
        status = "Halt...\r\n"
    if progress >= 1:
        progress = 1
        status = "Done...\r\n"
    block = int(round(barLength*progress))
    text = "\rPercent: [{0}] {1}% {2}".format( "#"*block + "-"*(barLength-block), progress*100, status)
    sys.stdout.write(text)
    sys.stdout.flush()

a = [1,2,3,4,5]
b = [1,2,3,4,5,6,7,8,9,10]

rango = (len(a)  * len(b)) + len(b)

# Forlmula general
# rango = (len(a)  * len(b)) + len(b) + len(a)

print(f"Rango: {rango}")
contador = 1

for i in range(len(a) + 1):
    for j in range(1, len(b) + 1):
        
        print(f'\ncontador[{contador}]: {j},{i}')
        #update_progress(contador/rango)
        
        if contador in tqdm (range (rango), desc="Loading..."):
            pass
            #time.sleep(0.1)
        #    contador += 1

        contador += 1