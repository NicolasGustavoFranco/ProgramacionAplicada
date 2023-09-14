import random

f=open("NumerosAleatorios1.txt", "x")

while True:
       Numale = random.random()
       Data =[Numale]
       f= open("NumerosAleatorios1.txt","a")

       for d in Data:

          f.write(str(d))
          f.write("\n ")

          f.close()
