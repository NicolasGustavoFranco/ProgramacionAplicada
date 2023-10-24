class Circle:
  pi = 3.14

  def __init__(self, diameter):
    print("Creating circle with diameter {d}".format(d=diameter))
    self.radius = diameter / 2

  def circumference(self):
    perimetro=2*Circle.pi*self.radius
    return perimetro
  
  def area(self):
        area=Circle.pi*self.radius**2
        return area


circulo=Circle(6)
percirculo=circulo.circumference()
print(percirculo)

areacirculo=circulo.area()
print(areacirculo)


class triangulo:
   
 def __init__(self, lado1,lado2,lado3):
    print("Crear triangulo con lados {d},{b},{c}".format(d=lado1,b=lado2,c=lado3))
    self.l1=lado1
    self.l2=lado2
    self.l3=lado3

 def Perimetro(self):
    perimetro = self.l1+self.l2+self.l3

    return perimetro
  
 def Area(self):
        area=(self.l1*self.l2)/2
        return area
 
Triangulo=triangulo(3,2,4)
pertri=Triangulo.Perimetro()
print(pertri)

areatri=Triangulo.Area()
print(areatri)

class Cuadrado:
   
 def __init__(self, lado):
    print("Crear cuadrado con lados {d}".format(d=lado))
    self.l=lado
    
 def Perimetro(self):
    perimetro = self.l*4

    return perimetro
  
 def Area(self):
        area=self.l*2
        return area
 
cuadrado=Cuadrado(4)
percuadra=cuadrado.Perimetro()
print(percuadra)

areacuadra=cuadrado.Area()
print(areacuadra)


class Rectangulo:
   
 def __init__(self, lado,lado2):
    print("Crear rectangulo con lados {d},{c}".format(d=lado,c=lado2))
    self.l=lado
    self.l2=lado2

 def Perimetro(self):
    perimetro = (self.l*2) + (self.l2*2)

    return perimetro
  
 def Area(self):
        area=self.l*self.l2
        return area
 
rectangulo=Rectangulo(4,3)
perrecta=rectangulo.Perimetro()
print(perrecta)

arearecta=rectangulo.Area()
print(arearecta)
