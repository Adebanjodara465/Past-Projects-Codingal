import math  #important for working with trig

from abc import ABC, abstractmethod

class Shapes(ABC):
  @abstractmethod
  def name(self):
    pass
  
  @abstractmethod
  def circumference(self):
    pass
  
  @abstractmethod
  def angle(self):
    pass
  
  @abstractmethod
  def area(self):
    pass
  
  

#circle starts 
class Circle(Shapes):
  def __init__(self, radius):
      self.radius = radius

  def name(self):
      print("\nThe name of the shape is Circle")

  def circumference(self):
      cim = 2 * math.pi * self.radius 
      print(f"The circumference of a circle is {cim:.2f}") # cim:.2f is for PRECISE calculations
      return cim
  
  def angle(self):
      print("The angle of a circle is 360 degrees")
      return 360

  def area(self):
      c_area = math.pi * (self.radius **2)
      print(f"The area of a circle is {c_area:.2f}", )
      return c_area
  
 #circle ends

#triangle starts  
class Triangle(Shapes):
  def __init__(self, height, base, slant):
      self.height = height
      self.base = base
      self.slant = slant

  def name(self):
      print("\nThe name of this shape is Triangle")

  def  circumference(self):
       peri = self.height + self.base + self.slant
       print(f"The perimeter of the triangle is {peri}")
       return peri

  def area(self):
       t_area = (self.height * self.base) / 2  
       print(f"The area of a triangle is {t_area}") 
       return t_area 
  
  def angle(self):
      cosine_A = ((self.base ** 2) + (self.slant ** 2) - (self.height ** 2)) / (2 * self.base * self.slant)
      cosine_A = max(-1, min(1, cosine_A))
      angle_in_rad = math.acos(cosine_A)
      angle_in_deg = math.degrees(angle_in_rad)
      print(f"The angle of this triangle is: {angle_in_deg:.2f} degrees")
      return angle_in_deg
  
#triangle ends

#Square starts
class Square(Shapes):
  def __init__(self, side):
      self.side = side
      self.__fact ='All sides are equal'  #a little encalpsulation

  def name(self):
      print(f"\nThe name of this shape is Square \n{self.__fact}")

  def  circumference(self):
       perimeter = 4 * self.side
       print(f"The perimeter of the square is {perimeter}")
       return perimeter

  def area(self):
      area = self.side ** 2
      print(f"The area of a Square is {area} ")
      return area
  
  def angle(self):
      print("All angles in a square are 90 degrees")
      return 90
      
#square stops here

radius = int(input("Enter your radius of the circle: "))                          
side = int(input("Enter your  side lenght for the square: "))
base = int(input("Enter your triangle base: "))
height = int(input("Enter your triangle heigth: "))
slant = int(input("Enter your triangle slant width: "))


#creating the objects
card = Circle(radius)
card.name()
card.circumference()
card.angle()
card.area()


box = Square(side)
box.name()
box.circumference()
box.angle()
box.area()

cake = Triangle(height, base, slant)
cake.name()
cake.circumference()
cake.angle()
cake.area()
