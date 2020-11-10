from tqdm import tqdm 
import time

for i in tqdm (range (5), desc="Trabajando..."): 
    time.sleep(0.1)
    
