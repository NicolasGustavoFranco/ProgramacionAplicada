import csv
import random
from csv import writer

Numale = random.random()


fields = ['NUMERO']
  
rows = [[Numale]]
 

filename = "NumerosAleatorios.csv"
 

with open(filename, 'w') as csvfile:
   
    csvwriter = csv.writer(csvfile)
     
    
    csvwriter.writerow(fields)
     
    
    csvwriter.writerows(rows)
    
csvfile.close()


while True:
      Numale1 = random.random()
      row_contents = [Numale1]

      with open("NumerosAleatorios.csv", 'a+', newline='') as write_obj:
        
        csv_writer = writer(write_obj)
        
        csv_writer.writerow(row_contents)
