""""
create a class and sub-class objects which represent different geometrical shapes

the shapes should be like rectangles, squares and any other sraight line type

the shapes should be classes, they should have the ability to compute routine geo-calcs

so yeah   Let's try with abstraction
"""
from abc import ABC, abstractmethod

class Shapes(ABC):
  @abstractmethod
  def name(self):
    pass
  
  @abstractmethod
  def area(self):
    pass
  
  @abstractmethod
  def perimeter(self):
    pass
  
  

#rectangle starts 
class Rectangle(Shapes):
  def __init__(self, length, width):
    self.length = length
    self.width = width

  def name(self):
    print("The name of this shape is Rectangle")

  def area(self): #length x braedth
    Area = self.length * self.width
    print("The area of a rectangle is ", Area)
    return Area

  def perimeter(self):
    Peri = 2 * (self.length + self.width)
    print("The perimeter of your Rectangle is", Peri)
    return Peri
 #rectangle ends

#triangle starts  
class Triangle(Shapes):
  def __init__(self, base, heigth, slant):
    self.base = base
    self.heigth = heigth
    self.slant = slant

  def name(self):
    print("the name of this shape is Triangle") 

  def area(self):
    t_area = (self.heigth * self.base) / 2  
    print("The area of a triangle is ", t_area) 
    return t_area

  def perimeter(self):
    P = self.base + self.slant + self.slant
    print("The perimeter of your Triangle is", P)
    return P 
#triangle ends

#Square starts
class Square(Shapes):
  def __init__(self, side):
    self.side = side

  def name(self):
    print("The name of this shape is Square")

  def area(self):
    area = self.side * self.side
    print("The area of a Square is ", area)
    return area
  
  def perimeter(self):
    peri = 4 * self.side
    print("The perimeter of your rectangle is", peri)
    return peri
#square stops here

length = int(input("Enter your lenght: "))
width = int(input("Enter your width: "))
side = int(input("Enter your  side width: "))
slant = int(input("Enter your triangle slant width: "))
heigth = int(input("Enter your triangle heigth width: "))
base = int(input("Enter your triangle base width: "))


#creating the objects
box = Square(side)
box.name()
box.area()

field = Rectangle(length, width)
field.area()

toy = Triangle(base, heigth, slant)
toy.perimeter()
toy.area()